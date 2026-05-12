# 1. import 가져오기 
import uvicorn
from fastapi import FastAPI

# 2. fastApi 객체 생성
app = FastAPI()

# 3. 서버 실행 
if __name__ == "__main__" :
    uvicorn.run( "T8-02:app" , host="127.0.0.1" , port = 8000 , reload=True )

# 4. REST 정의하기 
# REST : 자원 주고 받는 상태 구조   # REST API : HTTP 로 REST 구현
# 자동으로 JSON 타입으로 응답한다. vs @ResponseBody(@RestController)
# @app.get( "/URL" ) vs @GetMapping( "/URL")

@app.get( "/" )     # HTTP GET 방식으로 매핑한다 # 주소 정의
async def index() :
    return "안녕 파이썬웹"
