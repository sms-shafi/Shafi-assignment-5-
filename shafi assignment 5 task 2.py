numbers = list(range(1,11))
first_five_elements = numbers[:5]
reverse_five_elements = first_five_elements.copy()
reverse_five_elements.reverse()
print('Original list:',numbers)
print('Extracted first five elements:',first_five_elements)
print('Reversed extracted elements:',reverse_five_elements)
