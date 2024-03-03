# import re

# with open(r'C:\Users\herncrz\VSCODE\code_snippets\Python-Regular-Expressions\data.txt') as f:
#     readme1= f.read()


#     #MATCH NAME and PHONE#

#     pattern51 = re.compile(r'^[a-zA-Z]+\s[a-zA-Z]+$')
#     pattern52 = re.compile(r'[\d\d\d]+[-][\d\d\d]+[-][\d\d\d\d]+')

#     match51 = pattern51.finditer(readme1)
#     match52 = pattern52.finditer(readme1)

#     if pattern51:
#         print("Name:", match51.group(1))
#     else:
#         print("Name not found")


    

import re

with open(r'/home/jet/VSCODE_SYNC/code_snippets/Regular-Expressions/data.txt') as f:
    data = f.read()

# Regular expression patterns for name and phone number
name_pattern = re.compile(r'^[a-zA-Z]+\s[a-zA-Z]+$', re.MULTILINE)
phone_pattern = re.compile(r'\b\d{3}-\d{3}-\d{4}\b')

# Find all occurrences of name and phone number using finditer
name_matches = name_pattern.finditer(data)
phone_matches = phone_pattern.finditer(data)

# Zip name and phone number matches together
for name_match, phone_match in zip(name_matches, phone_matches):
    print("Name:", name_match.group())
    print("Phone Number:", phone_match.group())
    print()  # Adding an empty line for readability



    

    # #EMAIL

    # pattern4 = re.compile(r'[a-z]+[@][a-z]+[.com]+')

    # match4 = pattern4.finditer(readme1)

    # for matched in match4:
    #     print(matched)

    # #ADDRESS
    # pattern3 = re.compile(r'[0-9]+\s[a-zA-Z]+\s[St.,]+\s[a-zA-Z]+\s[A-Z]+\s[0-9]+')

    # match3 = pattern3.finditer(readme1)

    # for matched in match3:
    #     print(matched)

    # #PHONE NUMBERS
    # pattern2 = re.compile(r'[0-9]+[-][0-9]+[-][0-9]+')

    # match2 = pattern2.finditer(readme1)

    # for match in match2:
    #     print(match)



    ##GET all3 digits

    # pattern1 = re.compile(r'[\d\d\d]+')

    # matched = pattern1.finditer(readme1)

    # for match in matched:
    #     print(match)
    

