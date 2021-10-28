# 22. 括号生成
class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        # 思路：利用回溯法生成所有可能，然后再判断每种可能是否可行
        res = []

        def valid(string):
            stack = []
            for ch in string:
                if ch == '(':
                    stack.append(ch)
                else:
                    if stack:
                        if stack[-1] == '(':
                            stack.pop(-1)
                    else:
                        return False
            return len(stack) == 0

        def traceback(depth, path):
            if depth == 2*n:
                if valid(path):
                    s_path = ''.join(path)
                    res.append(s_path)
                return
            else:
                for ch in '()':
                    path.append(ch)
                    depth += 1
                    traceback(depth, path)
                    path.pop(-1)
                    depth -= 1
        traceback(0, [])
        return res
