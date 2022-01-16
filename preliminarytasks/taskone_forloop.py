#  Use a loop from 1 to 100 and print the numbers that satisfy the following conditions:

divisible_by_7_and_3 = []
divisible_by_7_and_not_3 = []
odd_numbers_divisible_by_7_and_not_3 = []
divisible_sum_of_digits = []
equal_to_square_of_digits_sum = []


def divisible():
    for num in range(1, 101):
        if (num % 7 == 0) and (num % 3 == 0):
            divisible_by_7_and_3.append(num)

        if (num % 7 == 0) and (num % 3 != 0):
            divisible_by_7_and_not_3.append(num)

        if (num in divisible_by_7_and_not_3) and (num % 2 != 0):
            odd_numbers_divisible_by_7_and_not_3.append(num)

        digits_in_number = [int(x) for x in str(num)]
        sum_of_digits = sum(digits_in_number)
        if num % sum_of_digits == 0:
            divisible_sum_of_digits.append(num)

        if num == sum_of_digits ** 2:
            equal_to_square_of_digits_sum.append(num)


if __name__ == "__main__":
    divisible()
    print("Numbers Divisible by 7 and 3")
    print(divisible_by_7_and_3)

    print("Numbers divisible by 7 and not 3")
    print(divisible_by_7_and_not_3)

    print("Odd numbers divisible by 7 and not 3")
    print(odd_numbers_divisible_by_7_and_not_3)

    print("Numbers divisible by sum of their digits")
    print(divisible_sum_of_digits)

    print("Equal to square of sum of its digits")
    print(equal_to_square_of_digits_sum)

