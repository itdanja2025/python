import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
efficiency_data = {
'주차': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
'공정 A 효율(%)': [80, 82, 81, 79, 85, 88, 86, 87, 89, 90],
'공정 B 효율(%)': [75, 77, 78, 76, 79, 81, 83, 84, 85, 86],
'공정 C 효율(%)': [70, 73, 72, 71, 74, 76, 75, 77, 78, 80]
}
df_efficiency = pd.DataFrame(efficiency_data)

# 기본 선 그래프
plt.plot(df_efficiency['주차'], df_efficiency['공정 A 효율(%)'], label='공정 A', marker='o')
plt.plot(df_efficiency['주차'], df_efficiency['공정 B 효율(%)'], label='공정 B', marker='o')
plt.plot(df_efficiency['주차'], df_efficiency['공정 C 효율(%)'], label='공정 C', marker='o')
plt.title('주차별 공정 효율 추세')
plt.xlabel('주차')
plt.ylabel('효율(%)')
plt.legend()
plt.show()

# 누적 선 그래프
plt.stackplot(df_efficiency['주차'], df_efficiency['공정 A 효율(%)'], df_efficiency['공정 B 효율(%)'], df_efficiency['공정 C 효율(%)'], labels=['공정 A', '공정 B', '공정 C'], alpha=0.5)
plt.title('누적 공정 효율 추세')
plt.xlabel('주차')
plt.ylabel('누적 효율(%)')
plt.legend(loc='upper left')
plt.show()

# 영역 그래프
plt.fill_between(df_efficiency['주차'], df_efficiency['공정 A 효율(%)'], color="skyblue", alpha=0.4, label='공정 A')
plt.fill_between(df_efficiency['주차'], df_efficiency['공정 B 효율(%)'], color="lightgreen", alpha=0.4, label='공정 B')
plt.fill_between(df_efficiency['주차'], df_efficiency['공정 C 효율(%)'], color="lightcoral", alpha=0.4, label='공정 C')
plt.legend(loc="upper right")
plt.title('공정 효율 영역 그래프')
plt.xlabel('주차')
plt.ylabel('효율(%)')
plt.show()