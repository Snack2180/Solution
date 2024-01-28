# 팰린드롬수

Num = input()

while Num != '0':

    RN = Num[::-1]
    
    if Num == RN:
        print('yes')
        Num = input()
    else:
        print('no')
        Num = input()