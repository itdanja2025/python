import pandas as pd  # pandas 라이브러리 불러오기 (데이터 분석 핵심 라이브러리)
import numpy as np

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

# [추가] 데이터 타입 최적화
# 사번은 연산용이 아니므로 문자열로, 부서는 범주형으로 변환하여 메모리 절약
df['사번'] = df['사번'].astype(str)
df['부서'] = df['부서'].astype('category')

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
    {'사번': 25001, '이름': ' 김철수 ', '나이': 20, '부서': '정보보호부', '입사일': '2022-03-02'},
    {'사번': 25001, '이름': ' 김철수 ', '나이': 20, '부서': '정보보호부', '입사일': '2022-03-02'},
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


# [추가] 텍스트 데이터 정제
# 이름의 앞뒤 공백을 제거하고, 부서명칭의 '부'를 '팀'으로 일괄 변경
df['이름'] = df['이름'].str.strip()
df['부서'] = df['부서'].str.replace('부', '팀')


print("변환 전 데이터 타입:")
print(df.dtypes)  
# dtypes: 각 컬럼 데이터 타입 확인

df['입사일'] = pd.to_datetime(df['입사일'])  
# to_datetime(): 문자열 → 날짜 타입 변환

print("\n변환 후 데이터 타입:")
print(df.dtypes)


# [추가] 파생 변수 생성 및 조건부 처리
# 1. 날짜에서 년도 추출
df['입사년도'] = df['입사일'].dt.year

# 2. np.where를 이용한 조건부 분류 (2021년 이전 입사자는 '경력', 아니면 '신입')
df['인력구분'] = np.where(df['입사년도'] <= 2021, '경력', '신입')

# 3. pd.cut을 이용한 수치 데이터 구간 분할 (나이대 그룹화)
bins = [0, 20, 22, 100]
labels = ['청년기', '도약기', '성숙기']
df['연령그룹'] = pd.cut(df['나이'], bins=bins, labels=labels)


# [추가] 이상치(Outlier) 처리
# 나이 데이터가 범위를 벗어날 경우 상/하한선으로 강제 조정 (Capping)
df['나이'] = df['나이'].clip(lower=18, upper=60)


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