# 풀이1
def solution(arr, n):
    if len(arr) % 2 == 1:
        for i in range(0, len(arr), 2):
            arr[i] += n
    else:
        for i in range(1, len(arr), 2):
            arr[i] += n
    return arr

# 풀이2
def solution(arr, n):
    answer = []
    for i in range(len(arr)):
        if len(arr) % 2 == 1:
            if i % 2 == 0:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
        else:
            if i % 2 == 1:
                answer.append(arr[i]+n)
            else:
                answer.append(arr[i])
    return answer