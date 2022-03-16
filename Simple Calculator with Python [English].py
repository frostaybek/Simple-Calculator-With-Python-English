import turtle
import time

def menu():
	print("""
Ayaz Aybek production
	
-----------
1-Addition
2-Substraction
3-Multiplication
4-Division
5-Exit
-----------
""")

#Addition, Subtraction, Multiplication, Division and Exit.

def makechoice(choice):
	if choice == 1:
		print("""
ADDITION SELECTED
""")
		x=input("First Number : ")
		y=input("Second Number : ")
		add=int(x)+int(y)
		print(add)
		time.sleep(0.1)
		
	elif choice == 2:
		print("""
SUBSTRACTION SELECTED
""")
		x=input("First Number : ")
		y=input("Second Number : ")
		sub=int(x)-int(y)
		print(sub)
		time.sleep(0.1)

	elif choice == 3:
		print("""
MULTIPLICATION SELECTED
""")
		x=input("First Number : ")
		y=input("Second Number : ")
		multi=int(x)*int(y)
		print(multi)
		time.sleep(0.1)

	elif choice == 4:
		print("""
DIVISION SELECTED
""")
		x=input("First Number : ")
		y=input("Second Number : ")
		div=int(x)/int(y)
		print(div)
		time.sleep(0.1)
		
	elif choice == 5:
	    print("EXIT SELECTED, GOODBYE :)")
	time.sleep(1.2)
	pass

	    
choice=0

while int(choice) != 5:
    menu()
    choice=input("Make your choice : ")
    makechoice(int(choice))