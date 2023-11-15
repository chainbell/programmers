def solution(people, limit):
    answer = 0
    people = sorted(people)
    print(people)
    l, r = 0, len(people)-1

    while l <= r:
        if people[l] + people[r] <= limit:
            l += 1
        r -= 1
        answer += 1

    return answer


people = [70, 50, 80, 50]
limit = 100

result = solution(people, limit)
print(result)