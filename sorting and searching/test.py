def solution(s):

    res = {}

    for x in s:
        if x in res:
            res.pop(x)
        else:
            res[x] = 1

    return res

print(solution('abcabcbb'))
print(solution('bbbbb'))
print(solution('pwwkew'))
