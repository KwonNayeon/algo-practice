'''
문제 정의:
입력된 문자열이 팰린드롬인지 판별하는 함수 구현
(팰린드롬: 앞에서 읽으나 뒤에서 읽으나 동일한 문자열)
'''

def is_palindrome(word):
    # 문자열의 절반 길이만큼만 반복
    # (홀수 길이여도 가운데 문자는 확인할 필요 없음)
    for i in range(len(word) // 2):
        # i=0: 첫번째(word[0])와 마지막 문자(word[-1]) 비교
        # i=1: 두번째(word[1])와 끝에서 두번째 문자(word[-2]) 비교
        # -0 인덱싱 문제를 방지하기 위해 -(i+1) 사용
        if word[i] != word[-(i+1)]:
            return False
    # 모든 대칭 문자 쌍이 동일하므로 팰린드롬임
    return True


# 테스트
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False