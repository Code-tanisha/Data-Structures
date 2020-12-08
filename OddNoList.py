# Create a list of all odd numbers between 1 and a max number.
# Max number is something you need to take from a user using input() function
max_no = int(input("Enter maximum no"))
odd_nos = []
for i in range(max_no):
    if i%2 == 1:
        odd_nos.append(i)
print(odd_nos)
