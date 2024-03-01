import re

with open(r'C:\Users\herncrz\VSCODE\code_snippets\Python-Regular-Expressions\data.txt') as f:
    readme1= f.read()

    #ADDRESS
    pattern3 = re.compile(r'[0-9]+\s+')

    match3 = pattern3.finditer(readme1)

    for matched in match3:
        print(matched)

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
    

