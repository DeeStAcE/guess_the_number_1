from random import randint


def get_the_number():
    while True:
        try:
            user_number = int(input('Enter your number:'))
            break
        except ValueError:
            print("It's not a number")

    return user_number


def check_the_numbers():
    random_num = randint(1, 100)
    user_num = get_the_number()
    while random_num != user_num:
        # print(random_num)
        if random_num > user_num:
            print('Too small!')
        else:
            print('Too big!')
        user_num = get_the_number()
    print('You win!')


check_the_numbers()
