
# day15/T5-04.py
import pandas as pd                 # 데이터표
import matplotlib.pyplot as plt     # 시각화
import koreanfont                   # 한글폰트
import json                         # JSON LOAD

# [1] T5_data.json 파일내 'risk_return_data'
with open( './T5_data.json' , 'r' , encoding='utf-8') as json_file : 
    data_json = json.load( json_file )
df = pd.DataFrame( data_json['risk_return_data'])
print( df )

# [2] 산점도 : 리스크 대비 수익률 , 값에 따른 계산식별로 원형크기 조정 -> 버블차트
# plt.scatter( x축 , y축 , s = 원형크기(계산식) , alpha = 투명도 ) 
plt.scatter( df['리스크'] , df['수익률(%)'] , s = df['수익률(%)']*100 , alpha=0.5 )
plt.xlabel('리스크')
plt.ylabel('수익률' )
plt.title('리스크 대비 수익률')
plt.show()

# [3] 산점도 : 자산별(그룹) 리스크 대비 수익률 
categories = df['자산'].unique()  # 중복제거된 자산 리스트 
# print( categories ) # ['자산 A', '자산 B', '자산 C', '자산 D', '자산 E']
for element in  categories  :       # enumerate( 리스트 ) 반복순회자 으로 인덱스와 요소값 하나씩 반환 
    sub = df[ df['자산'] == element ] # 동일한 자산 정보 가져오기. ( 필터링 )
    plt.scatter( sub['리스크'] , sub['수익률(%)'] , label = element )
plt.legend()
plt.show()













