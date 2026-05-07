# day15/T5-05.py
import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import koreanfont                   # 한글폰트
import json                         # JSON LOAD

# [1] T5_data.json 파일내 'financial_performance_data'
with open( './T5_data.json' , 'r' , encoding='utf-8') as json_file : 
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['financial_performance_data'])
print( df )

# [2] 플롯박스 : '수익' '비용' '이익' 으로 박스플롯 표시 
# plt.boxplot( ) : 데이터최솟값, 최댓값 , 1사분위 , 중앙값 3사분위 시각화 
plt.boxplot( [ df['수익'] , df['비용'] , df['이익'] ] , tick_labels=['수익' , '비용','이익'] )
plt.ylabel('금액')
plt.title('항목별 금액 분포')
plt.show()

# 차트확인 : 비용 데이터에서 800 부근에 이상치가 존재한다.

# [3] 플롯박스 : 분기별 수익 데이터 로 박스플롯 표시
# 플롯박스에서 그룹 , df.boxplot( column=['값'] , by='그룹기준')
df.boxplot( column = ['수익'] , by='분기')
plt.show()

# 차트확인 : 2분기가 수익 중앙값이 가장 높고 , 
# 1분기가 박스가 길어서 수익이 불 안정/확실 하다.
# 4분기가 박스가 조밀하게 있어서 수익성이 안정하다. 
