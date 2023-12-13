class_marks = {'ronak': 95, 'John': 85, 'Jitesh': 95, 'Sandeep': 70, 'David': 92}

absent_students=['Rancho', 'Faran', 'Raju']
def average_score(class_marks):
    total_marks =sum(class_marks.values())
    return total_marks /len(class_marks)

def highest_lowest_score(class_marks):
    return max(class_marks.values()), min(class_marks.values())

def count_absent_students(class_marks, absent_students):
    return len(absent_students)

def most_common_mark(class_marks):
    mark_counts = {}
    for mark in class_marks.values():
        if mark in mark_counts:
            mark_counts[mark] +=1
        else:
            mark_counts[mark] =1

    highest_freq_mark =max(mark_counts, key=mark_counts.get)
    return highest_freq_mark, mark_counts[highest_freq_mark]

average_mark =average_score(class_marks)
highest_mark, lowest_mark =highest_lowest_score(class_marks)
count_absent =count_absent_students(class_marks, absent_students)
most_common_mark, frequency =most_common_mark(class_marks)

print("a) Average score of class: ", average_mark)
print("b) Highest score and lowest score of class: ", highest_mark, " and ", lowest_mark)
print("c) Count of students who were absent for the test: ", count_absent)
print("d) Most common mark and its frequency: ", most_common_mark, " with a frequency of ", frequency)
