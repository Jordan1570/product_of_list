# multiply all numbers in list

def find_product(list_of_nums):
    
    # this way we multiply the first num by 1 to keep a postive value
    product_of_list = 1

    for num in list_of_nums:
        product_of_list *= num

    return product_of_list

list_product = find_product([8, 2, 3, -1, 7])

print(f'Product of list is {list_product}')