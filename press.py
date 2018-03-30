import random
# print('snakes and ladders')
# print('enter no.of players')
# n=int(input())
ladders=[1,2,3,4,5,6]
ladders_score=[10,20,30,40,50,60]
#print (ladders)

#print(snakes)

#print(player1)
player1_score=0
player2_score=0
winner=100 
while 1 :
	dice=random.randint(1,6)
	print('dice value is:',dice)
	player1_score=player1_score+dice
	if player1_score in ladders:
		pindex=ladders.index(player1_score)
		print('-----',pindex)
		print('climbed')
		player1_score=player1_score+ladders_score[pindex]
		dice=random.randint(1,6)
		if dice==6:
			promoted_value=dice(dice,player1_score)
			print('player1 promoted')
			print(promoted_value)
	print(player1_score)
	if player1_score>=100:
		print('player1 is winner')
		break
	# dice=random.randint(1,6)
	# player2_score=player2_score+dice
	# print(player2_score)
	# if player2_score>=100:
	# 	print('player2 is winner')
	# 	break
def dice(dice,player1_score):
	if dice==6:
		dice=random.randint(1,6)
		score=score+dice
		return(score)

