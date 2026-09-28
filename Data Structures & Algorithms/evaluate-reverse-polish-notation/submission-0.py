class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []

        for c in tokens:
            if c=="+":
                s.append(s.pop()+s.pop())
            elif c=="-":
                x,y=s.pop(), s.pop()
                s.append(y-x)
            elif c=="/":
                x,y=s.pop(), s.pop()
                s.append(int(y/x))
            elif c=="*":
                s.append(s.pop()*s.pop())
            else:
                s.append(int(c))
        return s[-1]