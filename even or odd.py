......
 Raju is a 3rd grade kid, he is struggling to find which is "even" number and which is a "odd" number. So, his teacher gave him a task to find how many even numbers and how many odd numbers are there in the given collection of values and print "Even" if even count is more than odd count, else print "Odd", if odd count is more and print "Equal" if both even count and odd count are same. Help Raju to understand the difference of even and odd.
Sample Input:
1 2 3 4 5
Sample Output:
Odd
.....
code:
...
def count_even_odd(values):
    even_count = 0  
    odd_count = 0   
    for value in values:
        if value % 2 == 0:
            even_count += 1  
        else:
            odd_count += 1   
    return even_count, odd_count
if __name__ == "__main__":
    input_values = input("Enter numbers separated by space: ")
    value_list = input_values.split()
    values = [int(x) for x in value_list]
    even_count, odd_count = count_even_odd(values)
    print(f"Even count: {even_count}")
    print(f"Odd count: {odd_count}")
    if even_count > odd_count:
        print("Even")
    elif odd_count > even_count:
        print("Odd")
    else:
        print("Equal")
....
output:
....
Enter numbers separated by space: 1 2 3 4 5 6 7
Even count: 3
Odd count: 4
Odd

=== Code Execution Successful ===
