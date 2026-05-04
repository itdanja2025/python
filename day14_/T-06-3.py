import korenfont
import matplotlib.pyplot as plt
import pandas as pd

sales_data = {
  '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  '캠페인 전 매출': [2000, 2200, 2500, 2700, 3000, 3200, 3100, 2900, 2800, 3000, 3200, 3400],
  '캠페인 후 매출': [3000, 3200, 3500, 3700, 4000, 4300, 4200, 4100, 3900, 4100, 4300, 4500],
  '추가 매출 효과': [0, 0, 0, 0, 0, 0, 500, 600, 700, 1100, 1200, 1300] # 캠페인으로 인한 추가 매출
}
df_sales = pd.DataFrame(sales_data)

# 기본 선 그래프: 캠페인 전후 매출 비교
plt.plot(df_sales['월'], df_sales['캠페인 전 매출'], label='캠페인 전 매출', marker='o', color='blue')
plt.plot(df_sales['월'], df_sales['캠페인 후 매출'], label='캠페인 후 매출', marker='o', color='green')
plt.xlabel('월')
plt.ylabel('매출')
plt.title('캠페인 전후 매출 변화')
plt.legend()
plt.show()

# 추가 매출 효과를 막대 그래프로 표시
plt.plot(df_sales['월'], df_sales['캠페인 전 매출'], label='캠페인 전 매출', marker='o', color='blue')
plt.plot(df_sales['월'], df_sales['캠페인 후 매출'], label='캠페인 후 매출', marker='o', color='green')
plt.bar(df_sales['월'], df_sales['추가 매출 효과'], color='orange', alpha=0.5, label='추가 매출 효과')
plt.xlabel('월')
plt.ylabel('매출')
plt.title('캠페인 전후 매출 및 추가 효과')
plt.legend()
plt.show()

# 누적 영역 그래프: 캠페인 후 매출에서의 추가 효과 강조
plt.fill_between(df_sales['월'], df_sales['캠페인 전 매출'], df_sales['캠페인 후 매출'], color="lightcoral", alpha=0.5, label='추가 매출 효과')
plt.plot(df_sales['월'], df_sales['캠페인 전 매출'], color="blue", label='캠페인 전 매출')
plt.plot(df_sales['월'], df_sales['캠페인 후 매출'], color="green", label='캠페인 후 매출')
plt.xlabel('월')
plt.ylabel('매출')
plt.title('캠페인 전후 매출의 누적 변화')
plt.legend()
plt.show()
