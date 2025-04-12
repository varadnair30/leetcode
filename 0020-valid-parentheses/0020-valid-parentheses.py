class Solution:
    def isValid(self, s: str) -> bool:

        stk = []
        for ch in s:
            if ch in "({[":
                stk.append(ch)
            elif ch in ")}]":
                if not stk:
                    return False
                top = stk[-1]
                if (ch == ')' and top == '(') or (ch == '}' and top == '{') or (ch == ']' and top == '['):
                    stk.pop()
                else:
                    return False
        return len(stk) == 0


        