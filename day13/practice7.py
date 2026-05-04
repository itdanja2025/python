import pandas as pd 

# 문제 1: 데이터프레임 생성과 정보 확인
x = [['iPhone', 120, 'Apple'], ['Galaxy', 110, 'Samsung'], ['Pixel', 90, 'Google']]
# pd.DataFrame( 자료 , columns=[ 열이름1 , 열이름2 , 열이름3] )
df = pd.DataFrame( x , columns=[ 'Model', 'Price', 'Company'] )
df.info() # 데이터의 전체적인 요약 정보(인덱스, 컬럼, 데이터 타입 등)를 한 번에 출력하는 메서드를 실행하시오.

# 문제 2: iloc와 loc를 이용한 데이터 추출
data = pd.DataFrame(
    {'Name': ['Ant', 'Bee', 'Cat', 'Dog'],'Age': [24, 27, 22, 32],'City': ['Seoul', 'Busan', 'Incheon', 'Daejeon']}, 
    index=['A', 'B', 'C', 'D'])

result = data.loc[ [ 'B' , 'C' ] , ['Name','Age'] ] # .loc[ [행라벨], [열라벨] ]
result2 = data.iloc[ 1 , 2 ]

# 문제 3: 컬럼 추가와 조건부 값 수정
data = pd.DataFrame({'Name': ['Ant', 'Bee', 'Cat'], 'Age': [24, 27, 22]})

data['Score'] = [85, 90, 95] # 아래 데이터에서 'Score' 컬럼을 [85, 90, 95]로 추가한 뒤, 
data.loc[ data['Score'] >= 90 , 'Name' ] = 'MVP' # x.loc[ 조건식 , 새로운/수정할열 ] = 새로운값

# 문제 4: 다중 조건을 활용한 행 필터링
data = pd.DataFrame({'Name': ['Ant', 'Bee', 'Cat', 'Dog'],'Age': [24, 27, 22, 32],'Score': [85, 90, 88, 76]})

result = data[ (data['Age'] >= 25) & (data['Score'] >=80 ) ]
print( result )

# 문제 5: 데이터 병합 (Merge)
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df2 = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})
print( pd.merge( df1 , df2 , on='ID', how= 'inner' ) )
print( pd.merge( df1 , df2 , on='ID', how= 'left' ) )

# 문제 6: 데이터 연결 (Concat)
df1 = pd.DataFrame({'Name': ['Ant', 'Bee'], 'Score': [90, 80]})
df2 = pd.DataFrame({'Name': ['Cat', 'Dog'], 'Score': [85, 75]})
print(  pd.concat( [ df1 , df2 ] , axis= 0 , ignore_index=True ) )

# 문제 7: 다중 기준 정렬
data = pd.DataFrame({'Name': ['Ant', 'Bee', 'Cat', 'Dog'],'Age': [27, 27, 22, 32],'Score': [88, 95, 85, 90] })
print( data.sort_values( by=[ 'Age' , 'Score'] , ascending=[ True , False ] ) )

# 문제 8: 그룹화 및 집계 (Groupby)
data = pd.DataFrame({ 'Category': ['A', 'B', 'A', 'B', 'A', 'B'], 'Values': [10, 20, 30, 40, 50, 60] })
print( data.groupby( 'Category' )['Values'].agg( [ 'sum' , 'mean' , 'count' ] ) )

# 문제 9: 다중 인덱스 그룹화
data = pd.DataFrame({'Category': ['A', 'A', 'B', 'B'],'Type': ['X', 'Y', 'X', 'Y'],'Values': [10, 20, 30, 40] })
print( data.groupby( ['Category' , 'Type'] )['Values'].mean() )

# 문제 10: 빈도수 분석 및 컬럼명 변경
data = pd.DataFrame({
 'Fruit': ['apple', 'banana', 'apple', 'orange'],
 'Color': ['red', 'yellow', 'red', 'orange']
})
print( data['Fruit'].value_counts() )   # 고윳값(중복수) 별 빈도수
data.columns = [ 'Item' , 'Style']   # data.columns 모든열 , data.index 모든행 # 전체수정 가능 # 원본수정O
print( data )
result = data.rename( columns={ 'Fruit' : 'Item' , 'Color' : 'Style' }  ) # 원본수정X 
print( result )