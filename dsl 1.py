group_a=['rohan','soham','gaurav','shubham'] #cricket players
group_b=['rohan','soham','advait','ronak','omkar'] #badminton players
group_c=['shubham','omkar','arya','gaurav'] #football players

def common_elememts(list1,list2):
    return list(set(list1)& set(list2))
    
def unique_elements(list1,list2):
    return list(set(list1)& set(list2))
    
def unique_elements_in_all(list1,list2,list3):
    return list(set(list1)^ set(list2)^ set(list3))
    
def count_unique_elements(list1):
    return len(set(list1))

both_ab=common_elememts(group_a, group_b)
either_ab_but_not_both=unique_elements(group_a, group_b)
neither_ab=unique_elements_in_all(group_a, group_b, group_c)
both_a_and_c_but_not_b=common_elememts(group_a, group_c)

print("a) list of students who play both cricket and badminton:",both_ab)
print("b) list of students who play either cricket or badminton but not both:",either_ab_but_not_both)
print("c) number of students who play neither cricket nor badminton:",count_unique_elements(neither_ab))
print("d) number of students who play cricket and football but not badminton:",count_unique_elements(both_a_and_c_but_not_b))