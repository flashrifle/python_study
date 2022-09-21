# 1. replace
# 문자열 교체

a = '오늘 날씨는 흐림입니다.'.replace("흐림", "맑음")
print(a)

# 2. find
# 문자열 찾기
b = "hello world".find('world')
print(b)

# 3. split
# 문자열 분리
c = '동해물과 백두산이 마르고 닳도록'.split()
print(c)

d = '동해물과:백두산이:마르고:닳도록'.split(':')
print(d)

# 4. strip
# 문자열 공백 제거
text = '    text    '
print("[" + text.rstrip() + "]")
print("[" + text.lstrip() + "]")
print("[" + text.strip() + "]")