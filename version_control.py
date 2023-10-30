def menu():
    print('Menu')
    print('-------------')
    print('1. Encode \n2. Decode \n3. Quit \n')


while True:
    menu()
    user_option = int(input('Please enter an option: '))

    if user_option == 1:
        password = input('Please enter your password to encode: ')
        print('Your password has been encoded and stored!')
        encoded_password = ''

        for char in password:
            if 0 <= int(char) <= 6:
                encoded_password += str(3 + int(char))
            elif int(char) >= 7:
                new_char = (int(char) + 3) % 10
                encoded_password += str(new_char)

    elif user_option == 2:
        print(f"The encoded password is {encoded_password}, and the original password is {password}.")

    elif user_option == 3:
        break

