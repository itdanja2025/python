
# 3. 라우터 : 앱(서버) 와 연결 되는 라우터
from fastapi import APIRouter
router = APIRouter( prefix="/api")

# 4. 서비스객체 호출
from service import productService 

# 5. HTTP 매핑
@router.get("/products")
async def products( ) :
    return productService.products( )

@router.get("/spring")
async def getSpring( ) :
    return productService.getSpring()
