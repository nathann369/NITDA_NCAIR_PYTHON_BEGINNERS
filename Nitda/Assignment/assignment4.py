


# What it does: Inserts an element at a specific position (index) in the list.

# Example:

lst = [1, 2, 4]
lst.insert(2, 3)  # Insert 3 at index 2
print(lst)  # Output: [1, 2, 3, 4]

# 2. extend(iterable)
# What it does: Adds all elements from an iterable (like a list, tuple, etc.) to the end of the list.

# Example:

lst = [1, 2]
lst.extend([3, 4])
print(lst)  # Output: [1, 2, 3, 4]

# 3. remove(element)
# What it does: Removes the first occurrence of the specified element from the list.

# Example:

lst = [1, 2, 3, 2]
lst.remove(2)
print(lst)  # Output: [1, 3, 2]

# 4. pop([index])
# What it does: Removes and returns the element at the given index. If no index is specified, it removes and returns the last item.

# Example:

lst = [1, 2, 3]
popped = lst.pop()      # Removes last element
print(popped)           # Output: 3
print(lst)              # Output: [1, 2]

popped_index = lst.pop(0)  # Removes element at index 0
print(popped_index)        # Output: 1
print(lst)                 # Output: [2]

# 5. index(element[, start[, end]])
# What it does: Returns the index of the first occurrence of the specified element. Optional start and end specify the search range.

# Example:

lst = [1, 2, 3, 2]
idx = lst.index(2)
print(idx)  # Output: 1

# 6. count(element)
# What it does: Returns the number of times the specified element appears in the list.

# Example:


lst = [1, 2, 2, 3]
cnt = lst.count(2)
print(cnt)  # Output: 2

# 7. sort(key=None, reverse=False)
# What it does: Sorts the list in place (modifies the list itself).

# key is a function that serves as a sort key (optional).

# reverse=True sorts in descending order.

# Example:


lst = [3, 1, 2]
lst.sort()
print(lst)  # Output: [1, 2, 3]

lst.sort(reverse=True)
print(lst)  # Output: [3, 2, 1]

# 8. reverse()
# What it does: Reverses the elements of the list in place.

# Example:

lst = [1, 2, 3]
lst.reverse()
print(lst)  # Output: [3, 2, 1]
# 9. clear()
# What it does: Removes all elements from the list, making it empty.

# Example:


lst = [1, 2, 3]
lst.clear()
print(lst)  # Output: []

# 10. copy()
# What it does: Returns a shallow copy of the list.

# Example:
 
lst = [1, 2, 3]
lst_copy = lst.copy()
print(lst_copy)  # Output: [1, 2, 3]
