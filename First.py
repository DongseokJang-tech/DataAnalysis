# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

# #은 한줄 주석

"""
여러줄 주석

"""

# 실행 ; 초록버튼 or F5
# 부분실행 : 블럭지정 and Ctrl + Enter
# 한줄실행 : F9


## 커맨드 라인 삭제 - cls

print("Hello~ World")

a = 3
b = 4
a + b
a * b
a / b

a ** b

7 % 3
3 % 7

## 8진수(Octal)
c = 0o177
print(c)

# 16진수(Hexadecimal)
d = 0x8ff
e = 0xABC
print(d)
print(e)

#-----------------------
7 / 4  # 1.75
7 // 4 # 1


a = 80
b = 75
c = 55
R = (a + b + c)/3
R


food = "Python's favorite food is perl"

food = 'Python's favorite food is perl


say  = '"Python is very easy." he says.'


food = 'Python\'s favorite food is perl'

food = 'Python's favorite food is perl'


say  = "\"Python is very easy.\" he says."
food
say


## 
multiline = "Life is too short\nYou need python"
print(multiline)


multiline1 = '''
    Life is too short
    You need python
    '''
print(multiline1)


multiline2 = """
    Life is too short
    You need python
    """
print(multiline2)


##
a = 123
type(a)

a = 100 ** 100
print(a)


##
a = True
type(a)

a = (100 == 100)
b = (10 > 100)
print(a, b)


a = "파이썬 만세"
print(a)
type(a)


a = "이건 큰따옴표 \" 모양."
b = '이건 작은따옴표 \' 모양.'
print(a, b)

a = '파이썬 \n만세'
print(a)

a = """파이썬
만세"""
a
print(a)


# 문자열 더해서 연결하기
head = "Python"
tail = " is fun!"
head + tail

# 문자열 곱하기
a = "python"
a * 2


print("=" * 50)
print("My Program")
print("=" * 50)



print("\n줄바꿈\n연습 ")
print("\t탭키\t연습")
print("글자가 \"강조\"되는 효과1")
print("글자가 \'강조\'되는 효과2")
print("\\\\\\ 역슬래시 세 개 출력")
print(r"\n \t \" \\를 그대로 출력")



## ==================================
# 1)
print('이름\t나이\t지역')
print('오라클\t10\t구로구')
print('파이썬\t3\t구로구')

# 2)
print('동해물과 백두산이 마르고 닳도록 \n하느님이 보우하사 우리나라 만세')

# 3)
print('안녕하세요 ' * 3)

# 4)
print('안\n녕\n하\n세\n요')


# 문자열 자료형 - 인덱싱(Indexing)
a = "Life is short, You need python"
a[0]
a[12]
a[-1]
a[-2]

a = "안녕하세요"
a[0]
a[1]
a[2]
a[3]
a[4]

print('안녕하세요' [-1])
print('안녕하세요' [-2])
print('안녕하세요' [-3])
print('안녕하세요' [-4])
print('안녕하세요' [-5])


a = "Life is too short, you need Python"
b = a[0] + a[1] + a[2] + a[3]
b


a = "Life is too short, you need Python"
a[0:4]
a[0:3]
a[0:5]
a[5:7]
a[12:17]


a = "Life is too short, you need Python"
a[19:]
a[:17]
a[:]
a[19:-7]


a = "20010331Rainy"
date = a[:8]
weather = a[8:]
date
weather

year = a[:4]
day = a[4:8]
year
day


## 주민등록번호 881120-1068234 나누기
## 연월일(YYMMDD) 부분과 그 뒤의 숫자 부분으로 나누어 출력해보기

pin = "881120-1068234"
yyyymmdd = pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)


## 주민등록번호 성별표시숫자 출력하기
pin = "881120-1068234"
print(pin[7])


## ======================================
# 1) head = "Python은"
#    tail = "아주 훌륭한 프로그래밍 언어이다" 일 때 아래와 같은 결과가 나오도록 하려면?

""" 
 =======================================
 Python은 아주 훌륭한 프로그래밍 언어이다
 ======================================="""

head = "Python은"
tail = "아주 훌륭한 프로그래밍 언어이다"
print('=' * 50)
print(head + ' ' + tail)
print('=' * 50)


# 2) string = "orajava" 일 때 아래와 같은 결과가 나오도록 출력하기
"""
orajava
java
ora
oraj
orajava
"""
string = "orajava"
print(string)
print(string[3:])
print(string[:3])
print(string[:4])
print(string)


# 3)
# pi = 3.141592이 아래와 같이 출력되게하기
# ==>변수 pi의 자료형은 <class 'float'>
pi = 3.141592
type(pi)


# 4)
# 3)에서 pi = 3이 아래와 같이 출력되게하기
# ==>변수 pi의 자료형은 <class 'int'>
pi = 3
type(pi)


# colors = ['red', 'blue', 'green']가 있을 때 결과가 아래와 같이 나오게하기
colors = ['red', 'blue', 'green']
# 5-1) red
print(colors [0])

# 5-2) green
print(colors [2])


# 6)
# color1과 color2가 아래와 같을 때 각각 문제에 주어진 결과가 나오게 하기
color1 = ['red', 'blue', 'green']
color2 = ['orange', 'black', 'white']

# 6-1) ['red', 'blue', 'green', 'orange', 'black', 'white']
print('[\'' + color1[0] + '\', \'' + color1[1] + '\', \'' + color1[2] + '\', \'' + color2[0] + '\', \'' + color2[1] + '\', \'' + color2[2] + '\']')

# 6-2) ['red', 'blue', 'green', 'red', 'blue', 'green']
print('[\'' + color1[0] + '\', \'' + color1[1] + '\', \'' + color1[2] + '\', \'' + color1[0] + '\', \'' + color1[1] + '\', \'' + color1[2] + '\']')


# 7) 다음과 같은 리스트가 있을 때 출력 결과가 아래와 같게 해보기
test = ['설현', '초아', '지민', '유나', '유경', '혜정', '민아', '찬미']

# 7-1) '지민'
print('\'' + test[2] + '\'')

# 7-2) '민아'
print('\'' + test[6] + '\'')

# 7-3) ['설현']
print('[\'' + test[0] + '\']')

# 7-4) ['민아', '찬미']
print('[\'' + test[6] + '\', \'' + test[7] + '\']')

# 7-5) ['초아', '지민']
print('[\'' + test[1] + '\', \'' + test[2] + '\']')

# 7-6) ['초아', '유경', '찬미']
print('[\'' + test[1] + '\', \'' + test[4] + '\', \'' + test[7] + '\']')





















