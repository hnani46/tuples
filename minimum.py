......
 Write a program to get n number of values from user in separate line and print the minimum value of the given tuple.
Sample Input:
3
20
30
10
Sample Output:
10
....
code:
...
def get_min_from_values(n):
    values = []
    for i in range(n):
        value = input(f"Enter value {i + 1}: ")
        values.append(value)
    try:
        values = [int(x) for x in values]
    except ValueError:
        values = [float(x) for x in values]
    min_value = min(values)
    print(f"The minimum value is: {min_value}")

if __name__ == "__main__":
    n = int(input("Enter the number of values you want to input: "))
    get_min_from_values(n)
.....
output:
....
Enter the number of values you want to input: 5
Enter value 1: 2
Enter value 2: 6
Enter value 3: 10
Enter value 4: 46
Enter value 5: 34
The minimum value is: 2

=== Code Execution Successful ===
