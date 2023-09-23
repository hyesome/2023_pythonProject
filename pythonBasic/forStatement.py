numbers = [1, 2, 3, 4, 5, 6, 7, 8]
strings = ["hello", "world"]

anys = [1, "hello", True, [1, 2, 3, 4]]

print(numbers[0])
print(strings[0])

print(anys[3][2])

scores = [84, -5, 65, 79, 105, 100, 91, 50, -32, 80, 54, 23, 58, 98, 64, 95, 90, 39, 84, 67, 82, 99, 91]

print(scores[3:])
print(scores[1:4])
print(scores[:3])

# 평균을 구하고 싶을때.
sum = 0
# for i in scores:
#     if 0 < i < 100:
#         sum = sum + i
#

for i in scores:
    if i > 100 or i < 0:
        print("skip", i)
        continue
    sum = sum + i


average = sum / len(scores)

print("학생들의 점수 총합: ", sum)
print("학생들의 점수 평균: ", average)

# for i in range(0, 11):
#     print(i)

# 소숫점 이용하기
# 외부 라이브러리 사용으로는 가능하지만
# range 함수기준으로는 정수만 사용 가능

for i in range(0, 5, 1):
    print(i*0.1)