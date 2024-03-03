
# # greeting = 'Hello'
# # name = 'Michael'

# # print(help(str.lower))

# import re

# message = 'Hello World i am pleased to see you'

# print(message.lower())

# print(message.upper())

# print(len(message))

# print(message.count('l'))


# print(message.find('to'))

# print(message.find('World'))

# message = message.replace('World', '      Universe')

# print(message.replace('World', 'Universe')) # temp

##IGNORE CASE using import re
# import re

# message = 'Hello World i am pleased to see you'
# old_substring = 'world'
# new_substring = 'universe'

# # Use re.IGNORECASE flag for case-insensitive matching
# result = re.sub(re.escape(old_substring), new_substring, message, flags=re.IGNORECASE)
# print(result)

#USING f STRING PLACE HOLDER

# greeting = 'Hello'
# name = " mike"

# message = '{}, {}. Welcome'.format(greeting, name)

# print(message)


name1 = input('Enter your name: ')
greet1= input('language to welcome: ')

# gmessage = '{} {}, My name is Jet'.format(greet1,name1)

# print(gmessage)


message2 = f'{greet1} {name1.upper()}!, My name is Pedro'

print(message2)

