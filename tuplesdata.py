.....
Write a program to get n number of tuple elements from the user in separate lines and print the sum of their values using predefined method.
.....
code:
...

n = int(input("Enter the number of elements: "))
elements = []
for _ in range(n):
    element = float(input("Enter a number: ")) 

tuple_elements = tuple(elements)
total_sum = sum(tuple_elements)

print("The sum of the tuple elements is:", total_sum)
....
output:
...
Enter the number of elements: 4
Enter a number: 20
Enter a number: 24
Enter a number: 15
Enter a number: 42
The sum of the tuple elements is: 101.0

=== Code Execution Successful ===
