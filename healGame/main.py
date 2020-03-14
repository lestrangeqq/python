#healerGame v0.1
import random    #импорт модуля для рандомного дамага

tank = 150
dps1 = 100
dps2 = 100
dps3 = 100
heal = 80
hoggerHp = 500
partyHp = tank + dps1 + dps2 + dps3 + heal

while hoggerHp > 0 and partyHp > 0:  #пока босс жив или все в пати живы цикл ходов будет продолжаться
	hoggerDmg = random.randrange(10, 30) #дамаг босса в диапазоне от 10 до 30
	tankDmg = random.randrange(3, 10)
	dps1Dmg = random.randrange(8, 13)
	dps2Dmg = random.randrange(4, 15)
	dps3Dmg = random.randrange(9, 10)

	if (hoggerHp > 0):
		hoggerHp -= tankDmg + dps1Dmg + dps2Dmg + dps3Dmg
		print ('Tank hits Hogger for: ' + str(tankDmg) + '\n' + 'DPS1 hits Hogger for: ' + str(dps1Dmg) + '\n' + 'DPS2 hits Hogger for: ' + str(dps2Dmg) + '\n' + 'DPS3 hits Hogger for: ' + str(dps3Dmg))
	
	if (tank > 0):  #босс наносит урон пати
		tank -= hoggerDmg
		print('Hogger hits the Tank for ' + str(hoggerDmg))
	elif (tank < 0 and dps1 > 0):
		dps1 -= hoggerDmg + 30
		print('Hogger crushes the Dps1 for ' + str(hoggerDmg))
	elif (tank < 0 and dps1 < 0 and dps2 > 0):
		dps2 -= hoggerDmg + 35
		print('Hogger crushes the Dps2 for ' + str(hoggerDmg))
	elif (tank < 0 and dps1 < 0 and dps2 < 0 and dps3 > 0):
		dps3 -= hoggerDmg + 40
		print('Hogger crushes the Dps3 for ' + str(hoggerDmg))
	else:
		heal -= hoggerDmg + 50
		print('Hogger shred the Heal for ' + str(hoggerDmg))
		
	#лог		
	print ('Hogger HP: ' + str(hoggerHp))
	print('| Tank HP: ' + str(tank) + '/150 | DPS 1 HP: ' + str(dps1) + '/100 | DPS 2 HP: ' + str(dps2) + '/100 | DPS 3 HP: ' + str(dps3) + '/100 | Healer HP: ' + str(heal) + '/80 |')
		
	turn = input('heal who? [T]ank, [H]eal, 1, 2 or 3 dps?: ') #хилим пати
	if (turn == 'T') or (turn == 't'):
		tank += 20 
		if (tank > 150): #remove overheal
			tank = 150
		print('Tank HP: ' + str(tank))
	elif (turn == 'H') or (turn == 'h'):
		heal += 20 
		if (heal > 80): #remove overheal
			heal = 80
		print('Heal HP: ' + str(heal))
	elif (turn == '1'):
		dps1 += 20 
		if (dps1 > 100): #remove overheal
			dps1 = 100
		print('DPS 1 HP: ' + str(dps1))
	elif (turn == '2'):
		dps2 += 20 
		if (dps2 > 100): #remove overheal
			dps2 = 100
		print('DPS 2 HP: ' + str(dps2))
	elif (turn == '3'):
		dps3 += 20 
		if (dps3 > 100): #remove overheal
			dps3 = 100
		print('DPS 3 HP: ' + str(dps3))
	else: 
		print('bad argument')

if (hoggerHp < 0 and partyHp > 0):
	print('You win!')
else:
	print('End')
