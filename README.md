# Password Cracking Tool

This project is a Python-based tool for cracking passwords using brute-force and dictionary attacks. The tool demonstrates the security implications of weak passwords and is intended for educational purposes only.

## Features
- **Brute-force attack:** Attempts every possible combination of characters to crack the password.
- **Dictionary attack:** Uses a provided dictionary file containing a list of potential passwords.
- Configurable character sets for brute-force attacks.
- Measures the time and attempts taken to crack the password.

## Requirements
- Python 3.x

## Setup
1. Ensure Python 3.x is installed on your system.
2. Install any required dependencies (none are needed beyond the Python standard library).
3. Save the script as `password_cracker.py`.
4. (Optional) Create a dictionary file with potential passwords, e.g., `dictionary.txt`.

## Usage
1. Open a terminal and navigate to the directory containing `password_cracker.py`.
2. Run the script:
   ```bash
   python password_cracker.py
   ```
3. Follow the on-screen prompts:
   - Input the password to crack.
   - Select the attack method:
     - `1`: Brute-force attack
     - `2`: Dictionary attack
   - If using brute-force, select a character set:
     - Lowercase letters
     - Uppercase letters
     - Letters (both lowercase and uppercase)
     - Digits
     - Letters and digits
     - Letters, digits, and punctuation
     - All printable characters
   - If using a dictionary attack, provide the path to the dictionary file.

4. View the results, including the guessed password, number of attempts, and time taken.

## Example
### Brute-force Attack
Input:
```
Input the password to crack: abc
Choose the method for the attack:
1. Brute-force attack
2. Dictionary attack
Enter the number corresponding to your choice: 1
Choose the character set for the brute-force attack:
1. Lowercase letters
Enter the number corresponding to your choice: 1
```
Output:
```
Password cracked using 1 in 731 attempts and 0.34 seconds. The password is 'abc'.
```

### Dictionary Attack
Input:
```
Input the password to crack: password123
Choose the method for the attack:
1. Brute-force attack
2. Dictionary attack
Enter the number corresponding to your choice: 2
Enter the path to the dictionary file: dictionary.txt
```
Output:
```
Password cracked using 2 in 57 attempts and 0.01 seconds. The password is 'password123'.
```

## Notes
- Brute-force attacks can take a significant amount of time for complex passwords.
- Ensure the dictionary file is formatted with one password per line.
- Use responsibly and only for ethical and educational purposes. Unauthorized password cracking is illegal and unethical.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

# Password-Cracker
