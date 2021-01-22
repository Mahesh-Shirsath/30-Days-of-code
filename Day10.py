"""Given a base-10 integer, n, convert it to binary (base-2). Then find and print the base-10 integer denoting the maximum number 
of consecutive 1's in n's binary representation. When working with different bases, it is common to show the base as a subscript."""


def consecutive(n):
    n = int(n[2:])
    count, maximum= 0, 0
    while n > 0:
        if n % 10 == 1:
            count += 1
        else:
            count = 0
        maximum = max(count, maximum)
        n = int(n / 10)
    return maximum

if __name__ == '__main__':
    n = int(input())
    result = consecutive(bin(n))    
    print(result)
