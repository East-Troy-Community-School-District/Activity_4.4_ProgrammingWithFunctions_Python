'''
Namespace Example 1
1/31/2023
Python I

Instructions:
Run the program and observe the output. Try adding
the following line of code to the bottom of the program...

print(local_variable)

The program does not work. Why?
Using this program as an example, where can you use
local variables? Global varaibles?
'''

def mystery():
    local_variable = 5
    print(global_variable)
    print(local_variable)


global_variable = 0
print(global_variable)
mystery()