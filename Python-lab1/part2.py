# 1- 

arr = [1, 2, 3, 3, 3]
arr = list(set(arr))
print(arr)

# 2- 

def merge_halves(a, b):
    """Merges two strings by combining their front and back halves."""
    a_mid = len(a) // 2 + len(a) % 2
    b_mid = len(b) // 2
    return a[:a_mid] + b[:b_mid] + a[a_mid:] + b[b_mid:]


string1 = "abcd"
string2 = "efgh"
merged_string = merge_halves(string1, string2)
print(merged_string)  # Output: abefcdgh


# 3- 

def all_unique(nums):
    """Checks if all numbers in a sequence are unique."""
    return len(set(nums)) == len(
        nums
    )

numbers1 = [1, 5, 7, 9]
numbers2 = [2, 4, 5, 5, 7, 9]
print(all_unique(numbers1))  
print(all_unique(numbers2))  


# 4- 

def bubble_sort(nums):
    """Sorts a list of numbers using bubble sort algorithm."""
    n = len(nums)
    for i in range(n - 1):
        for j in range(n - i - 1):  
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = (
                    nums[j + 1],
                    nums[j],
                )  

numbers = [5, 3, 8, 6, 7, 2]
bubble_sort(numbers)
print(numbers)  


# 5- 

import random

def guess_game():
    """Implements a number guessing game with 10 tries."""
    random_number = random.randint(1, 100)
    tries = 10
    guessed_numbers = set()

    while tries > 0:
        try:
            user_guess = int(input("Guess a number between 1 and 100: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if user_guess < 1 or user_guess > 100:
            print("Number out of range. Please try again.")
            continue

        if user_guess in guessed_numbers:
            print("You already guessed that number. Try again.")
            continue

        guessed_numbers.add(user_guess)
        tries -= 1

        if user_guess == random_number:
            print("Congratulations! You guessed the number in", 10 - tries, "tries!")
            if input("Play again? (y/n): ").lower() == "y":
                guess_game()  
            else:
                print("Thanks for playing!")
                break  
        elif user_guess < random_number:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    if tries == 0:
        print("You ran out of tries. The number was", random_number)
        if input("Play again? (y/n): ").lower() == "y":
            guess_game()  
        else:
            print("Thanks for playing!")

guess_game()
