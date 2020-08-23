from random import shuffle
from random import randint

color = ['黑桃', '紅心', '方塊', '梅花']
point = ['A','2','3','4','5','6','7','8','9','10','J','Q','K']
deck = [] 

for i in range(4):
    for j in range(13):
        deck.append( color[i]+point[j] )
shuffle(deck)

user_card = []     # 自己手牌
com_card = []      # 電腦手牌
cards_field = []   # 場上的牌, deck是還沒被抽得牌
field_total = 0    # 場上點數總和
for i in range(5):
    user_a = deck.pop()          
    user_card.append(user_a)
print("你抽的牌: ",user_card)

for i in range(5):
    com_a = deck.pop()
    com_card.append(com_a)

for i in range(9999):
    for j in range(999):
        a = input("你出的牌: ")
        if a == user_card[0] or a == user_card[1] or a == user_card[2] or a == user_card[3] or a == user_card[4] :
            break
        else:
            print("輸入錯誤")                              # 1刪使用者牌 2加場上牌 3加場上點數

    if a == user_card[0]:
        user_card.pop(0)
    elif a == user_card[1]:
        user_card.pop(1)
    elif a == user_card[2]:
        user_card.pop(2)
    elif a == user_card[3]:
        user_card.pop(3)
    else:
        user_card.pop(4)

    cards_field.append(a)

    if a[2:] =="4" or a[2:] =="5" or a[2:] =="J" :      # 4,5,j 皆為pass    # 10,Q,K 特殊牌
        print("你pass")
    elif a[:] =="黑桃A" :
        field_total = 0
    elif a[2:] =="A":
        b = "1"
        field_total = field_total + int(b)
        if field_total > 99 :
            print("爆了,你輸了")
    elif a[2:] =="10":
        for i in range(999):
            ch = input("請輸入(+10或-10): ")
            if ch == "+10":
                field_total = field_total + 10
                if field_total > 99 :
                    print("爆了,你輸了") 
                break
            elif ch == "-10":
                field_total = field_total - 10
                if field_total < 0 :
                    field_total = 0
                break
            else:
                print("輸入錯誤")
    elif  a[2:] =="Q" :
        for i in range(999):
            ch = input("請輸入(+20或-20): ")
            if ch == "+20":
                field_total = field_total + 20
                if field_total > 99 :
                    print("爆了,你輸了") 
                break
            elif ch == "-20":
                field_total = field_total -20
                if field_total < 0 :
                    field_total = 0
                break
            else:
                print("輸入錯誤")
    elif  a[2:] =="K" :
        field_total = 99
    else:
        b = a[2:]
        field_total = field_total + int(b)
        if field_total > 99 :
            print("你爆了 你輸了")

    if field_total > 99 :
        print("場上的牌總點數: ",field_total )
        break
    user_a = deck.pop()
    user_card.append(user_a)

    print("場上的牌總點數: ",field_total,"    你的手牌:",user_card)
    
    com_special = []
    for i in range(5):
        if com_card[i]=="黑桃A":
            com_special.append( com_card[i] )
        elif com_card[i][2:] in ["4", "5", "10", "J", "Q", "K"]:
            com_special.append( com_card[i] )
    if field_total>90 or len(com_special)==5:
        if len(com_special)!=0:
            a = com_special.pop()     # 場上點數>90 且 有特殊牌
            com_card.remove(a)
        else:
            a = com_card.pop()
    else:
        for i in range(5):
            if com_card[i] not in com_special:
                a = com_card.pop(i)
                break

    if a[:] == "黑桃A":
        field_total = 0 
        print("電腦出: ",a,"   場上的牌總點數: ", field_total)
    elif a[2:] == "A":
        field_total = field_total + 1
        if field_total > 99 :
            print("電腦出: ",a,"電腦爆了,你贏了") 
        else:
            print("電腦出: ",a,"   場上的牌總點數: ", field_total)
    elif a[2:] == "K":
        field_total = 99
        print("電腦出: ",a,"   場上的牌總點數: ", field_total)
    elif a[2:] == "10":
        field_total = field_total - 10
        print("電腦出: ",a,"   場上的牌總點數: ", field_total)
    elif a[2:] == "Q":
        field_total = field_total - 20
        print("電腦出: ",a,"   場上的牌總點數: ", field_total)
    elif a[2:] == "4" or a[2:] == "5" or a[2:] == "J" :
        print("電腦出: ",a,"   電腦pass","   場上的牌總點數: ", field_total)
    else :
        field_total = field_total + int(a[2:])
        if field_total > 99 :
            print("電腦出: ",a,"電腦爆了,你贏了") 
        else:
            print("電腦出: ",a,"   場上的牌總點數: ", field_total)

    cards_field.append(a)

    if field_total > 99:
        print("場上的牌總點數: ",field_total)
        print("電腦的牌: ", com_card)
        break
    com_c = deck.pop()
    com_card.append(com_c)

    if i%21==20:               # if len(deck)==0:
        deck = cards_field
        shuffle(deck)