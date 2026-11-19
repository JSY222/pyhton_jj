# 타이타닉 생존 여부 분류: ex24tree.py, ex25overfitting.py 참고
from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# 프로젝트에 있는 CSV 사용 (실행 폴더와 관계없이 읽기)
csv_path = Path(__file__).resolve().parents[1] / 'pro10anal1' / 'titanic_data.csv'
data = pd.read_csv(csv_path, usecols=['Survived', 'Pclass', 'Sex', 'Age', 'Fare'])
print(data.head(2), data.shape)  # usecols로 5개 열만 읽으므로 (891, 5)
# 문자열 열에 정수를 대입할 수 있도록 자료형 변경
data['Sex'] = data['Sex'].astype(object)
data.loc[data['Sex'] == 'male', 'Sex'] = 0
data.loc[data['Sex'] == 'female', 'Sex'] = 1
data['Sex'] = data['Sex'].astype(int)

feature = data[['Pclass', 'Sex', 'Fare']]
label = data['Survived']
# Age는 입력변수가 아니므로 Age 결측치 때문에 행을 삭제하지 않는다.

# 1) 학습용 70%, 평가용 30%로 분리
x_train, x_test, y_train, y_test = train_test_split(
    feature, label, test_size=0.3, random_state=12
)
print('학습용/평가용 크기:', x_train.shape, x_test.shape)

# 2) 의사결정나무 분류 모델 생성 및 학습
# random_state는 실행할 때마다 같은 결과를 얻기 위한 설정
model = DecisionTreeClassifier(random_state=12)
model.fit(x_train, y_train)

# 3) 평가용 데이터 예측 및 분류 정확도 출력
pred = model.predict(x_test)
print('예측값:', pred)
print('실제값:', y_test.to_numpy())
print('분류 정확도:', accuracy_score(y_test, pred))
