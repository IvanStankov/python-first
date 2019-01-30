from collections import deque

deq = deque(["one", "two", "three"])
print(deq)

deq.append("four")
print(deq)

deq.appendleft("zero")
print(deq)

print(".popleft() and deq after")
print(deq.popleft())
print(deq)

print(".pop() and deq after")
print(deq.pop())
print(deq)
