import random
import string

def generate_password(length):
    # Define character sets
    letters = string.ascii_letters
    digits = string.digits
    special_characters = string.punctuation

    # Combine all character sets
    all_characters = letters + digits + special_characters

    # Generate password
    password = ''.join(random.choice(all_characters) for _ in range(length))
    return password
def main():
    try:
        # Take input from user for password length
        length = int(input("Enter the length of the password: "))
        
        # Check if length is valid
        if length <= 0:
            print("Password length should be greater than zero.")
            return
        
        # Generate password
        password = generate_password(length)
        
        # Print password
        print("Generated Password:", password)
        
    except ValueError:
        print("Invalid input. Please enter a valid number for password length.")
if __name__ == "__main__":
    main()

letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

numbers = ['1','2','3','4','5','6','7','8','9']
special_character = ['!','@','#','$','%','^','&','*','(',')']

#take the input from user
number_char = int(input("enter the number of letter do you want: "))
number_num = int(input("enter the numbers of number do you want: "))
number_special = int(input("enter the number of special character do you want: "))
#add in password
password =" "
strong_password =" "
for char in range(1, number_char+1):
    password += random.choice(letters)
for char in range(1, number_num+1):
    password += random.choice(numbers)
for char in range(1, number_special+1):
    password += random.choice(special_character)

for char in range(1,len(password)):
    strong_password +=random.choice(password)
 
print(password)
print(strong_password)

