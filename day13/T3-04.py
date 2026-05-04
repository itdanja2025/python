# [1] 맷플롭릿 설치 : pip install matplotlib
# [2] 맷플롭릿 불러오기 : import matplotlib
import matplotlib as mpl
print( mpl.__version__ ) # 3.10.9
# [3] 관례적 import 하는 방법 
# import matplotlib as mpl
# import matplotlib.pyplot as plt

# 시각화란? 데이터 분석 결과를 시각적으로 표현하여 인사이트(특징) 도출 

# [*] 차트내 한글 깨짐 방지 코드( +한글폰트 ) , 항상 차트 사용하는 파일 상단에 복붙
import matplotlib as mpl
mpl.rc( 'font' , family='Malgun Gothic' )       # 한글 폰트 설정( 윈도우 기준 설치된 폰트 )
mpl.rcParams['axes.unicode_minus'] = False      # 음수 기호 깨짐 방지

# [1] 선 그래프 , 데이터의 추세(변화) , .plot( )
import matplotlib.pyplot as plt 
# 1.그래프의 데이터 준비 
x = [ 0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ]    # x축( 가로축 의 값 )
y = [ 9, 8, 7, 6, 5, 4, 3, 2, 1, 0 ]    # y축( 세로축 의 값 )
# 2. 그래프 설정 
plt.plot( x , y )                   # .plot( x값 , y값 )
plt.title( 'Line Chart Title')      # .tilte('차트제목')
plt.xlabel( 'X-axis Title' )        # .xlable( 'x축제목' )
plt.ylabel( 'Y축 제목' )             # .ylable( 'y축제목' )
plt.grid(True)                      # .grid(True) , 눈금선 표시 
# 3. 그래프 출력 
plt.show()

# [2] 선 그래프2
y2 = [ 0,1,2,3,4,5,6,7,8,9 ]    
plt.plot( x , y , label ='감소하는 선(항목명)' , color = 'blue'         , linestyle=':' )
plt.plot( x , y2, label ='증가하는 선(항목명)' , color = "#FF0000"    , linestyle='-' )
plt.legend()    # 범례에 항목명 표시
plt.show()

# [3] 막대 그래프 , 데이터의 비교 , .bar( x축값 , y축값 , width = 굵기 , label ='항목명' , color='색상' )
categories = [ '학생1' , '학생2' , '학생3' , '학생4' ]
values =     [   85   ,   92    ,  78    ,   90 ]
values2 =    [   88   ,   91    ,  75    ,   85 ]
# 막대 겹치지 않게 표시 , width='막대굵기' , *인덱스(위치번호) 활용한 크기 조정*
import numpy as np
x = np.arange( len(categories) )    # 0부터 x축의 값 개수 만큼 생성  0 ~ 3 
plt.bar( x - 0.2 , values , width= 0.4  , label='국어성적', color = 'blue')
plt.bar( x + 0.2 , values2 , width= 0.4 , label='수학성적', color = 'orange')
plt.title( '학생 성적 비교' )
plt.xlabel( '학생명')
plt.ylabel( '성적점수')
plt.legend()
plt.grid( axis='y') # 눈금선 (y축만)
plt.xticks( x , categories ) # *위치(0 ~ 3) 순으로 라벨(학생1~학생4) 지정* 
plt.show()

# [4] 파이 그래프 , 백분율 , .pie( 값 , labels = '항목명' , color='색상' , explode ='강조' ,  startangle = 시작각도 , autopct='비율표시')
labels = [ '피자' , '햄버거' , '샐러드' , '파스타' ]
sizes  = [   40  ,   30    ,   20     ,  10    ]
colors = [ 'gold','lightcoral','lightskyblue','lightgreen' ]
explode = [ 0.1 , 0 , 0 , 0]    # 원형에서 튀어나오는 정도(강조)
plt.pie( sizes , labels=labels , colors=colors , explode= explode , startangle= 90 , autopct='%1.0f%%' )
# %형식문자 %자릿수.소수자릿수f , f실수 , %% : 형식문자가 아닌 문자 '%' 표시
plt.title( '음식 선호도' )
plt.legend()
plt.show()

















