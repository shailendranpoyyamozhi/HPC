class Solution:
    def isValid(self, s: str) -> bool:
        LS = []
        for c in s:
            if c in ['(', '{', '[']:
                LS.append(c)
            elif c == ')' and len(LS) != 0 and LS[-1] == '(':
                LS.pop()
            elif c == '}' and len(LS) != 0 and LS[-1] == '{':
                LS.pop()
            elif c == ']' and len(LS) != 0 and LS[-1] == '[':
                LS.pop()
            else:
                return False
        return LS == []
        
