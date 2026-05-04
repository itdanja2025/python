
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
stock_data = {
  '기간': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  '주가': [100, 105, 110, 108, 115, 120, 118, 123, 130, 125, 128, 135],
  '거래량': [1000, 1200, 1500, 1300, 1600, 1800, 1700, 1900, 2100, 2000, 1950, 2200],
  '평균 이동선(3개월)': [None, None, 105, 107.67, 111, 114.33, 117.67, 120.33, 123.67, 126.0, 127.67, 129.67]
}
df_stock = pd.DataFrame(stock_data)

# 시각화
fig, ax1 = plt.subplots(figsize=(10, 6))

# 주가 변동 선 그래프
ax1.plot(df_stock['기간'], df_stock['주가'], label='주가', marker='o', color='blue')
ax1.set_xlabel('기간')
ax1.set_ylabel('주가', color='blue')

# 3개월 이동 평균선 추가
ax1.plot(df_stock['기간'], df_stock['평균 이동선(3개월)'], label='3개월 이동 평균', linestyle='--', color='orange')

# 거래량을 표시하는 이중 축 설정
ax2 = ax1.twinx()
ax2.bar(df_stock['기간'], df_stock['거래량'], color='gray', alpha=0.3, label='거래량')
ax2.set_ylabel('거래량', color='gray')

# 범례 및 제목 추가
fig.suptitle('기간별 주가 및 거래량 추세')
ax1.legend(loc='upper left')
plt.show()
