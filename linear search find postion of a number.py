#linear search to find postion of a given number
def search(lst, n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i  # Return the index if found
    return -1  # Return -1 if not found

lst = [5, 8, 4, 6, 2, 7, 3, 9]
n = 6

position = search(lst, n)
if position != -1:
    print("Found at position:", position + 1)  # Convert zero-based index to one-based index
else:
    print("Not found")
