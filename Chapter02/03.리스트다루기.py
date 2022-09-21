# 리스트 메서드

# 리스트 데이터 삭제
fruits = ['apple', 'orange', 'mango']
fruits.remove('orange')
print(fruits)

# 리스트 정렬
numbers = [0,1,2,7,3]
numbers.sort(reverse=True)
print(numbers)

# enumerate
# 리스트에 인덱스를 부여함
titles = ['출석', '출석인증', '출석이요']

for index, title in enumerate(titles, 1):
    print(f'{index}번째 글입니다. 제목: {title}')