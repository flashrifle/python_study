# # 1. 위치 매개변수

# def my_func(a,b):
#     print(a,b)

# my_func(1,2)

# # 2. 기본 매개변수

# def post_info(title, content='내용없음'):
# 	print('제목:', title)
# 	print('내용:', content)
    
# post_info('출석합니다.')

# # 3. 키워드 매개변수

# def post_info(title, content):
# 	print('제목:', title)
# 	print('내용:', content)

# post_info(content='재밌다', title='코딩')

# 4. 위치 가변 매개변수
def print_fruits(*args):
    for arg in args:
        print(arg)

print_fruits('apple','orange','mango')

# 5. 키워드 매개변수
def comment_info(**kwargs):
    for key, value in kwargs.items():
        print(f'{key} : {value}')

# 함수호출
comment_info(name='파린이', comment='감사합니다')

# 매개변수 작성 순서
# 위치 - 기본 - 위치 가변 - 키워드(기본) - 키워드 가변

def post_info(title, content, *tags):
    print(f'제목: {title}')
    print(f'내용: {content}')
    print(f'태그: {tags}')

post_info('#파이썬', '#디장고' '파이썬함수정리', '다양한매개변수정리')