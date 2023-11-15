def solution(n, lost, reserve):
    lost_set = set(lost)
    reserve_set = set(reserve)

    # 1. 문제 조건 : 여분의 체육복은 1회 도난당할 수 있다.
    reserve_result = reserve_set - lost_set

    # 2. 문제 조건 : 여분의 체육복에 대한 도난은 제외시킨다.
    lost_result = lost_set - reserve_set

    # 3. 왼쪽->오른쪽 순서로 체육복을 빌린다. 여기가 그리디
    count = len(lost_result)
    for lost in lost_result:
        if reserve_result.__contains__(lost - 1):
            count = count - 1
            reserve_result.remove(lost - 1)
        elif reserve_result.__contains__(lost + 1):
            count = count - 1
            reserve_result.remove(lost + 1)

    return n - count


n = 5
lost = [2, 4]
reserve = [1, 3, 5]

result = solution(n, lost, reserve)
print(result)