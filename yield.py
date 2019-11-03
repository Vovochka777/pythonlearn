def endocounters():
    i=3
    while i != 0:
        yield i
        i -= 1

file1 = endocounters()
file2 = endocounters()

print(next(file1))
print(next(file1))
print(next(file1))