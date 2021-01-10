from random import randint


def play():
    random_int = randint(0, 100)
    while True:
        user_guess = int(input("Guess the number"))

        if user_guess < random_int:
            print("猜小了")
            continue

        elif user_guess > random_int:
            print("猜大了")
            continue

        else:
            print("猜对了")
            break


if __name__ == '__main__':
    play()
