import pygame

# This function adds two numbers 
def add(x, y):
	f = open("/home/pi/Desktop/final_year_project/calculator/result.txt","w" )
	f.write(str(x) + " plus " + str(y) + " \n")
	res = x+y
	f.write(" equals \n")
	f.write(str(res))
	f.write("\nn Program complete \n")
	f.close()
	return x + y

# This function subtracts two numbers 
def subtract(x, y):
	f = open("/home/pi/Desktop/final_year_project/calculator/result.txt","w" )
	f.write(str(x) + " subtracted with " + str(y) + " \n")
	res = x-y
	f.write(" equals \n")
	f.write(str(res))
	f.write("\nn Program complete \n")
	f.close()
	return x - y

# This function multiplies two numbers
def multiply(x, y):
	f = open("/home/pi/Desktop/final_year_project/calculator/result.txt","w" )
	f.write(str(x) + " multiplied with " + str(y) + " \n")
	res = x*y
	f.write(" equals \n")
	f.write(str(res))
	f.write("\nn Program complete \n")
	f.close()
	return x * y

# This function divides two numbers
def divide(x, y):
	f = open("/home/pi/Desktop/final_year_project/calculator/result.txt","w" )
	f.write(str(x) + " divided " + str(y) + " \n")
	res = x/y
	f.write(" equals \n")
	f.write(str(res))
	f.write("\nn Program complete \n")
	f.close()
	return x / y


pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/cal_welcome.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue

print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")

# Take input from the user 
choice = input("Enter choice(1/2/3/4): ")


if choice == '1':
	pygame.mixer.init()
	pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/add.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	#print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
	pygame.mixer.init()
	pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/subtraction.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	#print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
	pygame.mixer.init()
	pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/multiplication.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	#print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
	pygame.mixer.init()
	pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/Division.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	#print(num1,"/",num2,"=", divide(num1,num2))
else:
	pygame.mixer.init()
	pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/cal_invalid.mp3")
	pygame.mixer.music.play()
	while pygame.mixer.music.get_busy() == True:
		continue
	#print("Invalid input")
	exit(0)


pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/first_num.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
num1 = float(input("Enter first number: "))


pygame.mixer.init()
pygame.mixer.music.load("/home/pi/Desktop/final_year_project/extravoices/second_num.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy() == True:
    continue
num2 = float(input("Enter second number: "))

if choice == '1':
	print(num1,"+",num2,"=", add(num1,num2))

elif choice == '2':
	print(num1,"-",num2,"=", subtract(num1,num2))

elif choice == '3':
	print(num1,"*",num2,"=", multiply(num1,num2))

elif choice == '4':
	print(num1,"/",num2,"=", divide(num1,num2))
else:
	print("Invalid input")
