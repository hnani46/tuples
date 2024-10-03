......
Write the program to count the number of times the given number (x) is present in the given tuple list and print it's factorial value without using factorial() method.
Sample Input:
1 2 3 4 1 5 1
1
Sample Output:
6
.....
code:
.....
def count_occurrences(tup, x):
    return tup.count(x)
def calculate_factorial(n):
    if n == 0 or n == 1:
        return 1
    factorial = 1
    for i in range(2, n + 1):
        factorial *= i
    return factorial
if __name__ == "__main__":
    input_values = input("Enter numbers for the tuple separated by space: ")
    value_list = input_values.split()
    tup = tuple(int(x) for x in value_list)
    x = int(input("Enter the number to count: "))
    count = count_occurrences(tup, x)
    factorial_value = calculate_factorial(x)
    print(f"The number {x} appears {count} time(s) in the tuple.")
    print(f"The factorial of {x} is: {factorial_value}")
......
output:
.....
Enter numbers for the tuple separated by space: 1 2 3 2 4 5
Enter the number to count: 2
The number 2 appears 2 time(s) in the tuple.
The factorial of 2 is: 2

=== Code Execution Successful ===
