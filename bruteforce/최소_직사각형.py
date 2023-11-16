def solution(sizes):
    return max([sorted(i)[0] for i in sizes]) * max([sorted(i)[1] for i in sizes])


# 가로, 세로 길이의 리스트
sizes = [[60, 50], [30, 70], [60, 30], [80, 40]]

result = solution(sizes)