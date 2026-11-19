# 자전거 시간당 대여량 회귀 예측
# 참고: pro10anal1/mplot5bike.py, ex29rf.py, ex28quiz.py
# 원본 문제: https://www.kaggle.com/c/bike-sharing-demand/data
# 사용자가 다운로드한 train.csv를 bike_dataset.csv로 복사해 사용한다.
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# 1. 데이터 읽기 및 확인
csv_path = Path(__file__).resolve().with_name('bike_dataset.csv')
data = pd.read_csv(csv_path, parse_dates=['datetime'])
print(data.head(2))
print('데이터 크기:', data.shape)
print('결측치:\n', data.isnull().sum())

# 2. 날짜/시간을 숫자 특성으로 변환 (수업에서 배운 .dt 사용)
data['year'] = data['datetime'].dt.year
data['month'] = data['datetime'].dt.month
data['hour'] = data['datetime'].dt.hour
data['dayofweek'] = data['datetime'].dt.dayofweek  # 월요일 0 ~ 일요일 6

# casual + registered = count이므로 두 열은 정답 유출을 막기 위해 제외
feature = data.drop(columns=['datetime', 'casual', 'registered', 'count'])
label = data['count']

# 3. 학습용 70%, 평가용 30% 분리
# 수업 방식의 무작위 분할이다. 미래 시점 예측 검증에는 시간순 분할이 필요하다.
x_train, x_test, y_train, y_test = train_test_split(
    feature, label, test_size=0.3, random_state=12
)
print('학습용/평가용 크기:', x_train.shape, x_test.shape)

# 4. 학습 데이터만으로 변수 중요도 판단
first_model = RandomForestRegressor(n_estimators=200, random_state=12, n_jobs=-1)
first_model.fit(x_train, y_train)
ranking = pd.DataFrame({
    'feature': x_train.columns,
    'importance': first_model.feature_importances_
}).sort_values(by='importance', ascending=False)
print('\n변수 중요도 순위:\n', ranking.to_string(index=False))

# 5. 중요도 상위 5개 변수 선택 (평가 결과를 보기 전에 개수 지정)
selected_features = ranking['feature'].head(5).tolist()
print('\n선택한 feature:', selected_features)

# 6. 선택한 변수로 최종 회귀 모델 학습
model = RandomForestRegressor(n_estimators=200, random_state=12, n_jobs=-1)
model.fit(x_train[selected_features], y_train)

# 7. 평가용 데이터의 대여량 예측 및 성능 평가
pred = model.predict(x_test[selected_features])
result = pd.DataFrame({'실제 대여량': y_test, '예측 대여량': pred})
print('\n예측 결과 10개:\n', result.head(10))
mse = mean_squared_error(y_test, pred)
print(f'MSE: {mse:.3f}')
print(f'RMSE: {np.sqrt(mse):.3f}')
print(f'R2(결정계수): {r2_score(y_test, pred):.3f}')
# 회귀이므로 분류 정확도(accuracy_score)가 아닌 MSE, RMSE, R2로 평가한다.
