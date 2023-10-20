#linear search
def linear_search(roll_numbers,target):
    for i,roll in enumerate(roll_numbers):
        if roll == target:
            return i
            return -1
    
#sentinel search
def sentinel_search(roll_numbers,target):
    roll_numbers.append(target)
    i=0
    while roll_numbers[i]!=target:
        i+=1
        roll_numbers.pop()
        if i<len(roll_numbers):
            return i
            return -1
    
#binary search
def binary_search(roll_numbers,target):
    left,right=0,len(roll_numbers)-1
    while left<=right:
        mid = (left+right)
        if roll_numbers[mid]==target:
            return mid
        elif roll_numbers[mid]<target:
            left=mid+1
        else:
            right=mid-1
            return-1
        
#fibonacci search
def fibonacci_search(roll_numbers,target):
    fib_m_minus_2 =0
    fib_m_minus_1 =1
    fib = fib_m_minus_1+fib_m_minus_2
    while fib<len(roll_numbers):
            fib_m_minus_2 = fib_m_minus_1
            fib_m_minus_1 = fib
            fib = fib_m_minus_1+fib_m_minus_2

            offset =-1
    while fib>1:
        i = min(offset + fib_m_minus_2,len(roll_numbers)-1)
        if roll_numbers[i]<target:
                fib = fib_m_minus_1
                fib_m_minus_1 = fib_m_minus_2
                fib_m_minus_2 = fib_m_minus_1
        
                offset =i
        elif roll_numbers[i]>target:
                fib = fib_m_minus_2
                fib_m_minus_1 = fib_m_minus_1 - fib_m_minus_2
                fib_m_minus_2 = fib_m_minus_1
    
        else:
            return i
        
        if fib_m_minus_1 and roll_numbers[offset+1] ==target:
             return offset+1
        return -1


#example usage:
roll_numbers_unsorted = [101,111,105,107,109]
roll_numbers_sorted = [101,103,105,107,109]

#linear search and sentinel search on unsorted data
print("linear search result:",linear_search(roll_numbers_unsorted,105))
print("sentinel search result:",sentinel_search(roll_numbers_unsorted,105))

#binary search and fibonacci search on sorted data
print("binary search result:",binary_search(roll_numbers_sorted,105))
print("fibonacci search reult:",fibonacci_search(roll_numbers_sorted,105))