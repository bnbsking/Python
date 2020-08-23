import random

shape = ['s', 'h', 'd', 'c']
num = [str(i) for i in range(1,14)]
num[0] = 'A'; num[9]='t'; num[10] = 'J'; num[11] = 'Q'; num[12] = 'K';
deck = []
for i in range(len(shape)):
	for j in range(len(num)):
		deck.append(shape[i]+num[j])
random.shuffle(deck)
p1 = [deck.pop() for i in range(5)]
p2 = [deck.pop() for i in range(5)]
use = []

def isSpecial(x):
	if x=="sA" or x[1] in ['t','J','Q','K']:
		return True
	return False

def play(x, score):
	if isSpecial(x):
		if x=="sA":
			return 0
		elif x[1]=="t":
			if score>=90:
				return score-10
			elif score<10:
				return score+10
			while True:
				t = input("+10 or -10 (+/-): ")
				if t=="+":
					return score+10
				elif t=="-":
					return score-10
				print("-"*10, "\nT-Error !!!\n", "-"*10)
		elif x[1]=="J":
			return score	
		elif x[1]=="Q":
			if score>=80:
				return score-20
			elif score<20:
				return score+20
			while True:
				t = input("+20 or -20 (+/-): ")
				if t=="+":
					return score+20
				elif t=="-":
					return score-20
				print("-"*10, "\nQ-Error !!!\n", "-"*10)
		else:
			return 99
	else:
		return score+1 if x[1]=="A" else score+int(x[1])

score = 0
while True:
	available = []
	for i in range(5):
		if isSpecial(p1[i]):
			available.append(i)		
		else:
			if p1[i][1]=="A":
				if score<99:
					available.append(i)
			elif score+int(p1[i][1])<99:
				available.append(i)
	if len(available)==0:
		print("\np1 = {} \nYOULOSE".format(p1))
		break
	while True:
		print("\nscore = {} \np1 = {}".format(score, p1))
		x = input("Enter a card 0~4: ")
		try:
			if 0<=int(x)<=4:
				if int(x) in available:
					print("play: ", p1[int(x)])
					score = play(p1[int(x)], score)
					use.append(p1[int(x)])
					if len(deck)==0:	
						deck, use = use, deck
					p1[int(x)] = deck.pop()		
					break
				print("-"*10, "\nOverFlow !!!\n", "-"*10)
			else:
				print("-"*10, "\nNot 0~4 number !!!\n", "-"*10)
		except:
			print("-"*10, "\nNot integer !!!\n", "-"*10)
		
	
