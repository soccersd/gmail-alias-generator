

import os
import random
import string

def generate_gmail_aliases(main_email, count):
    """Generate Gmail aliases by adding '+something' after the username part."""
    if '@' not in main_email or not main_email.endswith('@gmail.com'):
        print("Error: Please enter a valid Gmail address.")
        return []
    
    username = main_email.split('@')[0]
    domain = main_email.split('@')[1]
    
    aliases = []
    for i in range(count):
        
        suffix = random.choice(string.ascii_lowercase) + str(random.randint(1, 99))
        alias = f"{username}+{suffix}@{domain}"
        aliases.append(alias)
    
    return aliases

def main():
    print("Gmail Alias Generator")
    print("=====================")
    
    
    main_email = input("Enter your main Gmail address: ")
    
    try:
        count = int(input("How many aliases would you like to generate? "))
        if count <= 0:
            print("Please enter a positive number.")
            return
    except ValueError:
        print("Please enter a valid number.")
        return
    
    
    aliases = generate_gmail_aliases(main_email, count)
    
    if not aliases:
        return
    
    
    print("\nGenerated Gmail Aliases:")
    print("=======================")
    for i, alias in enumerate(aliases, 1):
        print(f"{i}. {alias}")
    
    
    save_to_file = input("\nDo you want to save these aliases to a text file? (y/n): ").lower()
    
    if save_to_file == 'y' or save_to_file == 'yes':
        filename = "gmail_aliases.txt"
        with open(filename, 'w') as file:
            file.write(f"Main email: {main_email}\n")
            file.write(f"Generated aliases ({count}):\n")
            for i, alias in enumerate(aliases, 1):
                file.write(f"{i}. {alias}\n")
        
        print(f"\nAliases saved to {os.path.abspath(filename)}")

if __name__ == "__main__":
    main() 