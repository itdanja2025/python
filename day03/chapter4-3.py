
# 범위 : range 
# [1] 숫자 1개만 넣는 경우 , 0부터 n-1 까지 리스트로 반환 
print( list( range(5) ) )               # [0, 1, 2, 3, 4]

# [2] 숫자 2개 넣는 경우 ,  s 부터 n-1 까지 리스트로 반환 
print( list( range( 0 , 5 ) ) )         # [0, 1, 2, 3, 4]

# [3] 숫자 3개 넣는 경우 ,   s 부터 n-1 까지 t만큼 증가 하면서 리스트 반환 
print( list( range( 0 , 10 , 2 ) ) )    # [0, 2, 4, 6, 8]

# 반복문 과 범위 활용 
# for 반복변수 in range( ) :
#   실행코드

# 예시1] 1부터 10 까지 출력 
for i in range( 1 , 11 ) : 
    print( i )

# 예시2] 1부터 10 까지 홀수만 출력 
for i in range( 1 , 11 , 2 ) :
    print( i )

# 예시3] 리스트와 범위 조합 
array = [ 273, 32, 103, 57, 52 ]
for index in range( len(array) ) : # 0부터 리스트의마지막인덱스까지
    print( array[index] )

# 예시4] 역순 
for i in range( 4 , -1 , -1 ) :    # 4부터 0 까지 1씩 감소 
    print( i )

for i in reversed( range(5) ) :     # reversed( 리스트 ) , 리스트 역순으로 이터레이터 제공 
    print( i )

# 예시5] 구구단 
for 단 in range( 1 , 10 ) : 
    for 곱 in range( 1 , 10 ) :
        print( 단 * 곱 )


# while 반복문 

# 무한반복 
# while True : # 조건식에 True 일때 무한반복 
#     print( "." , end = "") # print( 출력할자료 , end ="" ) 줄바꿈처리 하지 않는다.

# 1부터 10까지 출력 
i = 1               # 반복변수 초기값 
while i < 11 :      # 반복 조건 
    print( i )      
    i += 1          # 반복변수 증감식 

# 리스트 활용
list_a = [ 1 , 2 , 1 , 2 ]
while 2 in list_a : # 만약에 리스트에 2가 포함되면 
    list_a.remove( 2 )

print( list_a ) # [1 , 1 ]

# break 키워드 
i = 0                               # 초기값 : 0부터 
while True :                        # 무한반복조건 
    print( i )
    i += 1                          # 증감식 
    msg = input(" 종료할까요? > ")    # 입력받기 
    if msg in ['Y', 'y'] :          # 입력받은 값이 Y/y 이면 
        break                       # 가장 가까운 반복문 탈출 

# continue 키워드
numbers = [ 5, 15, 6, 20, 7, 25 ]
for number in numbers :             # 반복문 
    if number < 10 :                # 조건문 
        continue                    # 반복변수가 10보다 작으면 다음으로 이동 
    print( number )










