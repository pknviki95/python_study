'''
- Python byteray are a **sequence of integers in the range of 0-255**. 
- If the sequece of elements exceeds 255 it throws vaue error

'''

# sequence of numbers exceeds range from 0-255 - value error

list_variable=[1,2,3,65,66,256]

# bytes() for using bytes objects
bytearray_variable=bytearray(list_variable)

print("bytearray_variable: ",bytearray_variable)