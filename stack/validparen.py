def validParen(s:str)->bool:
    stack = []
    hash_map = {')':'(',']':'[','}':'{'}

    for ch in s:
        if ch in hash_map:
            if stack and stack[-1] == hash_map[ch]:
                stack.pop()
            else:
                return False
        else:
            stack.append(ch)
    return not stack
s = ("()[]{}")
result = validParen(s)
print(result)
                
