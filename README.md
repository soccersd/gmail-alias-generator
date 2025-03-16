# Gmail Alias Generator

A simple Python script that generates Gmail aliases by adding a '+suffix' after your Gmail username.

## What are Gmail Aliases?

Gmail allows you to create aliases of your email address by adding a plus sign (+) followed by any text before the @ symbol. For example, if your email is `username@gmail.com`, you can use `username+anything@gmail.com` as an alias.

All emails sent to these aliases will still arrive in your main Gmail inbox, but you can create filters based on the "To:" address to automatically sort, label, or manage these emails differently.

## Features

- Generate any number of unique Gmail aliases
- Each alias has a random suffix (a letter followed by a number)
- View all generated aliases in the terminal
- Option to save aliases to a text file for future reference

## Requirements

- Python 3.6 or higher

## How to Use

1. Run the script:
   ```
   python gmail_alias_generator.py
   ```

2. Enter your main Gmail address when prompted
   ```
   Enter your main Gmail address: youremail@gmail.com
   ```

3. Enter the number of aliases you want to generate
   ```
   How many aliases would you like to generate? 10
   ```

4. The script will display all generated aliases
   ```
   Generated Gmail Aliases:
   =======================
   1. youremail+a1@gmail.com
   2. youremail+b5@gmail.com
   ...
   ```

5. Choose whether to save the aliases to a text file
   ```
   Do you want to save these aliases to a text file? (y/n): y
   ```

6. If you choose yes, the aliases will be saved to `gmail_aliases.txt` in the current directory

## Benefits of Using Gmail Aliases

- **Track who shares your email**: Use a different alias for each website or service
- **Filter your inbox**: Create Gmail filters based on the alias to automatically organize emails
- **Reduce spam**: If an alias starts receiving spam, you know which service leaked your email
- **Test email functionality**: Useful for developers testing email features
- **Create multiple accounts**: Some services allow you to register multiple accounts with different email addresses

## How It Works

The script generates random suffixes consisting of a lowercase letter followed by a number between 1 and 99. This provides up to 2,574 unique combinations (26 letters × 99 numbers).

## Note

Gmail ignores everything after the plus sign (+) when delivering emails, so all emails sent to your aliases will still arrive in your main inbox. The alias part is only useful for filtering and organization. 