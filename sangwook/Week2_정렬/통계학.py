# 수를 처리하는 것은 통계학에서 상당히 중요한 일이다.
# 통계학에서 N개의 수를 대표하는 기본 통계값에는 다음과 같은 것들이 있다. 단, N은 홀수라고 가정하자.
# 산술평균 : N개의 수들의 합을 N으로 나눈 값
# 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# 범위 : N개의 수들 중 최댓값과 최솟값의 차이
# N개의 수가 주어졌을 때, 네 가지 기본 통계값을 구하는 프로그램을 작성하시오.
# 첫째 줄에 수의 개수 N(1 ≤ N ≤ 500,000)이 주어진다. 단, N은 홀수이다.
# 그 다음 N개의 줄에는 정수들이 주어진다. 입력되는 정수의 절댓값은 4,000을 넘지 않는다.

# 첫째 줄에는 산술평균을 출력한다. 소수점 이하 첫째 자리에서 반올림한 값을 출력한다.
# 둘째 줄에는 중앙값을 출력한다.
# 셋째 줄에는 최빈값을 출력한다. 여러 개 있을 때에는 최빈값 중 두 번째로 작은 값을 출력한다.
# 넷째 줄에는 범위를 출력한다.

import sys
from collections import Counter

n = int(input())
nums = []
for _ in range(n):
    num = int(sys.stdin.readline())
    nums.append(num)
# 계산을 위해 숫자들의 리스트를 오름차순으로 정렬
lst = sorted(nums)
# 1. 산술평균 출력
print(round(sum(lst) / len(lst)))
# 2. 중앙값 출력
print(lst[len(lst) // 2])
# 3. 최빈값 출력
# 카운트를 세기 위해 collections의 Counter를 사용
# 참고용 Counter 출력 예시
# mode = c.most_common()
# print(mode)
# [(4, 3), (3, 2), (5, 2), (1, 1), (2, 1)]
c = Counter(lst)
# 가장 많이 나온 값 2개만 추출
mode = c.most_common(2)
# 똑같은 값 하나만 들어온 경우
if len(mode) == 1:
    print(mode[0][0])
# 가장 많이 나온 값이 하나만 있는 경우
elif mode[0][1] != mode[1][1]:
    print(mode[0][0])
# 여러 개 나온 경우
else:
    print(mode[1][0])
# 4. 범위 출력
print(max(lst) - min(lst))

