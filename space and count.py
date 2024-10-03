.....
 Write a program to get the tuple values in a single line separated by space and count the nuber of times the given x value is present in the given tuple.
Sample Input:
1 2 3 1 2 3 4 1 2 1
1
Sample Output:
4
....
code:
....
def count_value_in_tuple(values, x):
    value_tuple = tuple(values)
    count = value_tuple.count(x)
    return count
if __name__ == "__main__":
    input_values = input("Enter values separated by space: ")
    values = input_values.split()
    x = input("Enter the value to count: ")
    count = count_value_in_tuple(values, x)
    print(f"The value '{x}' appears {count} time(s) in the tuple.")
....
output:
....
Enter values separated by space: 10 20 10 30 10 40
Enter the value to count: 3
The value '3' appears 0 time(s) in the tuple.

=== Code Execution Successful ===
