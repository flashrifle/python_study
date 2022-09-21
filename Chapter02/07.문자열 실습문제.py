# 소요시간을 모두 분으로 바꾸는 프로그램 작성

# hour = int(input("시간을 입력하세요 : "))
# minute  = int(input("분을 입력하세요 : "))
# print(f'{hour}시간 {minute}분')
# result = hour * 60 + minute
# print(result)


time = input("시간을 입력하세요 : ")
# 1. 분만 있는경우 ex) 30분
# 2. 시간만 있는 경우 ex) 2시간
# 3. 시간과 분만 있는경우 ex) 2시간 30분

if time.find('시간') == -1 : # find 함수에 -1 값을 주면 값을 찾을 수 없다 판단
    # 분만 있는경우
    result = int(time.split('분')[0]) # 만약 30분이라고 입력을 했다면 ['30',''] 으로 표시가 되므로 
else:                                 # 첫번째 리스트를 출력하기위해 [0]을 넣어줌
    if time.find('분') == -1:
        #시간만 있는경우
        result = int(time.split('시간')[0]) * 60 # 시간은 60분이므로 입력한 시간에 60을 곱해준다
    else:
        # 시간과 분이 있는 경우
        sub = time.split('시간')
        result = int(sub[0]) * 60 + int(sub[1].split('분')) 

print(result)