# 다층 인공신경망(MLP)으로 다항 분리
# 샘플 수: 총 178개 (클래스별 59개, 71개, 48개)
# 특성(Features): 13개 (알코올, 말산, 회분, 알칼리도, 마그네슘, 총 페놀, 플라보노이드 등)
# 타겟(Target): 3가지 와인 등급(클래스 0, 1, 2)


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import koreanize_matplotlib
from sklearn.datasets import load_wine
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

data = load_wine()
x = data.data
y = data.target
print(x[:2], ' ', x.shape) # (178, 13)
print(y[:2], ' ', np.unique(y)) # [0 0]   [0 1 2]

x_train,x_test,y_train,y_test = train_test_split(x, y, test_size=0.2, random_state=0)

# Scaleing (MLP에서 권장)
scaler = StandardScaler()
x_train_scaled = scaler.fit_transform(x_train)
x_test_scaled = scaler.fit_transform(x_test)

# 모델 생성 및 학습
# 1. 모델 생성
model = MLPClassifier(
    hidden_layer_sizes=(20,10), # 은닉층이 2개이고, 첫 번째는 뉴런 20개, 두 번째는 뉴런 10개
    activation='relu',          # 은닉층의 활성화 함수(relu): 음수는 0으로 바꾸고, 양수는 그대로 전달한다.
    solver='adam',              # 손실을 줄이도록 가중치와 편향을 수정하는 최적화 알고리즘이다.
    learning_rate_init=0.001,   # 초기 학습률 : 가중치와 편향의 수정 크기에 영향을 주며, Adam이 실제 수정 크기를 조절한다.
    max_iter=1000,              # Adam 기준으로 전체 학습 데이터를 최대 1000번 반복 학습한다. 종료 조건을 만족하면 일찍 멈출 수 있다.
    random_state=42,            # 가중치 초기화와 데이터 섞기 등에 사용하는 난수 시드로, 같은 조건에서 결과를 재현하기 위한 설정이다.
    verbose=1                   # 학습 중 반복 횟수와 손실(loss)을 출력한다. False로 설정하면 출력하지 않는다.
)
#     입력층         은닉층1        은닉층2         출력층
#      13개     →     20개     →     10개     →     3개
#  와인 특성 13개                                와인 품종 3종

# 2. 모델 학습
model.fit(x_train_scaled, y_train)

# 모델 예측 및 평가
# 1. 모델 예측
pred = model.predict(x_test_scaled) # y_test와 비교하기 위해 테스트 데이터 36개를 예측한다.

# 2. 모델 평가(분류정확도)
print('분류 정확도 평가1(accuacy_score) : ', accuracy_score(y_test, pred))
print('분류 정확도 평가2(confusion_matrix) : ', confusion_matrix(y_test, pred))
print('분류 정확도 평가3(classification report) : ', classification_report(y_test, pred))

# confusion matrix(혼동행렬) 시각화
cm = confusion_matrix(y_test, pred)
plt.figure(figsize=(5, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title('혼동행렬(confusion_matrix)')
plt.xlabel('예측값(predict)')
plt.ylabel('실제값(actual)')
plt.show()