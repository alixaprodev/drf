from collections import OrderedDict
import collections

def de_va():
    return 'missing values'
# Using a standard dict
regular_dict = collections.defaultdict(None)
regular_dict['apple'] = 3
regular_dict['banana'] = 2
regular_dict['cherry'] = 5
print(regular_dict[5])

# # Using an OrderedDict
# ordered_dict = OrderedDict()
# ordered_dict['apple'] = 3
# ordered_dict['banana'] = 2
# ordered_dict['cherry'] = 5

# # Iterating over the standard dict
# print("Iterating over a standard dict:")
# for key, value in regular_dict.items():
#     print(key, value)

# # Iterating over the OrderedDict
# print("\nIterating over an OrderedDict:")
# for key, value in ordered_dict.items():
#     print(key, value)
