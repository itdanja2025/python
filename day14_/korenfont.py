import matplotlib as mpl  # matplotlib을 mpl이라는 이름으로 사용

mpl.rc('font', family='Malgun Gothic')  # 한글 폰트 설정 (윈도우 기본 폰트)
# rc('font', family=폰트명): 그래프에서 사용할 기본 글꼴 설정

mpl.rcParams['axes.unicode_minus'] = False  # 마이너스 깨짐 방지 설정
# rcParams['axes.unicode_minus']: 음수 기호 깨짐 방지 옵션