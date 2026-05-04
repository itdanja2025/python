import pandas as pd
import json

# -------------------- 판다스 자료 가져오기 -------------------- #

# 1. CSV 파일 읽기
df = pd.read_csv(
    './day13_/data.csv',
    encoding='utf-8',          # 인코딩 설정 (한글 깨짐 시 'cp949' 또는 'euc-kr')
    header=0,                  # 첫 번째 행을 컬럼명으로 사용 (없으면 None)
    usecols=['사번', '이름', '나이', '부서'], # 필요한 컬럼만 선택해서 가져오기
    na_values=['-', '미응답', 'N/A'], # 특정 문자를 결측치(NaN)로 인식
    on_bad_lines='warn',    # 열 개수가 안 맞는 행은 경고 후 제외 (데이터 유실 방지)
    dtype={'사번': str}         # 특정 열의 데이터 타입을 지정하며 읽기
)
# read_csv(파일경로, encoding, header, usecols, na_values, dtype)
print(df.head())

# 2. 엑셀 파일 읽기 (openpyxl 필요) # pip install openpyxl
df = pd.read_excel(
    './day13_/data.xlsx', 
    sheet_name='Sheet1',       # 읽어올 시트 이름 또는 인덱스(0, 1...)
    skiprows=0,                # 상위 n개의 행을 제외하고 읽기
    na_values='NaN'            # 결측치로 처리할 값 지정
)
# read_excel(파일경로, sheet_name, skiprows, na_values)
print(df.head())

# 3. JSON 파일 읽기
with open('./day13_/data.json', 'r', encoding='utf-8') as json_file:
    data_json = json.load(json_file)
df = pd.DataFrame(data_json)
print(df.head())


# -------------------- 판다스 자료 내보내기 -------------------- #

# 1. CSV로 내보내기
df.to_csv(
    './day13_/data_out.csv', 
    index=False,               # 인덱스(행 번호) 저장 안함
    encoding='utf-8',      # 엑셀에서 한글 깨짐 방지 인코딩
    na_rep='Unknown',          # 결측치를 빈칸 대신 특정 문자로 채워 저장
    header=True                # 컬럼명(헤더) 포함 여부
)
# to_csv(파일명, index, encoding, na_rep, header)

# 2. 엑셀로 내보내기
df.to_excel(
    './day13_/data_out.xlsx', 
    index=False,
    sheet_name='회원정보'      # 엑셀 시트 이름 지정
)
# to_excel(파일명, index, sheet_name)

# 3. JSON으로 내보내기
df.to_json(
    './day13_/data_out.json', 
    orient='records',          # [{컬럼:값}, {컬럼:값}] 리스트 형태 저장
    force_ascii=False,         # 한글을 유니코드가 아닌 한글 그대로 저장
    date_format='iso'          # 날짜를 ISO 8601 형식으로 저장
)