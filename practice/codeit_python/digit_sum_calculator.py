# 자리수 합 리턴
def sum_digit(num):
    total = 0 
    str_num = str(num)
    
    for i in range(len(str_num)):
        digit = str_num[i]
        total += int(digit)
    return total

# sum_digit(1)부터 sum_digit(1000)까지의 합 구하기
total_sum = 0 
for i in range(1, 1001):
    total_sum += sum_digit(i)
    
print(total_sum)