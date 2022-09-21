items = ['       로지텍 마우스  ',' 앱솔 키보드   ']

def strip_all(b):
    return b.strip()

items = list(map(strip_all, items))
print(items)

items = list(map(lambda x : x.strip(), items))
print(items)