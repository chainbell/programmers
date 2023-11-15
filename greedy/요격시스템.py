def solution(targets):
    answer = 0

    target_sort = sorted(targets, key=lambda target: target[1])
    cursor = -1
    for target in target_sort:
        # target이 지나가려 할 때,
        if cursor < target[1]:
            # 맞춘 적이 있는지 확인 한 후 쏜다.
            if cursor < target[0]:
                cursor = target[1] - 1
                answer += 1

    return answer


targets = [[4, 5], [4, 8], [10, 14], [11, 13], [5, 12], [3, 7], [1, 4]]

result = solution(targets)
print(result)
