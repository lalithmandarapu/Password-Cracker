import itertools
import string
import time

def bruteforce_attack(password, charset):
    attempts = 0
    start_time = time.time()
    for length in range(1, len(password) + 1):
        for guess in itertools.product(charset, repeat=length):
            attempts += 1
            guess = ''.join(guess)
            if guess == password:
                end_time = time.time()
                duration = end_time - start_time
                return (attempts, guess, duration)
    end_time = time.time()
    duration = end_time - start_time
    return (attempts, None, duration)

def dictionary_attack(password, dictionary):
    attempts = 0
    start_time = time.time()
    for word in dictionary:
        attempts += 1
        if word == password:
            end_time = time.time()
            duration = end_time - start_time
            return (attempts, word, duration)
    end_time = time.time()
    duration = end_time - start_time
    return (attempts, None, duration)

def get_charset(choice):
    if choice == '1':
        return string.ascii_lowercase
    elif choice == '2':
        return string.ascii_uppercase
    elif choice == '3':
        return string.ascii_letters
    elif choice == '4':
        return string.digits
    elif choice == '5':
        return string.ascii_letters + string.digits
    elif choice == '6':
        return string.ascii_letters + string.digits + string.punctuation
    else:
        return string.printable.strip()

def main():
    password = input("Input the password to crack: ")

    print("Choose the method for the attack:")
    print("1. Brute-force attack")
    print("2. Dictionary attack")
    method_choice = input("Enter the number corresponding to your choice: ")

    if method_choice == '1':
        print("Choose the character set for the brute-force attack:")
        print("1. Lowercase letters")
        print("2. Uppercase letters")
        print("3. Letters (both lowercase and uppercase)")
        print("4. Digits")
        print("5. Letters and digits")
        print("6. Letters, digits, and punctuation")
        print("7. All printable characters")
        charset_choice = input("Enter the number corresponding to your choice: ")
        charset = get_charset(charset_choice)
        attempts, guess, duration = bruteforce_attack(password, charset)
    elif method_choice == '2':
        dictionary_file = input("Enter the path to the dictionary file: ")
        with open(dictionary_file, 'r') as file:
            dictionary = [line.strip() for line in file]
        attempts, guess, duration = dictionary_attack(password, dictionary)
    else:
        print("Invalid choice.")
        return

    if guess:
        print(f"Password cracked using {method_choice} in {attempts} attempts and {duration:.2f} seconds. The password is '{guess}'.")
    else:
        print(f"Password not cracked using {method_choice} after {attempts} attempts and {duration:.2f} seconds.")

if __name__ == "__main__":
    main()
        