# -------------------------------------------------------------------
# CSV FILE => DataFrame  객체로 저장
# - pandas.read_csv(경로)
# -------------------------------------------------------------------
import pandas as pd

FILE='datafiles\\banklist.csv'
# =FILE=r'datafiles\banklist.csv'

# DF 객체 생성 --------------------------------------------------------
bankDF=pd.read_csv(FILE)

# DF 확인 -------------------------------------------------------------
print(f'bankDF => \n{bankDF}')

# [1] 전체 요약 정보 제공 메서드 -> info()
bankDF.info()           # 프린트기능 포함

# [555 rows x 7 columns]
# <class 'pandas.core.frame.DataFrame'>
# RangeIndex: 555 entries, 0 to 554             # entries=rows
# Data columns (total 7 columns):
#  #   Column                 Non-Null Count  Dtype     # Null : 결측
# ---  ------                 --------------  -----
#  0   Bank Name              555 non-null    object
#  1   City                   555 non-null    object
#  2   ST                     555 non-null    object
#  3   CERT                   555 non-null    int64
#  4   Acquiring Institution  555 non-null    object
#  5   Closing Date           555 non-null    object
#  6   Updated Date           555 non-null    object
# dtypes: int64(1), object(6)
# memory usage: 30.5+ KB


# [2] 앞부분(뒷부분) 5줄(기본값) 실제 데이터 확인
print(bankDF.head())            # 프린트기능 포함x
print(bankDF.tail(3))


# [3] 데이터의 기술통계를 적용한 결과
print(bankDF.describe())            # 수치 데이터만 가능 (기본값)
print(bankDF.describe(include='all'))            # 모든 데이터 가능 (include='all')

# 데이터 가지고 놀기 -------------------------------------------------------------------
# (1) 4개 컬럼만 사용 => Bank Name, City, Closing Date, Updated Date  (0,1,5,6)
print(f'bankDF.columns = > {bankDF.columns}')
newDF=bankDF[['Bank Name', 'City','Closing Date', 'Updated Date']]
print(newDF.head(3))

# (2) 컬럼 중에서 인덱스로 설정
newDF.set_index(['Bank Name','City'],inplace=True)
print(newDF.info())
print(newDF.head(3))

# (3) UPdateed Date 기준으로 가장 최근 날짜부터 정렬
# 최신순 => 날짜 내림차순 (ascending=False)
# object => str  -----> datetime
newDF.sort_values(by=['Updated Date'], key=lambda col: pd.to_datetime(col), ascending=False,inplace=True)
print(newDF['Updated Date'].values)
print(newDF)
print(type(newDF['Updated Date'][0])) # 데이터 타입이 바뀐게 저장되지는 않음. 정렬만 원본 변경

