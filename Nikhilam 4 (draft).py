import math
import operator


def is_tenth_power(n):
    # # Is integer checks if a float is an integer ex: 10.0 is True, 10.5 is False

    if n <= 0:
        return False
    while n % 10 == 0:
        n //= 10

    if n == 1:
        return True
    else:
        return False


def main(num1, num2):
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

    # Average between the 2 highest places
    # The -1 as the second parameter in round rounds like this: 42->40, 56->60
    base = int(round((num1 + num2) / 2, -1))
    if base == 0:
        return 'Formula Not Applicable'

    if num1 < base:
        # part 1 method
        right1 = base - num1
        sign1 = operator.sub
    else:
        # Use part 2 method
        right1 = num1 - base
        sign1 = operator.add

    if num2 < base:
        # part 1 method
        right2 = base - num2
        sign2 = operator.sub
    else:
        # Use part 2 method
        right2 = num2 - base
        sign2 = operator.add

    right_ans = main(right1, right2)
    left_ans = sign2(num1, right2)

    if right_ans == 'Formula Not Applicable':
        return right_ans

    # If something DOESNT fully fall under part 1, then multiply the extra thing
    if not (is_tenth_power(base) and {sign1, sign2} == {operator.sub}):
        left_ans = main(left_ans, int(base / 10))
        if left_ans == 'Formula Not Applicable':
            return left_ans

    # Checks if sign1 and sign 2 are different
    if {sign1, sign2} == {operator.add, operator.sub}:
        # String manipulation is slower, so we mathematically carry over
        # Subtract all but last digit
        left_ans -= math.floor(right_ans / 10)
        # Cut the right answer to be just the last digit
        right_ans = int(str(right_ans)[-1])

        if not right_ans == 0:
            left_ans -= 1
            right_ans = 10 - right_ans

    elif {sign1, sign2} == {operator.sub}:
        # Carrying
        if (right_ans >= 10 and is_tenth_power(base) is False) or (num1 < 10 and num2 < 10):
            left_ans += math.floor(right_ans / 10)
            right_ans = int(str(right_ans)[-1])

        zeros = len(str(base)) - 1
        while len(str(right_ans)) < zeros:
            right_ans = '0' + str(right_ans)
    else:
        # Carrying
        left_ans += math.floor(right_ans / 10)
        right_ans = int(str(right_ans)[-1])

    return int(str(left_ans) + str(right_ans))


# Hard-coded 5x5 multiplication table
multiple_table = [[0, 0, 0, 0, 0, 0],
                  [0, 1, 2, 3, 4, 5],
                  [0, 2, 4, 6, 8, 10],
                  [0, 3, 6, 9, 12, 15],
                  [0, 4, 8, 12, 16, 20],
                  [0, 5, 10, 15, 20, 25],
                  ]


# print(main(94, 98))
# print(main(94, 98))
# exit()
# ## Manual Testing ##
# num1 = 8
# num2 = 2

# try:
#     ANS = main(num1, num2)
#     print('ANSWER:  ', ANS)
#     print('IS IT CORRECT?', int(ANS) == num1 * num2)
# except RecursionError:
#     print('ERROR: ', num1, 'x', num2)

# exit()
## Exahaustive check for equations solved ##
count = 0
for i in range(100):
    for x in range(100):
        try:
            # base1, base2 = calculate_base(x, i)
            ANS = main(x, i)
            if ANS == 'Formula Not Applicable':
                pass
            elif not ANS == x * i:
                print('NOT EQUAL', x, 'x', i, ANS, 'base:', int(round((int(x) + int(i)) / 2, -1)))
            else:
                count += 1
        except RecursionError:
            print('ERROR: ', x, 'x', i)

print(count, 'equations solved')
