
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
population_data = {
  '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
  '인구 밀도(명/km²)': [17000, 12000, 8000, 10000, 7000, 6500, 7500, 9000, 11000, 500, 1200, 1300, 800, 700, 1100, 1400, 600],
  '평균 연령': [40, 42, 38, 39, 37, 36, 35, 34, 41, 43, 45, 44, 38, 36, 37, 39, 42]
}
df_population = pd.DataFrame(population_data)

# 기본 히트맵
plt.figure(figsize=(10, 6))
sns.heatmap(
  df_population.set_index('지역').T,
  annot=True,
  fmt='d', # 정수형 포맷 지정
  cmap='YlOrRd',
  cbar_kws={'label': '값'}
)
plt.title('지역별 인구 밀도 히트맵')
plt.show()

# 클러스터 히트맵(2개 이상의 숫자형 열 필요)
numeric_data = df_population.set_index('지역').select_dtypes(include=['number'])
sns.clustermap(
  numeric_data,
  cmap='coolwarm',
  annot=True,
  fmt='d' # 정수형 포맷 지정
)
plt.title('인구 밀도 및 평균 연령 클러스터링 히트맵')
plt.show()