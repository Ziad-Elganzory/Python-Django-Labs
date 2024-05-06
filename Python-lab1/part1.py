# 1- 

fullName = input("Enter your first and last name: ")[::-1]
print(fullName)


# 2- 

n = int(input("Enter number: "))
print(n + int(f"{n}{n}") + int(f"{n}{n}{n}"))


# 3- 

print(
    """a string that you "don't" have to escape
This
is a ....... multi-line
heredoc string --------> example"""
)


# 4-

r = float(input("Enter sphere radius: "))
print(f"Volume = {((4/3) * 3.14 * r * r * r)}")

# 5-

base = float(input("Enter the base: "))
height = float(input("Enter the height: "))

print(f"Area = {(1/2)*base*height}")


# 6-

for i in range(1, 10):
    if i <= 5:
        print("* " * i)
    else:
        print("* " * (10 - i))


# 7- Write a Python program that accepts a word from the user and reverse it.
word = input("Enter word: ")[::-1]
print(word)

# 8- Write a Python program that prints all the numbers from 0 to 6 except 3 and 6.
for i in range(7):
    if i != 3 and i != 6:
        print(i)

# 9-Write a Python program to get the Fibonacci series between 0 to 50
a, b = 0, 1
while a <= 50:
    print(a)
    a, b = b, a + b

# 10- Write a Python program that accepts a string and calculate the number of digits and
# letters.

str = input("Enter String: ")

digits = 0
letters = 0

for char in str:
    if char.isdigit():
        digits += 1
    elif char.isalpha():
        letters += 1
print(f"digits: {digits}, letters: {letters}")
