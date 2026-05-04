
# [1]
import korenfont
import matplotlib.pyplot as plt
import pandas as pd
customer_data = {
  '성별': ['남성', '여성', '남성', '여성', '남성', '여성', '남성', '여성', '남성', '여성'],
  '연령대': ['10대', '10대', '20대', '20대', '30대', '30대', '40대', '40대', '50대', '50대'],
  '지역': ['서울', '서울', '부산', '부산', '대구', '대구', '광주', '광주', '인천', '인천'],
  '고객 수': [300, 250, 400, 350, 500, 450, 200, 300, 150, 200],
  '평균 구매 금액': [30000, 25000, 45000, 40000, 55000, 50000, 60000, 55000, 35000, 30000]
}
df_customer = pd.DataFrame(customer_data)
df_customer = df_customer.groupby(['성별', '연령대']).agg({'고객 수': 'sum', '평균 구매 금액':'mean'}).reset_index()

# 기본 막대 그래프
plt.bar(df_customer['연령대'].unique(), df_customer.groupby(['연령대']).agg({'고객 수':
'sum'})['고객 수'], color='skyblue')
plt.xlabel('연령대')
plt.ylabel('고객 수')
plt.title('연령대별 고객 수')
plt.show()

# 누적 막대 그래프(성별 비교)
male_data = df_customer[df_customer['성별'] == '남성']
female_data = df_customer[df_customer['성별'] == '여성']
plt.bar(male_data['연령대'], male_data['고객 수'], label='남성', color='blue')
plt.bar(female_data['연령대'], female_data['고객 수'], bottom=male_data['고객 수'],
label='여성', color='pink')
plt.xlabel('연령대')
plt.ylabel('고객 수')
plt.legend()
plt.title('성별 및 연령대별 누적 고객 수')
plt.show()

# 수평 막대 그래프
plt.barh(df_customer['연령대'], df_customer['평균 구매 금액'], color='green')
plt.xlabel('평균 구매 금액')
plt.ylabel('연령대')
plt.title('평균 구매 금액')
plt.show()
