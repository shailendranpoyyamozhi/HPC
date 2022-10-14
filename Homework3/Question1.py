def solution(list, num):
    look_for={}
    for n,x in enumerate(list,1):
        try:
            return list[look_for[x]-1], list[n-1]
        except:
            look_for.setdefault(num-x, n)

numbers = [0, 21, 78, 19, 90, 13] 
print(solution(numbers, 21))
print(solution(numbers, 25))
