x = [1,2,3,4,5]
y = x

y[2] = 0
print(y)
print(x)

print(id(y))
print(id(x))

# 리스트 복사방식

a = [5,6,7,8,9]
b = a.copy()

print(a, b)
print(id(a), id(b))

# 중첩 리스트 복사방식
import copy

c = [[1,2], [3,4,5]]
d = copy.deepcopy(c)
d[0][0] = 0

print(c)
print(d)