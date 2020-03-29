import random


def guess_integer(num, ans):
    if num is None:
        print("1st parameter is None - exiting from function")
        return False
    if ans is None:
        print("2nd parameter is None - exiting from function")
        return False

    if 0 < num < 11:
        if num == ans:
            print("__!!!_____ you guessed right")
            return True
        else:
            print("NOT guessed right")
            return False
    else:
        print("number not within range")
        return False


if __name__ == "__main__":
    answer = random.randint(0, 10)

    while True:
        try:
            a = int(input("Please enter a number "))
            result = guess_integer(a,answer)
            if result:
                break
        except TypeError:
            print("expecting integer")
            continue
