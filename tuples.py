# tuples lists
names = ('Alice', 'Bob', 'Charlie', 'Diana', 'Eve', 'Bob')
         
print('original',names)
# it will print from staring index not the last index
print(names[1:-2])

print(names.index('Charlie'))
# find the 4th element but index 3
print(names[3])
# find how many times Bob is in the tuple
print(names.count('Bob'))