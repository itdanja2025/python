
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
treatment_data = {
  '주차': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
  '평균 건강 점수': [50, 55, 60, 65, 70, 75, 80, 82, 85, 87],
  '치료군 건강 점수': [50, 57, 64, 70, 74, 78, 82, 85, 88, 90],
  '비치료군 건강 점수': [50, 53, 56, 58, 60, 62, 64, 66, 67, 68]
}
df_treatment = pd.DataFrame(treatment_data)

# 기본 선 그래프
plt.plot(df_treatment['주차'], df_treatment['평균 건강 점수'], label='평균 건강 점수', marker='o')
plt.title('치료 기간별 평균 건강 점수 변화')
plt.xlabel('주차')
plt.ylabel('평균 건강 점수')
plt.legend()
plt.show()

# 복수 선 그래프(치료군 vs 비치료군)
plt.plot(df_treatment['주차'], df_treatment['치료군 건강 점수'], label='치료군', marker='o', color='blue')
plt.plot(df_treatment['주차'], df_treatment['비치료군 건강 점수'], label='비치료군', marker='o', color='orange')
plt.title('치료군과 비치료군의 건강 점수 비교')
plt.xlabel('주차')
plt.ylabel('건강 점수')
plt.legend()
plt.show()

# 영역 그래프
plt.fill_between(df_treatment['주차'], df_treatment['치료군 건강 점수'], color="lightblue", alpha=0.4, label='치료군')
plt.fill_between(df_treatment['주차'], df_treatment['비치료군 건강 점수'], color="salmon", alpha=0.4, label='비치료군')
plt.plot(df_treatment['주차'], df_treatment['치료군 건강 점수'], color="blue", label='치료군 건강 점수')
plt.plot(df_treatment['주차'], df_treatment['비치료군 건강 점수'], color="red", label='비치료군 건강 점수')
plt.legend(loc="lower left")
plt.title('치료군과 비치료군의 건강 점수 영역 그래프')
plt.xlabel('주차')
plt.ylabel('건강 점수')
plt.show()
