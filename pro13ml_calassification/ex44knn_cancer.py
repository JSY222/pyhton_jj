# Breast_cancer_dataset으로 KNN을 학습해보자
# breat_cancer_dataset
# x : 세포의 측정값 : 30개
# y : 악성(0), 양성(1)
# 그리고 569개의 sample이 존재

# [1단계] : 데이터 불러오기 및 변수설정
# 1. Lib불러오기
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_breast_cancer # 유방암 데이터셋 불러오기
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler, MinMaxScaler # KNN의 표준화와 정규화가 필수이다!!
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# 2. 변수 설정 
data = load_breast_cancer()
x = data.data    # feature(독립변수)
y = data.target  # label(종속변수)
print(x[:2], ' ', x.shape)
# x[:2] : 첫 번째와 두 번째 샘플의 측정값을 출력한다. 각 행은 샘플 1개, 각 열은 특성 1개이다.
# x.shape = (569, 30) : 전체 샘플이 569개이고, 샘플마다 세포핵의 측정 특성이 30개 있다는 뜻이다.
print(y[:2], ' ', np.unique(y))
# y[:2] = [0 0] : 첫 번째와 두 번째 샘플의 정답이 모두 0(악성)이라는 뜻이다. x[:2]의 각 행과 순서대로 대응한다.
# np.unique(y) = [0 1] : 전체 정답에서 중복을 제거한 클래스 목록이다. 0은 악성, 1은 양성이며 개수나 확률이 아니다.

# 3. 과적합 방지 : train/test split
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42, stratify=y)

# 4. 스케일링 필요(이유 : KNN은 거리기반 모델이기 때문에 크기가 영향을 미치기 때문에 스케일링(정규화/표준화)가 필요하다)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

# K-NN모델에서는 k값이 중요하다. k값이 작으면 과적합, k값이 크면 과소적합이 발생한다.
# 그래서 최적의 k값을 확인하는 것이 중요하다.
train_acc = []
test_acc = []
k_range = range(3, 12, 2)


for k in k_range:
    # [2단계] : 모델 생성 및 학습
    # 1. 모델 생성
    model = KNeighborsClassifier(n_neighbors=k)
    # 2. 모델 학습
    model.fit(x_train_scaled, y_train)

    # [3단계] : 예측 및 평가
    # 1.예측(x_train, x_test)
    y_train_pred = model.predict(x_train_scaled)
    y_test_pred = model.predict(x_test_scaled)
    # 2. 분류 정확도 평가
    train_acc.append(accuracy_score(y_train, y_train_pred))
    test_acc.append(accuracy_score(y_test, y_test_pred))

print(train_acc)
print(test_acc)

# test data의 정확도를 비교해서 k값을 선택함(좀 더 바람직한 방법은 GridSearchbCV추천)
best_idx = np.argmax(test_acc)
best_k = list(k_range)[best_idx]
best_acc = test_acc[best_idx]
print('최적의 k값 : ', best_k)
print('최고 정확도 : ', best_acc)

# 시각화 
plt.figure()
plt.plot(k_range, train_acc, marker='o', c='b', label='train acc')
plt.plot(k_range, test_acc, marker='s', c='r', label='test acc')
plt.xlabel('k value')
plt.ylabel('accuracy')
plt.legend()
plt.grid()
plt.show()
# 그래프르 보면 3,4의 k value를 주면 정확도가 너무 크다. 하지만 kvalue를 5나 9가 되면 정확도가 안정이 된다.
# best_k 값으로 모델 생성 후 예측 ... 생략