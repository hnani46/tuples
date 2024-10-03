Write a program to get the tuple elements in a single line separated by spaces and print the number of elements in the given tuple.
Sample Input:
10 20 30
Sample Output:
3
.....
input_data = input("Enter numbers separated by spaces: ")

tuple_elements = tuple(input_data.split())

print(len(tuple_elements))
...
output:
....
Enter numbers separated by spaces: 10 20 30
3
