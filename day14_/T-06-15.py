
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
social_data = {
  '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],
  '실업률(%)': [3.5, 4.2, 4.0, 3.8, 3.7, 3.9, 4.1, 3.6, 3.3, 3.4, 3.5, 3.8, 3.9, 4.0, 3.8, 3.2],
  '범죄율(%)': [1.5, 2.2, 1.8, 1.7, 1.6, 1.9, 1.8, 1.4, 1.1, 1.3, 1.2, 1.5, 1.4, 1.7, 1.5, 1.2],
  '행복 지수': [70, 65, 68, 72, 74, 71, 69, 75, 78, 77, 76, 73, 74, 72, 70, 79]
}
df_social = pd.DataFrame(social_data)

# 기본 막대 그래프(실업률)
plt.bar(df_social['지역'], df_social['실업률(%)'], color='teal')
plt.xlabel('지역')
plt.ylabel('실업률(%)')
plt.title('지역별 실업률 비교')
plt.xticks(rotation=45)
plt.show()

# 누적 막대 그래프(실업률과 범죄율)
plt.bar(df_social['지역'], df_social['실업률(%)'], label='실업률(%)', color='blue')
plt.bar(df_social['지역'], df_social['범죄율(%)'], bottom=df_social['실업률(%)'], label='범죄율(%)', color='red')
plt.xlabel('지역')
plt.ylabel('비율(%)')
plt.title('지역별 실업률과 범죄율 비교')
plt.xticks(rotation=45)
plt.legend()
plt.show()

# 수평 막대 그래프(행복 지수)
df_social.sort_values(by='행복 지수', inplace=True)
plt.barh(df_social['지역'], df_social['행복 지수'], color='purple')
plt.xlabel('행복 지수')
plt.ylabel('지역')
plt.title('지역별 행복 지수 비교')
plt.show()
