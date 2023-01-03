# -------------------------------------------------------------------
# 인덱스(Index) 다루기
# -------------------------------------------------------------------
# 모듈/패키지 로딩 ---------------------------------------------------
import pandas as pd 

# DF 생성 -----------------------------------------------------------
df1=pd.DataFrame({'name':['마징가','배트맨','원더우먼'],
                'kor':[87,91,69],
                'eng':[99,73,89],
                'sci':[71,95,62]})

# DF 데이터 확인
print(f'df1 =>\n{df1}')
print(f'df1.index => {df1.index}')
print(f'df1.columns => {df1.columns}')

# [1] 특정 컬럼을 (행)인덱스로 설정 ------------------------------------
# unique(중복되지 않는) 컬럼을 인덱스로 설정
# DataFrame.set_index()

# 'name'컬럼을 행 인덱스로 설정하고 싶음
nameDF2=df1.set_index('name')     
print(nameDF2)                    

# 모든 행에 대한 값을 출력 => DF.loc[행인덱스] 
for rIdx in nameDF2.index:
    print(rIdx,nameDF2.loc[rIdx],sep='\n\n')
    print('-'*45)
sr1=nameDF2.loc['마징가']
print(sr1)


# [2] 인덱스 부분 변경 ---------------------------------------------------
# 전체 변경 => DF.index=[새로운 인덱스], DF.columns=[새로운 인덱스]
# DataFrame.rename()

# 행 인덱스 '마징가' '배트맨' '원더우먼' ====>  '배트맨'->'홍길동'
copydf1=nameDF2.rename(index={'배트맨':'홍길동'})
print(copydf1,'\n\n')

df = pd.DataFrame({'A':[1,2,3],'B':[4,5,6]})
print(df)

# 열(columns) 인덱스 변경
df.rename(columns={'B':'BB'},inplace=True)
print(df)

# 행(row) 인덱스 변경
df.rename(index={0:10,1:20,2:30},inplace=True)
print(df)
# 행(row) 인덱스 변경 => 10,20,30 => '10','20','30'
df.rename(index=str,inplace=True)
print(df.index)


# [3] 새로운 인덱스 설정 ---------------------------------------------------
# DataFrame.reindex([새로운 인덱스])
# 기존 인덱스랑 갯수나 이름 다를 수 있음 => 기존 인덱스가 아닌 인덱스의 값은 존재하지 않음 => NaN
newDF=df.reindex(['10','15','20','25'])
print('기존 인덱스 :',df,sep='\n')
print('변경된 인덱스 :',newDF,sep='\n')  # NaN : Not a Number = 공백x,값이 없음
# 변경된 인덱스 :
#       A   BB
# 10  1.0  4.0
# 15  NaN  NaN
# 20  2.0  5.0
# 25  NaN  NaN

# 결측(NaN) 처리
newDF=df.reindex(['10','15','20','25'],method='ffill') #앞의 값으로 채움
print('기존 인덱스 :',df,sep='\n')
print('변경된 인덱스 :',newDF,sep='\n')

newDF=df.reindex(['10','15','20','25'],method='bfill') # 뒤의 값으로 채움
print('기존 인덱스 :',df,sep='\n')
print('변경된 인덱스 :',newDF,sep='\n')

newDF=df.reindex(['10','15','20','25'],fill_value=0) # 지정한 디폴트값으로 채움
print('기존 인덱스 :',df,sep='\n')
print('변경된 인덱스 :',newDF,sep='\n')

# [4] 판다스에서 지정하는 기본 인덱스로 초기화 설정 ------------------------------
# DataFrame.reset_index()

# 기존 인덱스 => 컬럼으로 추가
newDF2=newDF.reset_index() 
print(newDF2)
# 기존 인덱스 => 드랍
newDF2.reset_index(drop=True)
print(newDF2)