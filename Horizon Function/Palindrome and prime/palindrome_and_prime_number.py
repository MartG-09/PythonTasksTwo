def check_if_number_is_palindrome_and_prime(number):
    digit = number
    length = len(str(digit))
    each = 0

    for count in range(length):
        num = digit % 10
        each = (each * 10) + num
        digit //= 10
    if (each != number):
            return False

    half_num = (number // 2) + 1
    for count in range(2 , half_num):
        if (number % count == 0):
            return False
    
    return True
