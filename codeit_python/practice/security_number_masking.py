# [문제 정의]
# 입력된 주민번호의 마지막 4자리를 '*'로 마스킹하는 함수 구현

# [해결 과정]
def mask_security_number(security_number):
   # 주민번호 문자열을 리스트로 변환
   number_list = list(security_number)
   
   # 마스킹 시작 위치 계산
   mask_start = len(number_list) - 4
   
   # 마지막 4자리 마스킹 처리
   for index in range(mask_start, len(number_list)):
       number_list[index] = "*"
   
   return ''.join(number_list)

# 테스트
print(mask_security_number("880720-1234567"))  # 880720-123****
print(mask_security_number("8807201234567"))   # 88072012****

###############################################################
# [디버깅 포인트]
# 1. 문자열 → 리스트 변환
#    - 문자열은 immutable하므로 list()로 변환하여 수정
#
# 2. 인덱스 처리
#    - 전체 길이에서 4를 빼서 마스킹 시작점 계산
#    - range()로 정확한 범위 순회
#
# 3. 결과 반환
#    - join() 메서드로 리스트를 문자열로 결합
#    - 빈 문자열 ''로 구분자 없이 결합
###############################################################