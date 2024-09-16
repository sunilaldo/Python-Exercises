def circulate_values(lst):
    if len(lst) > 1:
        first = lst.pop(0)  # Remove the first element
        lst.append(first)   # Add it to the end
    return lst

# Example usage:
values = [1, 2, 3, 4, 5]
print("Original list:", values)

# Perform circulation five times
for i in range(1, 6):
    values = circulate_values(values)
    print(f"After {i} circulation(s):", values)
