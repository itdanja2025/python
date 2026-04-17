
# 딕셔너리 란? 키를 기반으로 값을 저장하는 것 
# vs JS(JSON) vs JAVA(map/dto)

# [1] 선언 , { "키" : 값 , "키" : 값 }
dict_a = { "name" : "어벤저스 엔드게임" , "type" : "히어로 무비" }

# [2] 호출 
print( dict_a )
# print( dict_a.name ) # JS 가능하지만 오류 발생 
print( dict_a["name"] )
print( dict_a.get( "name") ) # JAVA MAP 처럼 호출 가능 
# print( dict_a["origin"] ) # 없는 키 이면 오류 발생 

# [3] 딕셔너리 값 추가 하기  , 딕셔너리명[ 'key' ] = value 
dict_a[ "price" ] = 1000
print( dict_a )  # {'name': '어벤저스 엔드게임', 'type': '히어로 무비', 'price': 1000}

dict_a[ 'price' ] = 2000 # 만약에 존재하면 key 이면 value 수정 # key는 중복없음 
print( dict_a )

# [4] 딕셔너리 키/값 제거하기 , del 딕셔너리명[ 'key' ]
del dict_a[ 'price']
print( dict_a )













