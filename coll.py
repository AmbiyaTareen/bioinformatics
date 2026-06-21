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
print(steps(0))