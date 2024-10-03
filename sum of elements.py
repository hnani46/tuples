......
Write a program to get tuple elements in a single line separated by spaces and print the sum of the elements without using sum() method.
Sample Input:
10 20 30
Sample Output:
60
....
code:
....
def calculate_sum_of_tuple(values):
    total = 0  
    for value in values:
        total += value  
    return total
if __name__ == "__main__":
    input_values = input("Enter numbers separated by space: ")
    value_list = input_values.split()
    values = [int(x) for x in value_list]
    total_sum = calculate_sum_of_tuple(values)
    print(f"The sum of the elements is: {total_sum}")
......
output:
.....
Enter numbers separated by space: 1 2 3 4 5 
The sum of the elements is: 15

=== Code Execution Successful ===
