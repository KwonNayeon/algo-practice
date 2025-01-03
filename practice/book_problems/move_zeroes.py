# Filename: move_zeros.py

def move_zeros(a_list):
   """
   Move all zeros to the end of the list while maintaining the order of non-zero elements.
   
   Args:
       a_list: List of integers
   Returns:
       list: Modified list with zeros moved to the end
   """
   zero_index = 0  # Keep track of where non-zero numbers should be placed
   
   # Iterate through the list with both index and value
   for index, n in enumerate(a_list):
       if n != 0:  # Found a non-zero number
           # Move the non-zero number to zero_index position
           a_list[zero_index] = n
           
           # If we've moved the number, put a zero in its original position
           if zero_index != index:
               a_list[index] = 0
               
           zero_index += 1  # Increment position for next non-zero number
           
   return a_list

# Test data
a_list = [8, 0, 3, 0, 12]

# Move zeros to end
move_zeros(a_list)
print(a_list)  # Expected output: [8, 3, 12, 0, 0]