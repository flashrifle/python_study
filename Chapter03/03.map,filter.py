# 1. map함수
# - 사용하는이유
# 기조 리스트를 수정해서 새로운 리스트를 만들 때

# 사용방법
print(list(map(int, ['3','4','5','6'])))

# - 예제
# 리스트 모든 요소의 공백 제거
items = ['       로지텍 마우스  ',' 앱솔 키보드   ']

# 1) for문 사용 경우
for i in range(len(items)):
    items[i] = items[i].strip()

print(items)

# 2) map 사용
def strip_all(x):
    return x.strip()

items = list(map(strip_all, items))

# 3) 람다 사용
items = list(map(lambda x : x.strip(), items))
print(items)

# 2. filter 함수
# 기존 리스트에서 조건을 만족하는 요소만 뽑고 싶을 때

# 사용방법
# filter(함수, 순서가있는 자료형)
def func(x):
    return x < 0

print(list(filter(func, [-3,-2,0,5,7])))

# -예제
# 리스트에서 길이가 3이하인 문자들만 필터링
animals = ['cat','tiger','dog','bird','monkey']

# 1) for 사용
result = []
for i in animals:
    if len(i) <= 3:
        result.append(i)
print(result)

# 2) 필터 사용
def word_check(x):
    return len(x) <= 3
result = list(filter(word_check, animals))
print(result)

# 3) 람다 사용

result = list(filter(lambda x : len(x) <= 3, animals))
print(result)