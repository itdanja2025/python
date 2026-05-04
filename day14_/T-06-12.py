
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# 예시 데이터 생성
np.random.seed(0)
quality_data = {
  '크기(mm)': np.random.normal(loc=50, scale=2, size=100), # 평균 50, 표준편차 2인 크기 데이터
  '무게(g)': np.random.normal(loc=100, scale=5, size=100) # 평균 100, 표준편차 5인 무게 데이터
}
df_quality = pd.DataFrame(quality_data)

# 기본 히스토그램(크기 분포)
plt.hist(df_quality['크기(mm)'], bins=5, color='skyblue', edgecolor='black')
plt.title('크기 분포 히스토그램')
plt.xlabel('크기(mm)')
plt.ylabel('빈도')
plt.show()

# 기본 히스토그램(무게 분포)
plt.hist(df_quality['무게(g)'], bins=5, color='lightgreen', edgecolor='black')
plt.title('무게 분포 히스토그램')
plt.xlabel('무게(g)')
plt.ylabel('빈도')
plt.show()

# 히스토그램과 밀도 그래프(크기)
sns.histplot(df_quality['크기(mm)'], kde=True, color='skyblue')
plt.title('크기 분포와 밀도 그래프')
plt.xlabel('크기(mm)')
plt.ylabel('밀도')
plt.show()

# 박스 플롯과 히스토그램 결합
fig, ax = plt.subplots(1, 2, figsize=(12, 6))
ax[0].boxplot(df_quality['크기(mm)'])
ax[0].set_title('박스 플롯')
ax[0].set_ylabel('크기(mm)')
ax[1].hist(df_quality['크기(mm)'], bins=5, color='skyblue', edgecolor='black')
ax[1].set_title('크기 분포 히스토그램')
plt.show()
