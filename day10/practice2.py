import numpy as np

# 문제 1: 기본 인덱싱 (Indexing)
x = np.array([10, 20, 30, 40, 50])
print( x[3] )
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print( x[ 1 , 2 ] )

# 문제 2: 음수 인덱싱 (Negative Indexing)
x = np.array( [10, 20, 30, 40, 50] ) 
print( x[-1] )
x = np.array( [[1, 2, 3], [4, 5, 6], [7, 8, 9]] )
print( x[ -1 , -1 ] )

# 문제 3: 불리언 & 팬시 인덱싱 (Boolean & Fancy Indexing)
x = np.array([10, 20, 30, 40, 50]) 
y = x > 30      # [False False False  True  True]
print( x[ y ] )   # [40 50]
print( x[ [0 , 2 , 4] ])    # [10 30 50] 

# 문제 4: 1차원 배열 슬라이싱 (Slicing)
x = np.array([10, 20, 30, 40, 50])
print( x[ 1 : 4 ])
print( x[ : 3 ] )
print( x[ : : 2 ])  

# 문제 5: 2차원 배열 슬라이싱
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print( x[ 0:2 , 1:3 ] )

# 문제 6: 축(Axis) 기준 슬라이싱
x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print( x[ : , 1 ] )
print( x[ 1 , :  ])

# 문제 7: 슬라이싱의 참조 특성 (View)
x = np.array([1, 2, 3, 4, 5])
y = x[1:4]
y[0] = 99
print( x )  # y가 x를 참조하므로 y가 변하면 x도 변한다.

# 문제 8: 요소별 사칙연산 (Element-wise Operations)
x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
print( x + y , x - y , x * y , x / y ) # [5 7 9] [-3 -3 -3] [ 4 10 18] [0.25 0.4  0.5 ]

# 문제 9: 브로드캐스팅 및 수학 함수
x = np.array([1, 2, 3])
print( x + 2 , x * 3 )

x = np.array([1, 4, 9])
print( np.sqrt( x ) )

# 문제 10: 논리 및 비교 연산 (Logic & Comparison)
x = np.array([True, False, True])
y = np.array([False, False, True])
print( np.logical_and( x , y) )     # False , Fasle , True  
print( np.logical_or( x , y) )      # True , False , True 

x = np.array( [1, 2, 3] )
y = np.array( [1, 2, 4] )
print( np.array_equal( x , y ) )    # False