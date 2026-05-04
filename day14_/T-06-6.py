import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
financial_performance_data = {
  '분기': ['Q1', 'Q2', 'Q3', 'Q4', 'Q1', 'Q2', 'Q3', 'Q4'],
  '수익': [1000, 1500, 1300, 1600, 1700, 1800, 1400, 1550],
  '비용': [800, 1200, 1100, 1300, 1250, 1400, 1350, 1450],
  '이익': [200, 300, 200, 300, 450, 400, 50, 100]
}
df_financial = pd.DataFrame(financial_performance_data)

# 기본 박스 플롯
plt.figure(figsize=(10, 6))
plt.boxplot([df_financial['수익'], df_financial['비용'], df_financial['이익']], tick_labels= ['수익', '비용', '이익'])
plt.title('재무 성과 분포')
plt.ylabel('금액')
plt.show()

# 분기별 박스 플롯
df_financial.boxplot(column=['수익'], by='분기')
plt.title('분기별 수익 분포')
plt.suptitle("") # 중복 제목 제거
plt.ylabel('수익')
plt.show()

# 박스 플롯과 막대 차트 결합
fig, ax = plt.subplots(figsize=(10, 6))
ax.boxplot(df_financial[['수익', '비용', '이익']].values, tick_labels=['수익', '비용', '이익'])
ax.bar(['수익', '비용', '이익'], df_financial[['수익', '비용', '이익']].mean(), color='orange', alpha=0.6, label='평균')
ax.set_ylabel('금액')
plt.legend()
plt.title('재무 성과 분포 및 평균')
plt.show()