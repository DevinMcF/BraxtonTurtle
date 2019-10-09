def grade_average(the_list):
    sum_of = 0
    for num in the_list:
        sum_of = sum_of + num
    average = sum_of / len(the_list)
    return average


a_list = [99, 100, 74, 63, 100, 100]
print(grade_average(a_list))
