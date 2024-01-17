import numpy as np
# initializing list
test_list = [["Gfg", "good"], ["is", "for"], ["Best"]]
# find the maximum length of a sublist
max_len = max(len(sublist) for sublist in test_list)
# pad the sublists with empty strings to make them the same length
padded_list = [sublist + [''] * (max_len - len(sublist)) for sublist in test_list]
# convert the list to a numpy array
arr = np.array(padded_list)
# use transpose to switch rows and columns
arr_t = arr.T
# use join to concatenate the strings in each row
res = [''.join(row) for row in arr_t]
# print the result
print("List after column concatenation: " + str(res))