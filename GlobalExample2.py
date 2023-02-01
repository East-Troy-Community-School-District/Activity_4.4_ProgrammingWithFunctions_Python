'''
Global Example 2
1/31/2023
Python I

Instructions:
Run the program and observe the output.
'''

def my_function():
    global x, y
    x = 200


x = 300
y = 3
print(x)
my_function()
print(x)
