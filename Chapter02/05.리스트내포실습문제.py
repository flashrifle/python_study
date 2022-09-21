# 실습문제 2.4.1
# 리스트 내포를 사용해서 word_list에 들어있는 첫글자가
# a인것만 뽑아서 list 생성


# word_list = ['apple', 'watch', 'apolo','abocada']

# #리스트 내포 사용전
# result = []
# for word in word_list:
#     if word[0] == 'a':
#         result.append(word)

# print(result)

# # 리스트 내포 사용
# result2 = [word for word in word_list if word[0] == 'a']

# print(result2)


# 실습문제 2.4.2
# 리스트 내포를 사용해서 None을 없애본다 

word = ['오메가3', 'None', '비타민C500', 'None', '홍삼절편']

# 리스트 내포 사용전
result = []
for i in word:
    if i != 'None':
        result.append(i)
    else:
        result.append('')
print(result)

# 리스트 내포 사용
result2 = [i if i != 'None' else '' for i in word]
print(result2)