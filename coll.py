<<<<<<< HEAD
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number//2
        else:
            number = number * 3 + 1
        count += 1
    return count
print(steps(6))
print(steps(1))
=======
def steps(number):
    if number <= 0:
        raise ValueError("Only positive integers allowed")
    count = 0
    while number != 1:
        if number % 2 == 0:
            number = number//2
        else:
            number = number * 3 + 1
        count += 1
    return count
print(steps(6))
print(steps(1))
>>>>>>> 6dd9691552871b3996124ea738570b6a08594b31
print(steps(0))