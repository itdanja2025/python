
import korenfont
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

purchase_data = {
  '시간대': ['오전', '오후', '저녁', '밤'],
  '제품 A': [100, 150, 200, 120],
  '제품 B': [80, 120, 180, 160],
  '제품 C': [90, 140, 170, 190],
  '제품 D': [75, 130, 190, 180],
  '제품 E': [60, 110, 160, 140]
}
df_purchase = pd.DataFrame(purchase_data)

# 기본 히트맵
plt.figure(figsize=(10, 6))
sns.heatmap(df_purchase.set_index('시간대'), annot=True, cmap='YlGnBu')
plt.title('시간대별 제품 구매 빈도 히트맵')
plt.show()

# 클러스터 히트맵
sns.clustermap(df_purchase.set_index('시간대'), annot=True, cmap='coolwarm', metric="euclidean", method="average")
plt.title('구매 패턴 클러스터링 히트맵')
plt.show()

# 라인 그래프
for column in df_purchase.columns[1:]:
  plt.plot(df_purchase['시간대'], df_purchase[column], marker='o', label=column)
plt.xlabel('시간대')
plt.ylabel('구매 빈도')
plt.legend()
plt.title('시간대별 제품 구매 패턴 라인 그래프')
plt.show()
