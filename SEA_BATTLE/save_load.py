def make_save(field_1_1, field_1_2, field_2_1, field_2_2):
	with open(file="save.txt", mode="w") as f:
		for i in field_1_1:
			for j in i:
				f.write(str(j) + " ")
			f.write("\n")
		for i in field_1_2:
			for j in i:
				f.write(str(j) + " ")
			f.write("\n")

		for i in field_2_1:
			for j in i:
				f.write(str(j) + " ")
			f.write("\n")

		for i in field_2_2:
			for j in i:
				f.write(str(j) + " ")
			f.write("\n") 


def read_save():
	with open(file="save.txt", mode="r", encoding="utf-8")  as f:
		field_1_1 = []
		field_1_2 = []
		field_2_1 = []
		field_2_2 = []
		for i in range(12):
			line = f.readline().strip()
			line = list(map(int, line.split()))
			field_1_1.append(line)
		for i in range(12):
			line = f.readline().strip()
			line = list(map(int, line.split()))
			field_1_2.append(line)
		for i in range(12):
			line = f.readline().strip()
			line = list(map(int, line.split()))
			field_2_1.append(line)
		for i in range(12):
			line = f.readline().strip()
			line = list(map(int, line.split()))
			field_2_2.append(line)
	return field_1_1, field_1_2, field_2_1, field_2_2
