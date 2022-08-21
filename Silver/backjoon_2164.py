import sys
from collections import deque

n = int(sys.stdin.readline())

queue = deque([i for i in range(1, n+1)])
while len(queue) >1:
    queue.popleft()
    firstNumber=queue.popleft()
    queue.append(firstNumber)
print(queue.popleft())
"""오답: 시간 초과."""
"""
import sys
n = int(sys.stdin.readline())
card = []
# 첫장은 버리고 다음카드는 마지막 옮긴다. ** 마지막 카드 하나 남을 때 까지.
def card_setting(card):
    card.pop(0)
    first_card=card[0]
    card.append(first_card)
    for i in range (0, len(card)) :
        if(len(card)>i+1):
            card[i] = card[i + 1]
    card.pop()
    # 남은 카드가 한장이 아니면 재귀함수.
    if(len(card)!=1):
        return card_setting(card)
    else:
        return card
#  n번째 카드 숫자 개수
for i in range(1,n+1):
    card.append(i)

result=card_setting(card)
print(result.pop())
"""






