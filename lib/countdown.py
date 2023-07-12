# your code goes here!
import time


def countdown():
    i = 10
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
    print("HAPPY NEW YEAR!")


countdown()

print("\n")


def count_with_sleep():
    i = 10
    while i > 0:
        print(f"{i} SECOND(S)!")
        i -= 1
        time.sleep(1)
    print("HAPPY NEW YEAR!")


count_with_sleep()
