def is_prime(num):
    number = 1
    while number != num:
        if num % number != 0:
            number += 1
            if num % number == 0:
                return False
            else:
                return True
        else:
            return False
print(is_prime(7))