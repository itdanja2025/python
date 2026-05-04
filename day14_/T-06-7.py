
import matplotlib.pyplot as plt
import pandas as pd
patient_status_data = {
  '상태': ['건강', '경증', '중증', '위중', '퇴원', '집중 치료 필요', '정기 검사 필요', '안정'],
  '환자 수': [300, 250, 100, 50, 200, 150, 180, 220]
}
df_patient_status = pd.DataFrame(patient_status_data)

# 파이 차트
plt.pie(df_patient_status['환자 수'], labels=df_patient_status['상태'], autopct='%1.1f%%',
startangle=140)
plt.title('환자 상태 분포')
plt.show()

# 도넛 차트
plt.pie(df_patient_status['환자 수'], labels=df_patient_status['상태'], autopct='%1.1f%%', startangle=140, wedgeprops=dict(width=0.3))
plt.title('환자 상태 분포(도넛 차트)')
plt.show()

# 누적 막대 그래프
plt.bar(df_patient_status['상태'], df_patient_status['환자 수'], color='skyblue')
plt.title('상태별 환자 수 비교')
plt.xlabel('상태')
plt.ylabel('환자 수')
plt.show()