import pandas as pd 
# 서비스 클래스 
class ItemService : 
    # 생성자
    def __init__(self):
        self.df = pd.DataFrame( [
            { 'id' : 1 , 'name' : '콜라' , 'price' : 1000 },
            { 'id' : 2 , 'name' : '사이다' , 'price' : 1500 },
        ] )
    # 함수
    # (1) 개별조회 서비스 
    def item( self , id ) :
        # df[ 조건식 ]   # df[ df['특정열'] == 값 ]
        result = self.df[ self.df['id'] == id ]
        if result.empty : # empty 비어있으면 
            return "해당 상품이 없습니다."
        # df타입 대신에 .to_dict( ) 
        print( result ) # df 조회 결과가 하나라도 항상 *리스트*형식
        return result.to_dict( orient = 'records')[ 0 ]

# ** 서비스 객체 생성 **
item_service = ItemService()