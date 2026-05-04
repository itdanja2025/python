import matplotlib.pyplot as plt  # matplotlib의 pyplot 모듈을 plt라는 이름으로 사용 (그래프 그릴 때 사용)
import matplotlib  # matplotlib 전체 라이브러리 불러오기

# print(matplotlib.__version__)  # 현재 설치된 matplotlib 버전 출력


x = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # x축에 사용할 데이터 리스트 (가로축 값)
y = [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  # y축에 사용할 데이터 리스트 (세로축 값)

# plt.plot(x, y)  # 선 그래프 생성 (x와 y를 연결한 선을 그림)
# # plot(x, y)
# # x: x축 데이터
# # y: y축 데이터

# plt.title('Line Graph')  # 그래프 제목 설정
# # title(문자열): 그래프의 제목을 설정

# plt.xlabel('X-axis')  # x축 이름 설정
# # xlabel(문자열): x축에 표시될 라벨 설정

# plt.ylabel('Y-axis')  # y축 이름 설정
# # ylabel(문자열): y축에 표시될 라벨 설정

# plt.grid(True)  # 격자(눈금선) 표시
# # grid(True/False): 그래프에 격자 표시 여부

# plt.show()  # 그래프를 화면에 출력
# # show(): 지금까지 만든 그래프를 화면에 보여줌


import matplotlib as mpl  # matplotlib을 mpl이라는 이름으로 사용

mpl.rc('font', family='Malgun Gothic')  # 한글 폰트 설정 (윈도우 기본 폰트)
# rc('font', family=폰트명): 그래프에서 사용할 기본 글꼴 설정

mpl.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지 설정
# rcParams['axes.unicode_minus']: 음수 기호 깨짐 방지 옵션

y2 = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]  # 두 번째 선 그래프용 데이터
plt.plot(x, y, label='감소하는 선', color='blue', linestyle=':')  
# plot(x, y, label, color, linestyle)
# label: 범례에 표시될 이름
# color: 선 색상
# linestyle: 선 스타일 ('-' 실선, ':' 점선 등)
plt.plot(x, y2, label='증가하는 선', color='#FF0000', linestyle='-')  
# 두 번째 선 그래프 (빨간색, 실선)
plt.title('그래프 제목', pad=30)  # 👈 제목과 그래프 간격 확보
plt.xlabel('X-axis')  # x축 이름 설정
plt.ylabel('Y-axis')  # y축 이름 설정
plt.grid(True)  # 격자 표시

plt.legend(loc='upper center', bbox_to_anchor=(0.5, 1.125), ncol=2)

plt.subplots_adjust(top=0.8)  # 👈 제목 아래 공간 확보

# legend(): label로 지정한 값들을 범례로 표시
plt.show()  # 그래프 출력


# import numpy as np  # numpy 라이브러리를 np로 사용 (배열 계산에 사용)
# categories = ['학생1', '학생2', '학생3', '학생4']  # x축 카테고리 이름
# values = [85, 92, 78, 90]  # 첫 번째 데이터 (국어 점수)
# values2 = [88, 91, 75, 85]  # 두 번째 데이터 (수학 점수)
# x = np.arange(len(categories))  
# # arange(n): 0부터 n-1까지 배열 생성 → [0,1,2,3]
# plt.bar(x - 0.2, values, width=0.4, label='국어 성적', color='blue')  
# # bar(x, height, width, label, color)
# # x: 막대 위치
# # height: 값(막대 높이)
# # width: 막대 너비
# plt.bar(x + 0.2, values2, width=0.4, label='수학 성적', color='orange')  
# # 두 번째 막대를 옆으로 이동해서 겹치지 않게 표시
# plt.title('학생 성적 비교')  # 그래프 제목
# plt.xlabel('학생')  # x축 이름
# plt.ylabel('성적')  # y축 이름
# plt.xticks(x, categories)  
# # xticks(위치, 라벨): x축 눈금 위치와 이름 설정
# plt.grid(axis='y')  
# # grid(axis='y'): y축 방향으로만 격자 표시
# plt.legend()  # 범례 표시
# plt.show()  # 그래프 출력


# labels = ['피자', '햄버거', '샐러드', '파스타']  # 각 조각 이름
# sizes = [40, 30, 20, 10]  # 각 조각 비율
# colors = ['gold', 'lightcoral', 'lightskyblue', 'lightgreen']  # 색상 리스트
# explode = (0.1, 0, 0, 0)  # 첫 번째 조각만 강조 (튀어나오게)
# plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, explode=explode)  
# # pie(sizes, labels, colors, autopct, startangle, explode)
# # sizes: 각 조각 크기
# # labels: 이름
# # autopct: 퍼센트 표시 형식
# # startangle: 시작 각도
# # explode: 강조 효과
# plt.title('음식 선호도')  # 제목 설정
# plt.axis('equal')  
# # axis('equal'): 원형이 찌그러지지 않도록 설정
# plt.show()  # 그래프 출력

# x = [1.5, 2.5, 3.5, 4.5, 5.5]  # x값 (키)
# y = [50, 60, 65, 70, 75]  # y값 (몸무게)
# plt.scatter(x, y, c='blue', s=100)  
# # scatter(x, y, c, s)
# # c: 색상
# # s: 점 크기
# plt.title('키와 몸무게의 관계')  # 제목
# plt.xlabel('키(미터)')  # x축 이름
# plt.ylabel('몸무게(킬로그램)')  # y축 이름
# plt.grid()  # 격자 표시
# plt.show()  # 그래프 출력

# data = []  # 히스토그램용 데이터 저장 리스트
# for i in range(500):  # 0부터 499까지 반복
#     value = sum([(i * j) % 100 / 100 for j in range(1, 13)]) - 6  
#     # 리스트 내포:
#     # (i*j)%100 → 나머지 계산
#     # /100 → 0~1 사이 값으로 변환
#     # sum() → 총합 계산
#     data.append(value)  # 계산된 값을 리스트에 추가
# plt.hist(data, bins=30, color='skyblue', alpha=0.7)  
# # hist(data, bins, color, alpha)
# # bins: 구간 개수
# # alpha: 투명도
# plt.title('정규 분포 히스토그램')  # 제목
# plt.xlabel('값')  # x축 이름
# plt.ylabel('빈도수')  # y축 이름
# plt.grid()  # 격자 표시
# plt.show()  # 그래프 출력

# fig, axs = plt.subplots(1, 2,  figsize=(15, 8))
# # subplots(행, 열 , figsize=(가로, 세로) )
# # 그래프 크기 설정 (인치 단위)
# # 1행 2열 그래프 생성 → axs[0], axs[1]로 접근 가능
# axs[0].plot([1, 2, 3], [1, 4, 9])  # 첫 번째 그래프에 선 그래프
# axs[0].set_title('선 그래프')  # 제목
# axs[0].set_xlabel('x값')  # x축 이름
# axs[0].set_ylabel('y값')  # y축 이름
# axs[1].bar([1, 2, 3], [3, 5, 2])  # 두 번째 그래프에 막대 그래프
# axs[1].set_title('막대그래프')  # 제목
# axs[1].set_xlabel('카테고리')  # x축 이름
# axs[1].set_ylabel('빈도수')  # y축 이름
# plt.savefig('./day13/save_chart.png')  # 그래프 사진으로 저장
# plt.show()  # 전체 그래프 출력
