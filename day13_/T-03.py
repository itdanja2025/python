import matplotlib.pyplot as plt  # 그래프를 그리기 위한 pyplot 모듈 불러오기
import seaborn as sns  # seaborn 라이브러리를 sns로 사용 (통계 기반 시각화)
import matplotlib as mpl  # matplotlib 설정 변경을 위한 모듈

mpl.rc('font', family='Malgun Gothic')  # 한글 폰트 설정 (윈도우 기본 폰트)
# rc('font', family=폰트명): 전체 그래프에서 사용할 글꼴 설정

mpl.rcParams['axes.unicode_minus'] = False  # 음수 기호 깨짐 방지 설정
# rcParams['axes.unicode_minus']: False로 설정하면 - 기호 정상 출력


data = [  # 히트맵에 사용할 2차원 리스트 데이터 (행렬 형태)
    [100, 150, 200, 120],  # 첫 번째 행 데이터
    [80, 120, 180, 160],   # 두 번째 행 데이터
    [90, 140, 170, 190],   # 세 번째 행 데이터
    [75, 130, 190, 180],   # 네 번째 행 데이터
    [60, 110, 160, 140]    # 다섯 번째 행 데이터
]

sns.heatmap(data, cmap='Blues', annot=True, fmt='d')  
# heatmap(data, cmap, annot, fmt)
# data: 2차원 데이터 (행렬 형태)
# cmap: 색상 스타일 (Blues → 파란색 계열)
# annot: True → 각 셀에 값 표시
# fmt: 데이터 표시 형식 ('d' → 정수)

plt.title('히트맵')  # 그래프 제목 설정
plt.xlabel('x축')  # x축 이름 설정
plt.ylabel('y축')  # y축 이름 설정

plt.show()  # 그래프 출력


import pandas as pd  # 데이터프레임 사용을 위한 pandas 불러오기

data = {  # 딕셔너리 형태 데이터 생성
    '수익': [1000, 1500, 1300, 1600, 1700],  # 수익 데이터
    '비용': [800, 1200, 1100, 1300, 1250]   # 비용 데이터
}

df_data = pd.DataFrame(data)  # 딕셔너리를 데이터프레임으로 변환
# DataFrame(딕셔너리): 컬럼 형태의 표 데이터 생성

sns.boxplot(data=df_data, fill=False, gap=0.1)  
# boxplot(data, fill, gap)
# data: 데이터프레임
# fill: False → 내부 색 채우지 않음
# gap: 박스 간 간격

plt.title('박스플롯')  # 그래프 제목 설정

plt.show()  # 그래프 출력


data = {  # 지역별 데이터 생성
    '지역': ['서울', '부산', '대구', '인천', '광주', '대전', '울산', '세종', '경기', '강원', '충북', '충남', '전북', '전남', '경북', '경남', '제주'],  # 지역 이름
    '인구 밀도(명/km²)': [17000, 12000, 8000, 10000, 7000, 6500, 7500, 9000, 11000, 500, 1200, 1300, 800, 700, 1100, 1400, 600],  # 인구 밀도
    '평균 연령': [40, 42, 38, 39, 37, 36, 35, 34, 41, 43, 45, 44, 38, 36, 37, 39, 42]  # 평균 연령
}

df_data = pd.DataFrame(data)  # 데이터프레임 생성

numeric_data = df_data.set_index('지역').select_dtypes(include=['number'])  
# set_index('지역'): '지역' 컬럼을 행 인덱스로 설정
# select_dtypes(include=['number']): 숫자형 데이터만 선택

plt.figure(figsize=(10, 8))  
# figure(figsize=(가로, 세로)): 그래프 크기 설정

sns.heatmap(
    numeric_data,  # 히트맵 데이터 (숫자 데이터만)
    cmap='coolwarm',  # 색상 스타일 (빨강-파랑)
    annot=True,  # 값 표시
    fmt='d',  # 정수 형식으로 표시
    linewidths=0.5  # 셀 사이 경계선 두께
)

plt.title('히트맵')  # 그래프 제목

plt.show()  # 그래프 출력


df_data = pd.DataFrame(data)  # 다시 데이터프레임 생성 (동일 데이터 사용)

sns.countplot(data=df_data, x='평균 연령', fill=True)  
# countplot(data, x, fill)
# data: 데이터프레임
# x: 기준이 되는 컬럼 (값의 개수를 셈)
# fill: 막대를 색으로 채움

plt.title('카운트플롯')  # 그래프 제목
plt.xlabel('평균연령')  # x축 이름
plt.ylabel('수량')  # y축 이름 (개수)

plt.show()  # 그래프 출력