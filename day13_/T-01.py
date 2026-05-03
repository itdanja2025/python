import pandas as pd  # pandas 라이브러리를 pd라는 이름으로 사용하겠다는 의미

# 데이터 병합(Merge)에 사용할 첫 번째 데이터프레임 생성 (ID와 Name 컬럼)
df_info = pd.DataFrame({'ID': [1, 2, 3], 'Name': ['Ant', 'Bee', 'Cat']})  # ID와 이름 정보

# 데이터 병합(Merge)에 사용할 두 번째 데이터프레임 생성 (ID와 Score 컬럼)
df_score = pd.DataFrame({'ID': [2, 3, 4], 'Score': [88, 92, 85]})  # ID와 점수 정보

# pd.merge() 함수 설명:
# pd.merge(left, right, on, how)
# left: 왼쪽 데이터프레임
# right: 오른쪽 데이터프레임
# on: 기준이 되는 공통 컬럼 이름
# how: 병합 방식 ('inner', 'left', 'right', 'outer')

# inner 병합: 두 데이터프레임에 모두 존재하는 ID만 결합 (교집합)
inner_merge = pd.merge(df_info, df_score, on='ID', how='inner')  # ID가 2,3인 데이터만 남음

# inner 병합 결과 출력
print("\n--- Inner Merge 결과 ---")  # 출력 구분용 텍스트
print(inner_merge)  # 병합된 데이터 출력

# left 병합: 왼쪽(df_info) 기준으로 모든 데이터 유지, 없는 값은 NaN 처리
left_merge = pd.merge(df_info, df_score, on='ID', how='left')  # ID=1은 Score 없음 → NaN

# left 병합 결과 출력
print("\n--- Left Merge 결과 ---")  # 출력 구분용 텍스트
print(left_merge)  # 병합된 데이터 출력


# 데이터 연결(Concat)에 사용할 첫 번째 데이터프레임 생성
df1 = pd.DataFrame({'ID': [1, 2, 3], 'Score': [90, 80, 85]})  # 첫 번째 데이터

# 데이터 연결(Concat)에 사용할 두 번째 데이터프레임 생성
df2 = pd.DataFrame({'ID': [4, 5, 6], 'Score': [75, 95, 88]})  # 두 번째 데이터

# pd.concat() 함수 설명:
# pd.concat(objs, axis, ignore_index)
# objs: 연결할 데이터프레임 리스트
# axis: 0이면 행 방향(세로), 1이면 열 방향(가로)
# ignore_index: True이면 인덱스를 0부터 새로 생성

# 세로 연결: 행(row)을 아래로 이어붙임
df_vertical = pd.concat([df1, df2], axis=0, ignore_index=True)  # 인덱스를 0부터 다시 생성

# 세로 연결 결과 출력
print("--- 세로 연결 결과 ---")  # 출력 구분용 텍스트
print(df_vertical)  # 연결된 데이터 출력

# 가로 연결: 열(column)을 옆으로 붙임
df_horizontal = pd.concat([df1, df2], axis=1)  # 인덱스 기준으로 옆에 붙음

# 가로 연결 결과 출력
print("\n--- 가로 연결 결과 ---")  # 출력 구분용 텍스트
print(df_horizontal)  # 연결된 데이터 출력


# 기본 데이터프레임 생성 (이름과 나이)
df_base = pd.DataFrame({  # 데이터프레임 생성 시작
    'Name': ['Ant', 'Bee', 'Cat'],  # 이름 컬럼
    'Age': [24, 27, 22]  # 나이 컬럼
})  # 데이터프레임 생성 끝

# pd.Series() 함수 설명:
# pd.Series(data, name)
# data: 값 리스트
# name: 컬럼 이름처럼 사용됨

# 새로운 점수 데이터를 Series로 생성
new_score = pd.Series([85, 90, 88], name='Score')  # Score라는 이름의 열 생성

