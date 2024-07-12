# LIST
#  list - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit

shopping_list = ['fruits', 'Vegetables', 'spices', 'stationary', 'furniture']
print(shopping_list)
# print(len(shopping_list))
# print(shopping_list[1])
# print(shopping_list[-3])

# shopping_list.append('kitchen tools')  # Add item at the end
# print(shopping_list)
#
# shopping_list.insert(6, 'Diary')  # Add item in the middle
# print(shopping_list)
#
# shopping_list.extend(['pooja utilities', 'home decor pieces'])  # Add multiple items in the end
# print(shopping_list)

shopping_list.remove('fruits')
print(shopping_list)

print(shopping_list.pop())
print(shopping_list.index("stationary"))
print(shopping_list)
shopping_list.reverse()
print(shopping_list)
shopping_list.sort()
print(shopping_list)

shopping_list[2] = 'Diary'
print(shopping_list)

shopping_list[2] = 678
print(shopping_list)

print(type(shopping_list))
