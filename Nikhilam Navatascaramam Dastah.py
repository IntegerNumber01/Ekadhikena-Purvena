import math


def main(num1, num2):
    # Determine bases for both numbers
    base1 = int('1' + ('0' * len(str(num1))))
    base2 = int('1' + ('0' * len(str(num2))))

    # If the number * 10 = base,
    # then make the base equal to the number
    if int(str(num1) + '0') == base1:
        base1 = num1

    if int(str(num2) + '0') == base2:
        base2 = num2

    # Make the biggest base dominant and get the number of zeros in the base
    if base1 > base2:
        base2 = base1
        zeros = len(str(base1)) - 1
    else:
        base1 = base2
        zeros = len(str(base2)) - 1

    # First priority conditions:
    # 1. If any number is equal to 0, return 0
    # 2. If any number is equal to 1, return the other number
    # 3. If both numbers are less than equal to 5, use the multiple table
    if num1 == 0 or num2 == 0:
        return 0

    if num1 == 1:
        return num2
    elif num2 == 1:
        return num1

    if num1 <= 5 and num2 <= 5:
        return multiple_table[num1][num2]

    # First step is to figure out the right values
    right1 = base1 - num1
    right2 = base2 - num2

    # Numbers have to be greater than 90% of the base
    # (the * operator is used and that is a violation that will be fixed later)
    if num1 <= math.ceil(base1 * (9 / 10)) or num2 <= math.ceil(base2 * (9 / 10)):
        return 'Formula Not Applicable'

    # Getting the left and right portions of the final answer
    left_ans = num1 - right2
    right_ans = main(right1, right2)

    # Becuase of recursion, right_ans can end up being 'Formula Not Applicable'
    if right_ans == 'Formula Not Applicable':
        return 'Formula Not Applicable'

    # Carrying
    if right_ans >= base1:
        to_carry = str(right_ans)[:len(str(right_ans)) - zeros]
        left_ans += int(to_carry)
        right_ans = str(right_ans)[len(str(right_ans)) - zeros:]

    # Adding extra zeros in FRONT of the right_ans if needed
    while len(str(right_ans)) < zeros:
        right_ans = '0' + str(right_ans)

    # Returning joined answer in the form of an integer
    return int(str(left_ans) + str(right_ans))


# Hard-coded 5x5 multiplication table
multiple_table = [[0, 0, 0, 0, 0, 0],
                  [0, 1, 2, 3, 4, 5],
                  [0, 2, 4, 6, 8, 10],
                  [0, 3, 6, 9, 12, 15],
                  [0, 4, 8, 12, 16, 20],
                  [0, 5, 10, 15, 20, 25],
                  ]
