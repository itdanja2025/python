
# 예외객체 : Exception 클래스
# 1] try ~ except 예외클래스명 as 변수명 ~ except 예외클래스명 as 변수명 
# 2] 모든 예외 잡기 : *마지막에 except 에 Exception 클래스 사용한다.
# 3] 강제 예외 발생 : 1) 미구현 2) 웹/앱 프레임워크(유효성검사/트랜잭션 등)
list_number = [ 52, 273, 32, 72, 100 ]
try : 
    number_input_a = int( input( "정수 입력>") )    # int() 에서 예외발생 경우 
    print( list_number[ number_input_a ] )         # [ ] 에서 예외발생 경우 
    raise NotImplementedError                      #  강제 예외 발생 
    예외.발생해주세요()                               # 예상치 못한 예외는 Exception
except ValueError as e :
    print( "정수만 입력하세요.")
except IndexError as e :
    print( "인덱스를 벗어났어요.!")
except Exception as e :
    print( e ) 