# 기존 데이터프레임에 새로운 열 추가
df_base['Score'] = new_score  # 인덱스를 기준으로 값이 들어감

# Series 추가 결과 출력
print("\n--- Series로 열 추가 결과 ---")  # 출력 구분용 텍스트
print(df_base)  # 결과 출력


# 정렬에 사용할 데이터프레임 생성
df = pd.DataFrame({  # 데이터프레임 생성 시작
    'Name': ['Ant', 'Bee', 'Cat', 'Dog'],  # 이름 컬럼
    'Age': [27, 27, 22, 32],  # 나이 컬럼
    'Score': [88, 95, 85, 90]  # 점수 컬럼
})  # 데이터프레임 생성 끝

# sort_values() 함수 설명:
# df.sort_values(by, ascending)
# by: 기준이 되는 컬럼명 (문자열 또는 리스트)
# ascending: True(오름차순), False(내림차순)

# Score 기준으로 내림차순 정렬
df_score_sorted = df.sort_values(by='Score', ascending=False)  # 점수가 높은 순으로 정렬

# 정렬 결과 출력
print("--- Score 기준 내림차순 정렬 ---")  # 출력 구분용 텍스트
print(df_score_sorted)  # 정렬 결과 출력

# 여러 컬럼 기준 정렬
# Age는 오름차순, Score는 내림차순
df_multi = df.sort_values(by=['Age', 'Score'], ascending=[True, False])  # 복합 정렬

# 다중 정렬 결과 출력
print("\n--- 다중 기준 정렬 결과 ---")  # 출력 구분용 텍스트
print(df_multi)  # 정렬 결과 출력

# sort_index() 함수 설명:
# df.sort_index(axis, ascending)
# axis: 0은 행 인덱스, 1은 열 이름 기준
# ascending: True(오름차순), False(내림차순)

# 행 인덱스 기준 정렬
df_idx = df.sort_index()  # 인덱스 순서대로 정렬

# 열 이름 기준 내림차순 정렬
df_col = df.sort_index(axis=1, ascending=False)  # 열 이름을 역순 정렬

# 열 기준 정렬 결과 출력
print("\n--- 열 이름 기준 정렬 결과 ---")  # 출력 구분용 텍스트
print(df_col)  # 결과 출력


# 그룹화에 사용할 데이터프레임 생성
df = pd.DataFrame({  # 데이터프레임 생성 시작
    'Category': ['A', 'A', 'B', 'B', 'A', 'B'],  # 카테고리 컬럼
    'Type': ['X', 'Y', 'X', 'Y', 'X', 'Y'],  # 타입 컬럼
    'Values': [10, 20, 30, 40, 50, 60]  # 값 컬럼
})  # 데이터프레임 생성 끝

# groupby() 함수 설명:
# df.groupby(by)
# by: 기준이 되는 컬럼 (문자열 또는 리스트)

# 카테고리별 Values 합계 계산
group_sum = df.groupby('Category')['Values'].sum()  # Category로 묶고 Values 합 계산

# 결과 출력
print("--- 카테고리별 합계 ---")  # 출력 구분용 텍스트
print(group_sum)  # 결과 출력

# 카테고리 + 타입 기준 평균 계산
group_mean = df.groupby(['Category', 'Type'])['Values'].mean()  # 두 컬럼으로 그룹화

# 결과 출력
print("\n--- 카테고리 & 타입별 평균 ---")  # 출력 구분용 텍스트
print(group_mean)  # 결과 출력

# agg() 함수 설명:
# 여러 통계 함수를 한 번에 적용 가능
# ['sum', 'mean', 'count'] 처럼 리스트로 전달

# 카테고리별 다양한 통계 계산
group_agg = df.groupby('Category')['Values'].agg(['sum', 'mean', 'count'])  # 여러 통계 적용

# 결과 출력
print("\n--- 카테고리별 종합 통계 ---")  # 출력 구분용 텍스트
print(group_agg)  # 결과 출력