import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
disease_data = {
  '연령대': ['10대', '20대', '30대', '40대', '50대', '60대', '70대'],
  '남성 발생률(%)': [2, 5, 7, 10, 12, 15, 18],
  '여성 발생률(%)': [3, 6, 8, 9, 11, 13, 16],
  '전체 발생률(%)': [2.5, 5.5, 7.5, 9.5, 11.5, 14.0, 17.0]
}
df_disease = pd.DataFrame(disease_data)

# 기본 막대 그래프
plt.bar(df_disease['연령대'], df_disease['남성 발생률(%)'], label='남성 발생률', color='blue', alpha=0.6)
plt.bar(df_disease['연령대'], df_disease['여성 발생률(%)'], label='여성 발생률', color='pink', alpha=0.6)
plt.title('연령대별 성별 질병 발생률 비교')
plt.xlabel('연령대')
plt.ylabel('발병률(%)')
plt.legend()
plt.show()

# 누적 막대 그래프
plt.bar(df_disease['연령대'], df_disease['남성 발생률(%)'], label='남성 발생률', color='blue')
plt.bar(df_disease['연령대'], df_disease['여성 발생률(%)'], bottom=df_disease['남성 발생률(%)'], label='여성 발생률', color='pink')
plt.title('연령대별 성별 질병 발생률(누적 막대 차트)')
plt.xlabel('연령대')
plt.ylabel('발병률(%)')
plt.legend()
plt.show()

# 수평 막대 그래프
plt.barh(df_disease['연령대'], df_disease['전체 발생률(%)'], color='green')
plt.title('연령대별 전체 질병 발생률(수평 막대 그래프)')
plt.xlabel('발병률(%)')
plt.ylabel('연령대')
plt.show()
