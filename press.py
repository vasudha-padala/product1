import random
# print('snakes and ladders')
# print('enter no.of players')
# n=int(input())
ladders=[6,9,20,25,53,54,61]
ladders_score=[27,50,39,57,72,85,82]
#print (ladders)
snakes=[43,55,70,78,95,96]
snakes_score=[16,34,48,42,73,82]
#print(snakes)

#print(player1)
player1_score=0
player2_score=0
winner=100 
while 1 :
	dice=random.randint(1,6)
	print('dice value of player1 is:',dice)
	#player1_score=start(dice,player1_score)
	player1_score=player1_score+dice
	if player1_score in ladders:
		lindex=ladders.index(player1_score)
		print('-----',lindex)
		print('climbed')
		player1_score=player1_score+ladders_score[lindex]
		dice=random.randint(1,6)
		if dice==6:
			player1_score=climb(dice,player1_score)
			print('player1 promoted')
			print(player1_score)
	if player1_score in snakes:
		sindex=snakes.index(player1_score)
		print('!!!!',sindex)
		print('going down')
		player1_score=player1_score-snakes_score[sindex]
	print(player1_score)
	if player1_score>=100:
		print('player1 is winner')
		break
	#player 2 is started
	dice=random.randint(1,6)
	print('dice value of player2 is:',dice)
	#player2_score=start(dice,player2_score)
	player2_score=player2_score+dice
	if player2_score in ladders:
		lindex=ladders.index(player2_score)
		print('-----',lindex)
		print('climbed')
		player2_score=player2_score+ladders_score[lindex]
		dice=random.randint(1,6)
		if dice==6:
			player2_score=climb(dice,player2_score)
			print('player2 promoted')
			print(player2_score)
	if player2_score in snakes:
		sindex=snakes.index(player2_score)
		print('!!!!',sindex)
		print('going down')
		player2_score=player2_score-snakes_score[sindex]
	print(player2_score)
	if player2_score>=100:
	 	print('player2 is winner')
	 	break
def climb(dice,player_score):
	if dice==6:
		dice=random.randint(1,6)
		player_score=player_score+dice
		return(player_score)
#def start(dice,player_score):
	if dice==6:
		print('you are about to play') 
		dice=random.randint(1,6)
		player_score=player_score+dice
		if dice==6:
			initial(dice,player_score)
		else:
			print('chance is given to next player')
		return(player_score)

