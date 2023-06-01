number = input("Enter a number: ")
number_incremented = ""
for figure in number:
    new_digit = str((int(figure) + 1) % 10)
    number_incremented += new_digit

print("The number incremented by 1 is:", number_incremented)