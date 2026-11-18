# List
def modify_list(my_list):
    # Replace the second element (index 1) with 100
    my_list[1] = 100
    
    # Append 200 to the end of the list
    my_list.append(200)

    # Print the modified list
    print(my_list)

# Example list
example_list: list[int]=[10, 20, 30, 40, 50]
modify_list(my_list=example_list)

# Expected Output:
# [10, 100, 30, 40, 50, 200]
# .venv\Scripts\Activate.ps1 --> To Start Virtual Environment 