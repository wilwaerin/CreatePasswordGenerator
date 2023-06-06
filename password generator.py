# Go to: https://replit.com/@appbrewery/password-generator-start?v=1

#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


password=[]

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))



for letter in range(0,(nr_letters)):
  a=(random.choice(letters))
  password.append(a)
else:
  pass

for symbol in range(0,(nr_symbols)):
  b=(random.choice(symbols))
  password.append(b)
  
else:
  pass

for numberr in range(0,(nr_numbers)):
  c=(random.choice(numbers))
  password.append(c)
else:
  pass

random.shuffle(password)

passw=""
for char in password:
    passw += char

print(f"Your password is: {passw}")

 
