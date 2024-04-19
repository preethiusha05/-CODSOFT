import random

def main():
    length = int(input("Enter the total length of the password: "))
    num_uppercase = int(input("Enter the number of uppercase letters: "))
    num_lowercase = int(input("Enter the number of lowercase letters: "))
    num_symbols = int(input("Enter the number of symbols: "))
    num_digits = int(input("Enter the number of digits: "))

    
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    symbols = "@#!$%&*^{}[]"
    digits = "1234567890"

    
    all_characters = []

    
    all_characters.extend(random.sample(upper_case, num_uppercase))
    all_characters.extend(random.sample(lower_case, num_lowercase))
    all_characters.extend(random.sample(symbols, num_symbols))
    all_characters.extend(random.sample(digits, num_digits))

    
    remaining_length = length - (num_uppercase + num_lowercase + num_symbols + num_digits)
    all_characters.extend(random.choices(upper_case + lower_case + symbols + digits, k=remaining_length))


    random.shuffle(all_characters)

    
    password = ''.join(all_characters)

    
    print("Generated Password:", password)


if __name__ == "__main__":
    main()
