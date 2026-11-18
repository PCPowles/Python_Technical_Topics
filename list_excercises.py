# Let's simulate packing a bag for travel with lists and explore some operations!



# Packing our bag with initial items
bag = ['t-shirt', 'shorts', 'sandals']

# TODO: Add 'sunglasses' to our bag at the end
# bag = bag.append('sunglasses')
bag.append('sunglasses')
print(bag)
print("=======================================")

# We realized we need 'hat' right after 't-shirt', let's insert it at index 1
# TODO: Insert 'hat' into the bag at the position right after 't-shirt'
bag.insert(1, 'hat')
print(bag)
print("=======================================")

# Let's check the item at the top of the bag which is the last item we packed
top_item = bag[-1]
print(top_item)
print("=======================================")

# Printing out our bag to see all items packed
print(bag)

#///////////////////////////////////////
# https://codesignal.com/learn/course/90/unit/2/practice/3
# Answer
#///////////////////////////////////////

# Let's simulate packing a bag for travel with lists and explore some operations!

# Packing our bag with initial items
bag = ['t-shirt', 'shorts', 'sandals']

# TODO: Add 'sunglasses' to our bag at the end
bag.append('sunglasses')

# We realized we need 'hat' right after 't-shirt', let's insert it at index 1
# TODO: Insert 'hat' into the bag at the position right after 't-shirt'
bag.insert(1, 'hat')

# Let's check the item at the top of the bag which is the last item we packed
top_item = bag[-1]
print(top_item)

# Printing out our bag to see all items packed
print(bag)


#/////////////////////////////////////////////
# Check list items
#/////////////////////////////////////////////
# Travel Packing List and Selection
# from pickle import FALSE


packing_list = ['clothes', 'toothbrush', 'passport', 'camera']
item_to_check = 'passport'

# TODO: Write a line of code to check if the item_to_check is in the packing_list
is_item_packed = item_to_check in packing_list 

# TODO: Find the index of item_to_check in the list if it is packed, otherwise set it to -1
item_index = packing_list.index(item_to_check) if is_item_packed else -1


# Print out the results
print("Is the item packed?", is_item_packed)
print("Item index:", item_index)















