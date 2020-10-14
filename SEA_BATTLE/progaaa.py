import save_load 

field_1_1 =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	    	[0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0],
	    	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	    	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	    	[0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0],
	    	[0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
	    	[0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
	    	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
	    	[0, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1, 0],
	    	[0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
	    	[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

field_1_2 =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

field_2_1 =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
	 		[0, 0, 0, 0, 1, 0, 0, 1, 1, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 1, 0],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
			[0, 0, 1, 0, 1, 1, 1, 0, 0, 0, 0, 0],
			[0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],]

field_2_2 =[[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
  			[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]


def fields_output_1(field_1_1, field_1_2):
	print("    1 2 3 4 5 6 7 8 9 10       1 2 3 4 5 6 7 8 9 10")
	print("   ---------------------      ---------------------")
	for i in range(1, 11):
		letter = chr(ord("A") + i - 1)
		print(letter + " |",*field_1_1[i][1:11], "   " + letter + " |", *field_1_2[i][1:11])

def fields_output_2(field_2_1, field_2_2):
	print("")
	print("    1 2 3 4 5 6 7 8 9 10       1 2 3 4 5 6 7 8 9 10")
	print("   ---------------------      ---------------------")
	for i in range(1, 11):
		letter = chr(ord("A") + i - 1)
		print(letter + " |",*field_2_1[i][1:11], "   " + letter + " |", *field_2_2[i][1:11])

def coord_input():
	while(True):
		let_coord = input()      #ввод координат с буквой
		if (len(let_coord) <= 3) and (let_coord[1::].isdigit()):
			x = ord(let_coord[0]) - ord("A") + 1
			y = int(let_coord[1::])
			if(1 <= x <= 10) and (1 <= y <= 10):
				return [x, y]
				break
			print("Ошибка: Ваши координаты выходят за пределы поля боя")
		print("Введите координаты правильно! (Заглавная латинская буква и число слитно)")


k_1 = 0
k_2 = 0

field_1_1, field_1_2, field_2_1, field_2_2 = save_load.read_save()
while k_2 != 18 and k_1 != 18:
	game_1 = False
	while game_1 == False:  #ходит 1 игрок
		fields_output_1(field_1_1, field_1_2)
		print("Ход 1-го игрока: ")
		coord = coord_input()
		i = coord[0]
		j = coord[1]
		if field_2_1[i][j] == 1:
			field_2_1[i][j] = 8
			field_1_2[i][j] = 8
			field_2_1[i - 1][j - 1] = 7
			field_1_2[i - 1][j - 1] = 7
			field_2_1[i + 1][j - 1] = 7
			field_1_2[i + 1][j - 1] = 7
			field_2_1[i - 1][j + 1] = 7
			field_1_2[i - 1][j + 1] = 7
			field_2_1[i + 1][j + 1] = 7
			field_1_2[i + 1][j + 1] = 7
			k_1 += 1
			if field_2_1[i - 1][j - 1] == 1 or field_2_1[i - 1][j + 1] == 1 or field_2_1[i + 1][j - 1] == 1 or field_2_1[i + 1][j + 1] == 1:
				print("Вы попали в корабль, сделайте еще ход")
			else:
				print("Вы уничтожили корабль, так держать!")
		else:
			print("Промах!")
			field_2_1[i][j] = 7
			game_1 = True

	save_load.make_save(field_1_1, field_1_2, field_2_1, field_2_2)		


	game_2 = False
	while game_2 == False:   #ходит 2 игрок

		fields_output_2(field_2_1, field_2_2)	
		print("Ход 2-го игрока: ")
		coord = coord_input()
		i = coord[0]
		j = coord[1]

		if field_1_1[i][j] == 1:
			field_1_1[i][j] = 8
			field_2_2[i][j] = 8
			field_1_1[i - 1][j - 1] = 7
			field_2_2[i - 1][j - 1] = 7
			field_1_1[i + 1][j - 1] = 7
			field_2_2[i + 1][j - 1] = 7
			field_1_1[i - 1][j + 1] = 7
			field_2_2[i - 1][j + 1] = 7
			field_1_1[i + 1][j + 1] = 7
			field_2_2[i + 1][j + 1] = 7
			k_2 += 1
			if field_1_1[i - 1][j - 1] == 1 or field_1_1[i - 1][j + 1] == 1 or field_1_1[i + 1][j - 1] == 1 or field_1_1[i + 1][j + 1] == 1:
				print("Вы попали в корабль , сделайте еще ход")
			else:
				print("Вы уничтожили корабль,так держать!")
		else:
			print("Промах!")
			field_2_1[i][j] = 7
			game_2 = True
	save_load.make_save(field_1_1, field_1_2, field_2_1, field_2_2)

if k_1 == 18:
	print("Игрок 1 Выиграл!")
if k_2 == 18:
	print("Игрок 2 Выиграл!")	