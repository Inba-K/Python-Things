number = int(input("Enter a number: "))
original_number = number
sum_of_powers = 0
num_digits = len(str(number))

for digit_char in str(number):
    digit = int(digit_char)
    sum_of_powers += digit ** num_digits

if sum_of_powers == original_number:
    print(f"{original_number} is an Armstrong number.")
else:
    print(f"{original_number} is not an Armstrong number.")
