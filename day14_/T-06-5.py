import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
risk_return_data = {
  '자산': ['자산 A', '자산 B', '자산 C', '자산 A', '자산 B', '자산 A', '자산 D', '자산 E'],
  '리스크': [0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4],
  '수익률(%)': [4, 6, 8, 7, 10, 12, 9, 14]
}
df_risk_return = pd.DataFrame(risk_return_data)

# 기본 산점도
plt.scatter(df_risk_return['리스크'], df_risk_return['수익률(%)'])
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.title('리스크 대비 수익률 산점도')
plt.show()

# 자산 유형에 따른 색상 구분 산점도
categories = df_risk_return['자산'].unique()
colors = ['red', 'green', 'blue', 'orange', 'cyan', 'skyblue', '#4FDE3E', '#DE83F3']
for i, category in enumerate(categories):
  subset = df_risk_return[df_risk_return['자산'] == category]
  plt.scatter(subset['리스크'], subset['수익률(%)'], color=colors[i], label=category)
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.legend()
plt.title('리스크 대비 수익률(자산별)')
plt.show()

# 버블 차트(마커 크기 조절)
plt.scatter(df_risk_return['리스크'], df_risk_return['수익률(%)'], s=df_risk_return['리스크']*1000, alpha=0.5)
plt.xlabel('리스크')
plt.ylabel('수익률(%)')
plt.title('리스크 대비 수익률 버블 차트')
plt.show()