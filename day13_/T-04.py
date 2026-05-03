import pandas as pd  # pandas 라이브러리 불러오기 (데이터 분석 핵심 라이브러리)

# CSV 파일 읽기
df_csv = pd.read_csv('./day13_/data.csv')  
# read_csv(파일경로)
# 파일경로: 불러올 CSV 파일 위치

print(df_csv.head())  
# head(): 상위 5개 행 출력 (데이터 구조 확인용)

# 엑셀 파일 읽기 (openpyxl 필요) # pip install openpyxl
df_excel = pd.read_excel('./day13_/data.xlsx', sheet_name='Sheet1')  
# read_excel(파일경로, sheet_name)
# sheet_name: 읽을 시트 이름
print(df_excel.head())  # 상위 5개 행 출력


import json  # JSON 파일 처리를 위한 라이브러리

with open('./day13_/data.json', 'r', encoding='utf-8') as json_file:  
    # open(파일경로, 모드, encoding)
    # 'r': 읽기 모드
    # encoding='utf-8': 한글 깨짐 방지
    data_json = json.load(json_file)  
    # json.load(): JSON 파일을 파이썬 딕셔너리로 변환

df_json = pd.DataFrame(data_json)  
# DataFrame(): 딕셔너리 → 표 형태로 변환

print(df_json.head())  # 상위 데이터 출력

# -------------------- -------------------- #

# 일부 값이 없는 데이터 생성 (결측값 포함)
data_dict = [
    {'사번': 25001, '나이': 20, '부서': '정보보호부'},
    {'사번': 25002, '이름': '이영희', '부서': '기술부'},
    {'사번': 25003, '이름': '박민수', '나이': 22},
    {'사번': 25004, '이름': '정수진', '나이': 20},
    {'사번': 25005, '이름': '한미래', '나이': 23, '부서': '개발부'},
]

df = pd.DataFrame(data_dict)  # 데이터프레임 생성
print(df)  # 전체 데이터 출력

print("각 열의 결측값 개수:")
print(df.isnull().sum())  
# isnull(): 결측값(True/False)
# sum(): True 개수 합 → 결측값 개수

print("각 열의 결측값 비율:")
print(df.isnull().mean() * 100)  
# mean(): 결측 비율 계산 (평균 → 비율)
# *100 → 퍼센트 변환


# 결측값이 있는 행 제거
df_dropped_rows = df.dropna()  
# dropna(): NaN 포함 행 제거

print("결측값 포함 행 제거 후:")
print(df_dropped_rows)

# 결측값이 있는 열 제거
df_dropped_cols = df.dropna(axis=1)  
# axis=1 → 열 기준 삭제

print("\n결측값 포함 열 제거 후:")
print(df_dropped_cols)


# 결측값 채우기 (평균)
df = df.fillna({'나이': df['나이'].mean()})  
# fillna({컬럼: 값})
# mean(): 평균값

print(df)

# 결측값 채우기 (중앙값)
df = df.fillna({'나이': df['나이'].median()})  
# median(): 중앙값

print(df)

# 결측값 채우기 (최빈값)
df = df.fillna({'부서': df['부서'].mode()[0]})  
# mode()[0]: 가장 많이 등장한 값

print(df)


# -------------------- 중복 데이터 처리 -------------------- #

data_dict = [
    {'사번': 25001, '이름': '김철수', '나이': 20, '부서': '정보보호부', '입사일': '2022-03-02'},
    {'사번': 25001, '이름': '김철수', '나이': 20, '부서': '정보보호부', '입사일': '2022-03-02'},
    {'사번': 25002, '이름': '이영희', '나이': 21, '부서': '기술부', '입사일': '2021-03-02'},
    {'사번': 25003, '이름': '박민수', '나이': 22, '부서': '생산부', '입사일': '2020-03-02'},
    {'사번': 25004, '이름': '정수진', '나이': 20, '부서': '전략본부', '입사일': '2022-03-02'},
    {'사번': 25005, '이름': '한미래', '나이': 23, '부서': '개발부', '입사일': '2019-03-02'},
    {'사번': 25005, '이름': '한미래', '나이': 23, '부서': '개발부', '입사일': '2019-03-02'},
]

df = pd.DataFrame(data_dict)  # 데이터프레임 생성

print("중복 제거 전:")
print(df)

df = df.drop_duplicates()  
# drop_duplicates(): 동일한 행 제거

print("\n중복 제거 후:")
print(df)


print("변환 전 데이터 타입:")
print(df.dtypes)  
# dtypes: 각 컬럼 데이터 타입 확인

df['입사일'] = pd.to_datetime(df['입사일'])  
# to_datetime(): 문자열 → 날짜 타입 변환

print("\n변환 후 데이터 타입:")
print(df.dtypes)


# 범주형 데이터 인코딩 (원-핫 인코딩)
df_encoded = pd.get_dummies(df, columns=['부서'])  
# get_dummies(df, columns)
# columns: 변환할 범주형 컬럼

print("인코딩 결과:")
print(df_encoded.head())


# 정규화 (Min-Max Scaling)
df['나이_정규화'] = (df['나이'] - df['나이'].min()) / (df['나이'].max() - df['나이'].min())  
# (값 - 최소값) / (최대값 - 최소값)

# 표준화 (Z-score)
df['나이_표준화'] = (df['나이'] - df['나이'].mean()) / df['나이'].std()  
# (값 - 평균) / 표준편차

print("정규화 및 표준화 결과:")
print(df)

print("\n정규화 통계:")
print(df['나이_정규화'].describe())  
# describe(): 요약 통계

print("\n표준화 통계:")
print(df['나이_표준화'].describe())


# -------------------- 데이터 조회 -------------------- #

print("원본 데이터:")
print(df)

print("\n이름 컬럼:")
print(df['이름'])  
# df['컬럼명']: 특정 열 선택

print("\n3번째 행:")
print(df.loc[2])  
# loc[인덱스]: 행 선택

print("\n나이 21 이상:")
print(df[df['나이'] >= 21])  
# 조건 필터링

print("\n나이 21 이상 AND 정보보호부:")
print(df[(df['나이'] >= 21) & (df['부서'] == '정보보호부')])  
# & : AND 조건


print("\n처음 두 열:")
print(df.iloc[:, 0:2])  
# iloc[행, 열] → 위치 기반 선택

print("\n2~4번째 행:")
print(df.iloc[1:4])  

print("\n2~4행 + 앞 2열:")
print(df.iloc[1:4, 0:2])  

print("\n사번 + 부서:")
print(df[['사번', '부서']])  
# 여러 컬럼 선택


# -------------------- 정렬 -------------------- #

print("\n나이 오름차순:")
print(df.sort_values('나이'))  

print("\n나이 내림차순:")
print(df.sort_values('나이', ascending=False))  

print("\n나이 내림차순 + 부서 오름차순:")
print(df.sort_values(['나이', '부서'], ascending=[False, True]))  

print("\n이름 오름차순:")
print(df.sort_values('이름'))  


# -------------------- 파일 저장 -------------------- #

df.to_csv('./day13_/data_out.csv', index=False, encoding='utf-8-sig')  
# to_csv(파일명, index, encoding)
# index=False → 인덱스 저장 안함

df.to_excel('./day13_/data_out.xlsx', index=False)  
# to_excel(파일명)

df.to_json('./day13_/data_out.json', orient='records', force_ascii=False, date_format='iso')  
# to_json(파일명, orient, force_ascii, date_format)
# orient='records' → 리스트 형태 저장
# force_ascii=False → 한글 유지
# date_format='iso' → 날짜 ISO 형식 저장