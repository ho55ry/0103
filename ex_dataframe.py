# ----------------------------------------------------------------------------------------------------
# 데이터 프레임 (DataFrame)
# - 판다스의 구조화 데이터 타입
# - 구성 : 행과 열
# - 요소 : 행인덱스 , 열이름
# ----------------------------------------------------------------------------------------------------
# 패키지, 모듈 로딩
import pandas as pd

# 데이터 프레임(DF) 생성 실습
# 리스트 이용해서 데이터 만들어봄  // 리스트 1개 -> 시리즈 따라서 리스트2개 이용
data=[[10,20,30],['F','M','M']]
df1=pd.DataFrame(data)

# 데이터 확인 : 출력
print(f'df1 => \n{df1}')
#   0  1  2
#0 10 20 30 이렇게 나옴 0,1 행 인덱스 / 0,1,2 열 인덱스
#1 F   M  M
print(f'df1.index => {df1.index}')
print(f'df1.columns => {df1.columns}')
print(f'df1.shape => {df1.shape}')
print(f'df1.ndim => {df1.ndim}')
print(f'df1.dtypes => \n{df1.dtypes}') #=> 숫자,문자 섞이면 데이터 타입 object
print(f'df1.values => \n{df1.values}')
print('type(df1.values) =>',type(df1.values))


# 딕셔너리 이용해서 데이터 만들어봄  // 리스트 1개 -> 시리즈 따라서 리스트2개 이용
data={'name':['홍','이','박'],'job':['학생','학생','주부']}
df2=pd.DataFrame(data)

# 데이터 확인 : 출력
print(f'df2 => \n{df2}')
print(f'df2.index   => {df2.index}')
print(f'df2.columns => {df2.columns}')
print(f'df2.shape   => {df2.shape}')
print(f'df2.ndim    => {df2.ndim}')
print(f'df2.dtypes  => \n{df2.dtypes}')
print(f'df2.values  => \n{df2.values}\ntype(df2.values) => {type(df2.values)}')
