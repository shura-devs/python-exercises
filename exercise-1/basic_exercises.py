'''
Implement the following functions. You can use as many helper functions as you like.

To check whether your implentation is correct, run the following command:
"pytest"

If all tests do not pass, you need to identify the bugs and correct your functions.
'''

'''
Reverse a list
[1,2,3] -> [3,2,1]
'''
def reverse_list(my_list):
    pass

'''
Merge 2 lists together
[1,2,3], [10,11,12] -> [(1, 10), (2, 11), (3,12)] 
'''
def merge_lists(l1, l2):
    pass

'''
Return 'True' if the sum of the element in my_list
or the product of the elements in my_list
are divisible by 10.
Return 'False' otherwise.
'''
def total_divisible_by_ten(my_list):
    pass

'''
You are given a dictionary with strings as keys and ints as values
Return a new dictionary with all key value pairs in dict_with_dogs 
except key value pairs where the key contains the string "dog"
["cat":25, "horse":35, "dog":22, "catdog":23, "cat_dog_horse":40] ->
["cat":25, "horse":35]
'''
def filter_dog(dict_with_dogs):
    pass


'''
Write a recursive function which takes the parameters:
- num: Any number above 0
- my_list: an empty list []

If num == 1, return my_list
If num is odd, it should calculate the following calculation: (num + 1) / 2, 
add the new value to my_list and then call recurse_func again
If num is even, it should calculate the following calculation: (num + 2) / 2 
add the new value to my_list and then call recurse_func again
'''
def recurse_func(num, my_list):
    pass