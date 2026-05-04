import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# 예시 데이터 생성
policy_data = {
  '월': ['1월', '2월', '3월', '4월', '5월', '6월', '7월', '8월', '9월', '10월', '11월', '12월'],
  '범죄율(%)': [5.2, 5.1, 4.9, 4.8, 4.7, 4.6, 4.5, 4.3, 4.1, 4.0, 3.9, 3.8],
  '실업률(%)': [3.5, 3.6, 3.5, 3.4, 3.3, 3.2, 3.1, 3.0, 2.9, 2.8, 2.7, 2.6],
  '정책 효과 지수': [0, 0, 0, 0, 0, 0, 20, 35, 50, 60, 70, 80] # 정책 시행 후 효과 지수
}
df_policy = pd.DataFrame(policy_data)

# 범죄율과 실업률 선 그래프
plt.plot(df_policy['월'], df_policy['범죄율(%)'], label='범죄율(%)', marker='o')
plt.plot(df_policy['월'], df_policy['실업률(%)'], label='실업률(%)', marker='o')
plt.xlabel('월')
plt.ylabel('비율(%)')
plt.title('정책 시행 전후 범죄율과 실업률 변화')
plt.legend()
plt.show()

# 정책 효과 지수 막대 그래프
plt.bar(df_policy['월'], df_policy['정책 효과 지수'], color='orange', alpha=0.6)
plt.xlabel('월')
plt.ylabel('정책 효과 지수')
plt.title('정책 시행 후 효과 지수 변화')
plt.show()

# 이중 축 그래프(범죄율과 실업률)
fig, ax1 = plt.subplots()
ax1.plot(df_policy['월'], df_policy['범죄율(%)'], color='blue', label='범죄율(%)', marker='o')
ax1.set_xlabel('월')
ax1.set_ylabel('범죄율(%)', color='blue')
ax2 = ax1.twinx()
ax2.plot(df_policy['월'], df_policy['실업률(%)'], color='green', label='실업률(%)', marker='o')
ax2.set_ylabel('실업률(%)', color='green')
plt.title('정책 시행 전후 범죄율과 실업률 변화(이중 축)')
fig.tight_layout()
plt.show()