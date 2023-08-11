import string
import getpass

def check_password_strength():

    print("*** Your password is invisible to hide it from another, so just type your password and press enter ***")
    password = getpass.getpass('Enter the password: ')
    strength = 0
    feedback = ''
    lower_count = upper_count = num_count = space_count = special_count = 0

    for char in list(password):
        if char in string.ascii_lowercase:
            lower_count += 1
        elif char in string.ascii_uppercase:
            upper_count += 1
        elif char in string.digits:
            num_count += 1
        elif char == ' ':
            wspace_count += 1
        else:
            special_count += 1

    if lower_count >= 1:
        strength += 1
    if upper_count >= 1:
        strength += 1
    if num_count >= 1:
        strength += 1
    if space_count >= 1:
        strength += 1
    if special_count >= 1:
        strength += 1

    if strength == 1:
        feedback = ("That's a very bad password. Change it as soon as possible.")
    elif strength == 2:
        feedback = ("That\'s a weak password. You should consider using a tougher password.")
    elif strength == 3:
        feedback = "Your password is okay, but it can be improved."
    elif strength == 4:
        feedback = ("Your password is hard to guess. But you could make it even more secure.")
    elif strength == 5:
        feedback = ("Now that's a damn strong password! Hackers don't have any chance to guess this password!")

    print("Your password has:-")
    print(f"\tlowercase letters:- {lower_count}")
    print(f"\tuppercase letters:- {upper_count}")
    print(f"\tdigits:- {num_count}")
    print(f"\twhitespaces:- {space_count}")
    print(f"\tspecial characters:- {special_count}")
    print(f"\tPassword Rating:- {strength} / 5")
    print(f"\tFeedback:- {feedback}")

def check_pwd():
    while True:
        choice = input("Do you want to check your password's strength (y/n) : ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid input...please try again. \n')
    
def check_another_pwd():
    while True:
        choice = input("Do you want to check another password's strength (y/n) : ")
        if choice.lower() == 'y':
            return True
        elif choice.lower() == 'n':
            return False
        else:
            print('Invalid input...please try again. \n')


if __name__ == '__main__':
    print('********** Welcome to Password Strength Checker **********')
    check_psw = check_pwd()
    while check_psw:
        check_password_strength()
        check_psw = check_another_pwd()
    else:
        print("********** Thank You **********")