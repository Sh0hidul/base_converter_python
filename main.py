
def convert(n,b):
    digits = []
    if n == 0:
        return 0

    if n < 0 or b < 2:
        raise ValueError('Number cannot be negative or denominator can not be less than 2')

    while n > 0:
        r = n % b
        n = n//b
        digits.insert(0,r)
    return digits
list1 = convert(0,3)
print(list1)

