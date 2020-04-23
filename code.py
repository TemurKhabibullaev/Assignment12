# 4/21/2020 Temur Khabibullaev
import re


def definer(string):
    choice = int(input(""
                       "1.See if the string has a 'q'\n"
                       "2.See if the string contains 'the'\n"
                       "3.See if the string has a '*' in it\n"
                       "4.See if the string contains a digit\n"
                       "5.See if the string contains a period\n"
                       "6.See if the string has at least 2 consecutive vowels (a,e,i,o,u)\n"
                       "7.See if the string contains white space\n"
                       "8.See if the string has any letters that repeat three times in a single word\n"
                       "9.See if the string starts with the word ‘Hello’ (must match the capital H)\n"
                       "10.See if the string contains an email address\n"
                       "11.Exit\n>>>"))
    # Find "q" letter
    if choice == 1:
        if re.search(r"q", string):
            return "Yes! It contains a 'q' letter"
        else:
            return 'No. It does not contain a "q" letter'
    # Find out if string has "the" word
    if choice == 2:
        if re.search(r'the', string):
            return "Yes! It contains 'the' word"
        else:
            return 'No! It does not contain "the" word'
    # Find * symbol
    if choice == 3:
        if re.search(r'[*]', string):
            return "Yes! It contains a star symbol"
        else:
            return 'There is no star symbol'
    # Find any digits
    if choice == 4:
        if re.search(r'[0-9]', string):
            return "Yes! It contains digits"
        else:
            return 'There is no digits'
    # Find . in string
    if choice == 5:
        if re.search(r'[.]', string):
            return "Yes! It contains a period"
        else:
            return 'No. It does not contain a period'
    # Consecutive letters "aeiou" finder
    if choice == 6:
        if re.search(r'[aeiou]{2}', string):
            return "Yes!"
        else:
            return "No"
    # White space finder
    if choice == 7:
        if re.search(r'[\s]', string):
            return "Yes! There is a white space"
        else:
            return 'No.There is no white space'
    # I gave up on this one
    if choice == 8:
        print("This option is not yet available")
    # Finds only if string starts with "Hello"
    if choice == 9:
        if re.search(r'^Hello', string):
            return "Yes! It starts with 'Hello'"
        else:
            return 'No. It does not start with "Hello"'
    # Email @ pattern finder
    if choice == 10:
        if re.findall(r'\w+@\w+\.\w+', string):
            return "Yes! This is an email."
        else:
            return 'No. This is not an email'
    if choice == 11:
        return None


string = str(input('\n>>>'))
option = None

while option != 0:
    temporary = definer(string)
    print(temporary)
    
    if temporary == None:
        break
