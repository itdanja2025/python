import pandas as pd

# ==========================================
# 문제 1: 데이터프레임 생성과 정보 확인
# ==========================================
print("--- 문제 1 ---")
x = [['iPhone', 120, 'Apple'], ['Galaxy', 110, 'Samsung'], ['Pixel', 90, 'Google']]

# 1. 2차원 리스트 x와 columns 파라미터를 사용하여 DataFrame 생성
df1 = pd.DataFrame(x, columns=['Model', 'Price', 'Company'])

# 2. 데이터프레임의 전체적인 요약 정보 출력 (인덱스, 컬럼명, 결측치, 데이터 타입 등)
# 주의: info() 메서드는 기본적으로 콘솔에 직접 출력하므로 print()로 감쌀 필요가 없습니다.
df1.info() 
print("\n")


# ==========================================
# 문제 2: iloc와 loc를 이용한 데이터 추출
# ==========================================
print("--- 문제 2 ---")
data2 = pd.DataFrame({
    'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
    'Age': [24, 27, 22, 32],
    'City': ['Seoul', 'Busan', 'Incheon', 'Daejeon']
}, index=['A', 'B', 'C', 'D'])

# 1. loc 사용: 'Bee'(인덱스 'B')와 'Cat'(인덱스 'C')의 'Name'과 'Age' 정보 추출
# loc는 [행 이름(인덱스명), 열 이름(컬럼명)] 형태로 접근합니다.
loc_result = data2.loc[['B', 'C'], ['Name', 'Age']]
print("[loc 추출 결과]\n", loc_result)

# 2. iloc 사용: 2행 3열(City 정보) 추출
# iloc는 0부터 시작하는 정수 인덱스만 사용합니다. 
# 2행은 인덱스 1, 3열은 인덱스 2에 해당합니다. (Bee의 City인 'Busan' 추출)
iloc_result = data2.iloc[1, 2]
print("\n[iloc 추출 결과]\n", iloc_result)
print("\n")


# ==========================================
# 문제 3: 컬럼 추가와 조건부 값 수정
# ==========================================
print("--- 문제 3 ---")
data3 = pd.DataFrame({'Name': ['Ant', 'Bee', 'Cat'], 'Age': [24, 27, 22]})

# 1. 'Score' 컬럼 추가
data3['Score'] = [85, 90, 95]

# 2. 'Score'가 90점 이상인 데이터의 'Name'을 'MVP'로 변경
# 조건(data3['Score'] >= 90)을 만족하는 행의 'Name' 컬럼을 지정하여 값을 수정합니다.
data3.loc[data3['Score'] >= 90, 'Name'] = 'MVP'
print(data3)
print("\n")


# ==========================================
# 문제 4: 다중 조건을 활용한 행 필터링
# ==========================================
print("--- 문제 4 ---")
data4 = pd.DataFrame({
    'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
    'Age': [24, 27, 22, 32],
    'Score': [85, 90, 88, 76]
})

# 'Age'가 25 이상이면서(&) 'Score'가 80 이상인 조건
# 주의: 다중 조건 시 각 조건은 반드시 괄호()로 묶어주어야 합니다.
filtered_data = data4[(data4['Age'] >= 25) & (data4['Score'] >= 80)]
print(filtered_data)
print("\n")


# ==========================================
# 문제 5: 데이터 병합 (Merge)
# ==========================================
print("--- 문제 5 ---")
df1_merge = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})
df2_merge = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})

# 1. inner 방식: 두 데이터에 모두 존재하는 ID(2, 3)만 남김 (교집합)
inner_merged = pd.merge(df1_merge, df2_merge, on='ID', how='inner')
print("[Inner Merge]\n", inner_merged)

# 2. left 방식: 기준이 되는 왼쪽 데이터(df1)의 모든 정보를 유지 (ID 1, 2, 3)
# df2에 없는 ID 1의 Score는 NaN(결측치)으로 처리됩니다.
left_merged = pd.merge(df1_merge, df2_merge, on='ID', how='left')
print("\n[Left Merge]\n", left_merged)
print("\n")


# ==========================================
# 문제 6: 데이터 연결 (Concat)
# ==========================================
print("--- 문제 6 ---")
df1_concat = pd.DataFrame({'Name': ['Ant', 'Bee'], 'Score': [90, 80]})
df2_concat = pd.DataFrame({'Name': ['Cat', 'Dog'], 'Score': [85, 75]})

# 위아래(행 방향, axis=0 기본값)로 연결하며, 
# ignore_index=True를 설정하여 기존 인덱스를 버리고 0부터 다시 번호를 매깁니다.
concat_result = pd.concat([df1_concat, df2_concat], ignore_index=True)
print(concat_result)
print("\n")


# ==========================================
# 문제 7: 다중 기준 정렬
# ==========================================
print("--- 문제 7 ---")
data7 = pd.DataFrame({
    'Name': ['Ant', 'Bee', 'Cat', 'Dog'],
    'Age': [27, 27, 22, 32],
    'Score': [88, 95, 85, 90]
})

# by 파라미터에 정렬 기준 컬럼을 리스트로 전달합니다.
# ascending 파라미터에 각 컬럼별 오름차순(True)/내림차순(False) 여부를 매핑합니다.
sorted_data = data7.sort_values(by=['Age', 'Score'], ascending=[True, False])
print(sorted_data)
print("\n")


# ==========================================
# 문제 8: 그룹화 및 집계 (Groupby)
# ==========================================
print("--- 문제 8 ---")
data8 = pd.DataFrame({
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Values': [10, 20, 30, 40, 50, 60]
})

# 'Category'별로 그룹화한 뒤, 'Values' 컬럼에 대해 agg() 함수로 다중 집계 함수를 적용합니다.
grouped_data = data8.groupby('Category')['Values'].agg(['sum', 'mean', 'count'])
print(grouped_data)
print("\n")


# ==========================================
# 문제 9: 다중 인덱스 그룹화
# ==========================================
print("--- 문제 9 ---")
data9 = pd.DataFrame({
    'Category': ['A', 'A', 'B', 'B'],
    'Type': ['X', 'Y', 'X', 'Y'],
    'Values': [10, 20, 30, 40]
})

# 여러 컬럼으로 그룹화할 때는 리스트 형태로 넘겨줍니다. 
# 결과적으로 Category와 Type이 MultiIndex로 설정됩니다.
multi_grouped = data9.groupby(['Category', 'Type'])['Values'].mean()
print(multi_grouped)
print("\n")


# ==========================================
# 문제 10: 빈도수 분석 및 컬럼명 변경
# ==========================================
print("--- 문제 10 ---")
data10 = pd.DataFrame({
    'Fruit': ['apple', 'banana', 'apple', 'orange'],
    'Color': ['red', 'yellow', 'red', 'orange']
})

# 1. 'Fruit' 열의 고윳값별 빈도수 확인
# value_counts()는 해당 열의 각 고유한 값이 몇 번 등장하는지 내림차순으로 보여줍니다.
fruit_counts = data10['Fruit'].value_counts()
print("[Fruit 빈도수]\n", fruit_counts)

# 2. 모든 컬럼명을 ['Item', 'Style']로 변경
# columns 속성에 새로운 리스트를 할당하여 전체 컬럼명을 직관적으로 변경할 수 있습니다.
data10.columns = ['Item', 'Style']
print("\n[컬럼명 변경 결과]\n", data10)