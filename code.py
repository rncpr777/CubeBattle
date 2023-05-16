import random
import time 

def play():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    if a > b:
        return 1 
    if b > a:
        return 2
    else:
        return play()
        
print('!!!Welcome to DiceBattle!!!')
print('How many rounds do you want to simulate?')
rounds = int(input())
p1 = 0 
p2 = 0 
print('0:0')
print('')
for i in range(rounds):
    res = play()
    if res == 1:
        p1 = p1 + 1
    elif res == 2:
        p2 = p2 + 1
    print(str(p1) + ':' + str(p2))
    print('')
    time.sleep(2)
