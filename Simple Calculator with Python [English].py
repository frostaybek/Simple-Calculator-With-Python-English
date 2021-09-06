def menu():
	print("""Menu
---------
1-Addition
2-Subtraction
3-Multiplication
4-Division
5-Exit""")

#Addition, Subtraction, Multiplication, Division and Exit.

def choicemade(selection):
	if selection == 1:
		print("Addition chosen")
		x=input("First number : ")
		y=input("Second number : ")
		total=int(x)+int(y)
		print(total)
		

	elif selection == 2:
		print("Subtraction chosen")
		x=input("First number : ")
		y=input("Second number : ")
		eject=int(x)-int(y)
		print(eject)

	elif selection == 3:
		print("multiplication chosen")
		x=input("First number : ")
		y=input("Second number : ")
		multiplication=int(x)*int(y)
		print(multiplication)

	elif selection == 4:
		print("chamber chosen")
		x=input("First number : ")
		y=input("Second number : ")
		divide =int(x)/int(y)
		print(divide)
		
	elif selection == 5:
	    print("Exit chosen")
	    pass
	    
	    
selection=0

while int(selection) != 5:
    menu()
    selection=input("Select your Chosen : ")
    choicemade(int(selection))
    
	    








    


    


