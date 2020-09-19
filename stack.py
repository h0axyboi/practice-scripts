from collections import deque
class Stack:
    def __init__(self):
        self.stack=deque()

    def push(self,data):
        self.stack.append(data)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return len(self.stack)==0

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)

def reverse_string(a):
    s=Stack()
    for c in a:
        s.push(c)
    new_str=''
    while not s.is_empty():
        new_str+=s.pop()
    return new_str

def is_match(c,s):
    d={
    ')':'(',
    '}':'{',
    ']':'['
    }
    return s.pop()==d[c]

def is_balanced(a):
    s=Stack()
    for c in a:
        if c=='(' or c=='{' or c=='[':
            s.push(c)
        elif c==')' or c==']' or c=='}':
            if s.is_empty():
                return False
            if not is_match(c,s):
                return False
    return False if not s.is_empty() else True

print(reverse_string('We will conquer COVID-19'))
print(is_balanced("({a+b})"))
print(is_balanced("))((a+b}{"))
print(is_balanced("((a+b))"))
print(is_balanced("))"))
print(is_balanced("[a+b]*(x+2y)*{gg+kk}"))
