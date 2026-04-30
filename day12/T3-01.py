# numpy : 배열 기반( 위치(인덱스) ) , 공학 수치 계산
# pandas : 테이블 기반( 라벨(인덱스) ) , 전처리/필터링(+numpy)
    # 1차원 : series        # 2차원 : dataframe

# [1] pandas 설치 : pip install pandas
# [2] import pandas as pd

import pandas as pd
print( pd.__version__ ) # 3.0.2

# series 
# 1. 생성 
x = [ 10 , 20 , 30 , 40 ]  # 리스트 
z = pd.Series( x )
print( z ) 
# 0    10           # 0 ~ 4 : 각 요소들의 인덱스
# 1    20           # 10~50 : 각 요소의 값 
# 2    30
# ~~~~~
# dtype: int64      # 데이터의 타입 

# 2. 각 요소들의 라벨 포함하기 
y = [ 'a' , 'b' , 'c' , 'd' ]
z = pd.Series( x , index=y )    # index에 라벨(목록) 대입 
print( z )
# a    10           # a ~ d : 각 요소들의 인덱스(라벨)
# b    20          
# c    30
# dtype: int64

# 3. 딕셔너리 으로 생성 
# 파이썬 주요 타입 , [리스트] (튜플) {딕셔너리}
x = { 'apple' : 1 , 'banana' : 2 , 'cherry' : 3 }
z = pd.Series( x )
print( z )

# 4. 주요 속성 확인 
print( z.dtype )        # 타입반환 , int64
print( z.index )        # 인덱스반환, Index(['apple', 'banana', 'cherry'], dtype='str')
print( z.values )       # 값반환 , [1 2 3]
print( z.head(2) )      # .head(n) , 상위 n개(기본값:5) 개만 출력( 확인용 )
print( z.tail(2) )      # .tail(n) , 하위 n개 만 출력 
print( z.iloc[0] )      # iloc[인덱스번호] , 라벨이 아닌 위치로 조회
