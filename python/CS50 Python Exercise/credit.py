def luhn_check(card_num):
    total = 0
    reverse_digit = card_num[::-1]
    for i in range(len(card_num)):
        digit = int(reverse_digit[i])
        if i % 2 == 1:
            doubled = digit*2
            total += doubled if doubled < 10 else (doubled - 9)
        else:
            total += digit

    return total % 10 == 0


def card_type(card_num):
    length = len(card_num)
    digit_one = int(card_num[0])
    digit_two = int(card_num[1])

    if digit_one == 4 and (length == 13 or length == 16):
        print("VISA")

    elif digit_one == 5 and (1 <= digit_two <= 5) and length == 16:
        print("MASTERCARD")

    elif digit_one == 3 and (digit_two == 4 or digit_two == 7) and length == 15:
        print("AMEX")

    else:
        print("INVALID")
    return


def main():
    card_num = input("Number: ")
    if not card_num.isdigit():
        print("INVALID")
        return

    if luhn_check(card_num):
        card_type(card_num)
    else:
        print("INVALID")


if __name__ == "__main__":
    main()
