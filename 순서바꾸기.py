# 풀이1
def solution(num_list, n):
    answer_front = []
    answer_back = []
    for i in range(len(num_list)):
        if i >= n:
            answer_front.append(num_list[i])
        else:
            answer_back.append(num_list[i])
    return answer_front + answer_back

# 풀이2
def solution(num_list, n):
    return num_list[n:] + num_list[:n]