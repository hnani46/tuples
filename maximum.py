.....
Write a program to get n number of tuple elements from the user in separate line and print the maximum value of the given values.
....
code:
...
def get_max_from_tuples(n):
    elements = []
    for i in range(n):
        value = input(f"Enter element {i + 1}: ")
        elements.append(value)
    try:
        elements = [int(x) for x in elements]
    except ValueError:
        elements = [float(x) for x in elements]
    max_value = max(elements)
    
    print(f"The maximum value is: {max_value}")

if __name__ == "__main__":
    n = int(input("Enter the number of elements you want to input: "))
    get_max_from_tuples(n)
...
output:
....
Enter the number of elements you want to input: 4
Enter element 1: 12
Enter element 2: 2
Enter element 3: 5
Enter element 4: 26
The maximum value is: 26

=== Code Execution Successful ===
