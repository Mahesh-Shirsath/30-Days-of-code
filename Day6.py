"""Given a string,S, of length N that is indexed from 0 to N-1, print its even-indexed and odd-indexed characters as  
space-separated strings on a single line (see the Sample below for more detail)"""

def even_odd(arr):
    even, odd = [], []
    for i in range(len(arr)):
        if i % 2 == 0:
            even.append(arr[i])
        else:
            odd.append(arr[i])
    str1 = ""
    return (str1.join(even), str1.join(odd))
if __name__ == "__main__":
    no_items = int(input())
    strings = []
    for i in range(no_items):
        strings.append(input().strip())
    for i in range(no_items):
        lst = list(strings[i])
        even, odd = map(str, even_odd(lst))
        print(even, odd)
