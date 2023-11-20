"""
수열 A가 주어졌을 때, 가장 긴 감소하는 부분 수열을 구하는 프로그램을 작성하시오.

예를 들어, 수열 A = {10, 30, 10, 20, 20, 10} 인 경우에 가장 긴 감소하는 부분 수열은 A = {10, 30, 10, 20, 20, 10}  이고, 길이는 3이다.

첫째 줄에 수열 A의 크기 N (1 ≤ N ≤ 1,000)이 주어진다.

둘째 줄에는 수열 A를 이루고 있는 Ai가 주어진다. (1 ≤ Ai ≤ 1,000)

6
10 30 10 20 20 10
"""
length = 6
input = [10, 30, 10, 20, 20, 10]

def dp_1():
    count_list = [1] * length
    for i in range(1, length):
        for j in range(i):
            if input[j] > input[i]:
                # DP -> 기존에 사용한 값을 재활용 할 수 있어야 한다.
                count_list[i] = max(count_list[i], count_list[j] + 1)

    print(max(count_list))

dp_1()

# 아무리 생각해도 이게 딥러닝보다 어려운데
# 이전의 계산을 누적시켜서 재활용하는 것이 DP의 주 목적이다.