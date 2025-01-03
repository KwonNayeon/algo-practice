# Filename: find_duplicates.py

def duplicates(an_iterable):
   """
   Find duplicate items in an iterable object.
   
   Args:
       an_iterable: Any iterable object (list, tuple, etc.)
   Returns:
       list: A list containing all duplicate items
   """
   dups = []  # Store duplicate items
   a_set = set()  # Use set for efficient lookup
   
   for item in an_iterable:
       l1 = len(a_set)  # Length before adding item
       a_set.add(item)  # Try to add item to set
       l2 = len(a_set)  # Length after adding item
       
       # If lengths are same, item was already in set
       if l1 == l2:
           dups.append(item)
   return dups

# Test data
a_list = [
   'Susan Adams',
   'Kwame Goodall', 
   'Jill Hampton',
   'Susan Adams'  # Duplicate name
]

# Find and print duplicates
dups = duplicates(a_list)
print(dups)  # Expected output: ['Susan Adams']