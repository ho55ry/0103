# ----------------------------------------------------------------------------------------------------
# 데이터 프레임 (DataFrame) 요소 다루기
# - 요소 : 행인덱스 , 열이름
# ----------------------------------------------------------------------------------------------------
# 패키지, 모듈 로딩----------------------------------------------------------------------------
import pandas as pd

# 데이터 프레임(DF) 생성 실습-------------------------------------------------------------------------------
data=[[10,20,30],['F','M','M'],[11,22,33],[44,55,66],['A','B','C']]
df1=pd.DataFrame(data)

# DF 요소/원소 다루기 ------------------------------------------------------------------------------------
# 열(column) 기준으로 요소
# 0번 컬럼 가져오기 => 변수명[컬럼명]
print(f'columns => {df1.columns}')
one=df1[0]
print(f'one => {type(one)}\n{one}')

print('---------------------------------------------')
for col in df1.columns:
    print(f'[{col}] => {type(df1[col])}\n{df1[col]}')

# 컬럼 여러개 가져오기 => 변수명[컬럼명,컬럼명]

# 0번, 2번 가져오기
onetwo=df1[[0,2]]
print(f'onetwo => {type(onetwo)}\n{onetwo}')

print(df1[0:1])   # 변수명[이상:미만] 로우 출력
#     0   1   2
# 0  10  20  30

# DF 요소/원소 다루기 열(column) ------------------------------------------------------------------------
# DF의 컬럼속성변경 => 변수명.속성명=새로운 값
df1.columns=['One','Two','Three']
print(f'변경 확인 : {df1.columns}\n{df1}')

# 'One' 컬럼 가져오기 => 변수명[컬럼]
print(f"df1['One'] => {type(df1['One'])}\n{df1['One']}")
print(f"df1.One => {type(df1.One)}\n{df1.One}")

# 컬럼 인덱스 변경 후 기본 인덱스 사용 불가
# print(df1[0]) # 안됨


# DF 요소/원소 다루기 행(row) ---------------------------------------------------------------------------------
# 변수명.iloc[인덱스] : 정수형 인덱스만 가능
# 변수명.loc[인덱스] : 문자열 인덱스 가능

# 0번 행 데이터 가져오기
print(df1)
zeroRow=df1.iloc[0]
print(f'zeroRow => {type(zeroRow)}\n{zeroRow}')

# 여러 행 데이터 가져오기 => 변수명.iloc[[인덱스,인덱스]]
zerotwoRow=df1.iloc[[0,2]]
print(f'zerotwoRow => {type(zerotwoRow)}\n{zerotwoRow}')

# 범위 지정 데이터 가져오기 => 변수명.iloc[이상:미만]  or 변수명[이상:미만]
onethreeRow=df1.iloc[1:4]
print(f'onethreeRow => {type(onethreeRow)}\n{onethreeRow}')

onethreeRow2=df1[1:4]
print(f'onethreeRow2 => {type(onethreeRow2)}\n{onethreeRow2}') # 두 개가 같은 결과


# 행(Row) 인덱스 속성 변경 후 행 추출 ----------------------------------------------------------------------
print(df1)
df1.index=['A','B','C','D','E']
print(df1)

# zeroRow=df1.iloc['A'] # 오류발생 iloc는 정수인덱스만
zeroRow=df1.loc['A']
# zeroRow=df1.loc[0] # 인덱스 이름 바꿔놓고 loc에서 정수인덱스로 부르면 오류남
zeroRow2=df1.iloc[0] 
print(zeroRow)
print(zeroRow2)

# ------------------------------------------------------
df1.index=[1,2,3,4,5]
print(df1)
print(df1.iloc[1]) # 행 이름 상관없이 무조건 행 번호
print(df1.loc[1]) # 행 이름
# -----------------------------------------------------
df1.index=['A','B','C','D','E']


# 요소/원소 (element) 추출하기----------------------------------------------------------------------------------
print('-'*60)
print(df1)
print('-'*60)
# 사용법 : 변수명.iloc[행번호,열번호]  or 변수명.iloc[행번호][열번호]
#        : 변수명.loc[행이름,열이름] or 변수명.loc[행이름][열이름]

# 요소값이 33인 데이터 추출
v33=df1.loc['C','Three']
v22=df1.loc['C','Two']
print(f'v33 => {v33}, v22 => {v22}')

# 데이터 44와 66 추출하고 싶음
v44=df1.iloc[3,0]
v66=df1.loc['D']['Three']
v44_66=df1.iloc[3,[0,2]]
print(f'v44 => {v44}, v66 => {v66}')
print(f'v44_66 => \n{v44_66}')

# 요소값이 20,30,22,33 인 데이터 추출하고 싶음
vv=df1.iloc[[0,2],[1,2]]
vv2=df1.loc[['A','C'],['Two','Three']]
print(f'vv =>\n{vv}')
print(f'vv2 =>\n{vv2}')

