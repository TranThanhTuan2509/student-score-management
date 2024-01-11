class Student:
	def __init__(self, id, name, gender,age,Math_score,Physic_score,Chemistry_score):
		self.id = id
		self.name = name
		self.gender = gender
		self.age = age
		self.Math_score = Math_score
		self.Physic_score = Physic_score
		self.Chemistry_score = Chemistry_score
		self.Average = round((Math_score+Physic_score+Chemistry_score) / 3,1)
		self.hocLuc = ""

class In4:
	def __init__(self,Information):
		self.Information = Information
		self.next = None

class Management:
	def __init__(self):
		self.head = None
		self.archive = {}
		self.Name = []

	def Push(self,data):
		New_node = In4(data)
		if self.head != None:
			New_node.next = self.head
		self.head = New_node

	def Search(self,a,name):
		if self.head.Information == name:
			return print(a[name][0])
		else:
			temp = self.head
			while temp != None:
				if temp.Information == name:
					return	print(a[name][0])
				temp = temp.next
			return print('Your name you need is not exist')
		
	def Search_each_subject(self,a,name,choice):
		if self.head.Information == name:
			if choice == 2:
				return print(a[name][1])
			elif choice == 3:
				return print(a[name][2])
			else:
				return print(a[name][3])
		else:
			temp = self.head
			while temp != None:
				if temp.Information == name:
					if choice == 2:
						return print(a[name][1])
					elif choice == 3:
						return print(a[name][2])
					else:
						return print(a[name][3])
					
				temp = temp.next
			return print('Your name you need is not exist')

	def show_menu(self):
		print("Main Menu:")
		print("----------------------------------------")
		print("| Option 1: Create Student Information |")
		print("| Option 2: Show Math Score   		  |")
		print("| Option 3: Show Physic Score          |")
		print("| Option 4: Show Chemistry Score       |")
		print("| Option 5: Show Student Information   |")
		print("| Option 6: Exit                       |")
		print("----------------------------------------")

	def select_name(self,prompt):
		name = input(prompt)
		name = name.title()
		return name
		
		
	
	def select_in_range(self,prompt):
		choice = input(prompt)
		while not choice.isnumeric() or (int(choice) > 6) or (int(choice) < 1):
			choice = input(prompt)
		choice = int(choice)
		return choice

	def Enter_Student_Information(self):
		
		n = int(input("Nhap so sv: "))
		for i in range(n): 
			id= int(input("Nhap id cua sinh vien: "))
			name = input("Nhap ten sinh vien: ")
			name = name.title()
			gender = input("Nhap gioi tinh sinh vien: ")
			age = int(input("Nhap tuoi sinh vien: "))
			Math_score = float(input("Nhap diem toan: "))
			Physic_score = float(input("Nhap diem Ly: "))
			Chemistry_score = float(input("Nhap diem Hoa: "))
			student = Student(id, name, gender, age, Math_score,Physic_score,Chemistry_score)
			value = f'Sinh vien co MSV {student.id} co ten la {student.name} gioi tinh {student.gender} tuoi {student.age} co diem toan {student.Math_score}, diem li {student.Physic_score}, diem hoa {student.Chemistry_score} '
			self.archive.update({name:(value , Math_score , Physic_score , Chemistry_score)})
			self.Name.append(name)

		self.Name.sort(key = lambda x : (x.split()[-1], x.split()[0], x.split()[1]))
		for i in range(len(self.Name)):
			self.Push(self.Name[-(i+1)])

		return self.archive
	
if __name__ == "__main__":
	
	management = Management()
	while True:
		management.show_menu()
		choice = management.select_in_range("Choose your option (1 -> 6): ")
		if choice == 1:
			management.Enter_Student_Information()
		if choice == 2:
			management.Search_each_subject(management.archive,management.select_name("Student's name you want to show: "),2)
		if choice == 3:
			management.Search_each_subject(management.archive,management.select_name("Student's name you want to show: "),3)
		if choice == 4:
			management.Search_each_subject(management.archive,management.select_name("Student's name you want to show: "),4)
		if choice == 5:
			management.Search(management.archive,management.select_name("Student's name you want to show: "))
		if choice == 6:
			break
	

	

	