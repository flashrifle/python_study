# 문자열 포매팅이 없다면
# ??님 수강기간이 7일 남았습니다.

name = '리잼'
duration = 7

massage = name + '님 수강기간이' + str(duration) + '일 남았습니다.'
print(massage)

# 문자열 포매팅 사용
massage_format = f'{name}님 수강기간이 {duration}일 남았습니다.'
print(massage_format)

# format 메서드
hello = 'Hello {0} {1} {2}'.format('apple', 'banana', 'pen')
print(hello)

# f-string 메서드
shoes = '나이키'
size = 270
print(f'제 신발은 {shoes}이고 size는 {size}입니다.')