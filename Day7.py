"""Given an array, A, of N integers, print A's elements in reverse order as a single line of space-separated numbers."""

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))
    for i in range(len(arr), 0, -1):
        print(arr[i-1], end=" ")
    print()

