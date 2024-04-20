logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""


print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(msg,shift,choice):
    new_msg = ""
    if choice == "decode":
        shift = shift * (-1)
    for char in msg:
        if char in alphabet:
            position = alphabet.index(char)
            new_position = position + shift
            new_msg += alphabet[new_position]
        else:
            new_msg+=char 
    print(f"Here's the {choice}d result: {new_msg}")


stop = False
while not stop:
    choice = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    msg= input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(msg=msg,shift=shift,choice=choice)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if restart == "no":
        stop = True
        print("Goodbye")
        




'''
The above Ceasar function can also be written in 2 different functions as follows

def encrypt(msg,shift):
    coded = ""
    for char in msg:
        position = alphabet.index(char)
        new_position = position+shift
        new_msg=alphabet[new_position]
    else:
        new_msg+=char
    print(f"The encoded text is {coded}")


def decrypt(msg,shift):
    decoded = ""
    for char in msg:
        position = alphabet.index(cahr)
        new_position = position-shift
        new_msg+=alphabet[new_position]
    else:
        new_msg = char
    print(f"The decoded text is {decoded}")




if choice == "encode":
    encrypt(msg=msg,shift=shift)

if choice == "decode":
    decrypt(msg=msg,shift=shift )


    '''
