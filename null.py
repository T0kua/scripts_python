import random
import os
karts = []
for i in range(40) :
	if i < 10 :
		karts.append(0)
	if i < 20 and i >= 10 :
		karts.append(1)
	if i < 30 and i >= 20:
		karts.append(2)
	if i >= 30 :
		karts.append(3)
random.shuffle(karts)
coldPC = karts[0:4]
score = 0
coldPL = karts[4:8]
game = True
while game:
	if len(coldPL) == 0 or len(coldPC) == 0 :
		print("nothing is win")
		game = False
		break
	print(f"{coldPL}                     score : {score}")
	x = int(input("enter kart number :"))
	if x in coldPL :
		for i in range(len(coldPL)) :
			if coldPL[i] == int(x) :
				score += coldPL[i]
				coldPL.pop(i)
				break
	else :
		print("error : kard is nothing")
		continue
	if score > 9 :
		print("you lose")
		game = False
		break
	print("PC make step...")
	if coldPC[0] + score > 9 :
		coldPC.sort()
		print(f"PC kard is {coldPC[0]}")
		score += coldPC[0]
		print(f"score :{score}")
		coldPC.pop(0)
	else :
		print(f"PC kard is {coldPC[0]}")
		score += coldPC[0]
		print(f"score :{score}")
		coldPC.pop(0)
	if score > 9 :
		print("you win")
		game = False
		break

os.system("pause")