def linear_search(roll_numbers, target):
    for i in range(len(roll_numbers)):
        if roll_numbers[i] ==target:
            return True
    return False

def sentinel_search(roll_numbers, target):
    roll_numbers.append(target)
    index =0
    while roll_numbers[index] !=target:
        index +=1
    return index !=len(roll_numbers) -1

roll_numbers = [45, 34, 76, 98, 23, 10]
target =34

print("Using Linear Search:")
print("Is the target present?", linear_search(roll_numbers, target))

print("\nUsing Sentinel Search:")
print("Is the target present?", sentinel_search(roll_numbers, target))
