
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
defect_data = {
  '공정 단계': ['조립', '검사', '포장', '배송', '완성', '조립', '검사', '포장', '배송', '완성'],
  '결함률(%)': [5, 2, 1, 0.5, 0.8, 4.8, 2.2, 1.1, 0.6, 1.0],
  '제품군': ['A', 'A', 'A', 'A', 'A', 'B', 'B', 'B', 'B', 'B']
}
df_defect = pd.DataFrame(defect_data)

# 기본 막대 그래프
product_a = df_defect[df_defect['제품군'] == 'A']
plt.bar(df_defect['공정 단계'], df_defect['결함률(%)'], color='skyblue')
plt.title('공정 단계별 결함률 (제품군A)')
plt.xlabel('공정 단계')
plt.ylabel('결함률(%)')
plt.show()

# 수평 막대 그래프
plt.barh(product_a['공정 단계'], product_a['결함률(%)'], color='orange')
plt.title('공정 단계별 결함률(수평)')
plt.xlabel('결함률(%)')
plt.ylabel('공정 단계')
plt.show()

# 제품군 별 누적 막대 그래프
product_b = df_defect[df_defect['제품군'] == 'B']
plt.bar(product_a['공정 단계'], product_a['결함률(%)'], label='제품군 A', color='blue')
plt.bar(product_b['공정 단계'], product_b['결함률(%)'], bottom=product_a['결함률(%)'], label='제품군 B', color='green')
plt.title('공정 단계별 결함률(제품군 A vs B)')
plt.xlabel('공정 단계')
plt.ylabel('결함률(%)')
plt.legend()
plt.show()