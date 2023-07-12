# your code goes here!
import time


def countdown(num):
    i = num
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    print("HAPPY NEW YEAR!")


# countdown()


def countdown_with_sleep(num):
    i = num
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


countdown_with_sleep(10)
