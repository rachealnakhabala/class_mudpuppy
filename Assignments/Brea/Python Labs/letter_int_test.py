#letter_int.py, figuring out how to call an 
import string

user_input = input("Give me a letter or number: ")

if user_input.isdigit():
    user_input = int(user_input)
    print('abcdefghijklmnopqrstuvwxyz'[user_input])
else:
    print('abcdefghijklmnopqrstuvwxyz'.index(user_input))