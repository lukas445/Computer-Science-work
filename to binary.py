# [program name]
# Lukas Delicata
# [date]
# OCR AS Computer Science

def number():
    user_inp = int(input('Please enter a number between 0 and 255: '))
    if user_inp >= 256:
        print('This number is over 255. Try again.')
        number()
    elif user_inp <= -1:
        print('This number is below 0. Try again.')
        number()
    else:
        binary = bin(user_inp)[2:]
        print(binary)

number()
