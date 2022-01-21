def is_member_in_a_group(student_no, lst_groups):

    count = 0

    for i in range(len(lst_groups)):
        for j in range(len(lst_groups[i])):
            if (lst_groups[i][j] == student_no):
                count += 1

    if (count == 1):
        ans = True
    else:
        ans = False

    return ans

def are_valid_groups(lst_student_no, lst_groups):

    ans = True
    no_of_student = len(lst_student_no)
    no_of_student_in_groups = 0
    bool_lst = []

    for x in range(len(lst_student_no)):
        student_no = lst_student_no[x]
        bool_lst.append(is_member_in_a_group(student_no, lst_groups))

    for i in range(len(lst_groups)):
            for j in range(len(lst_groups[i])):
                no_of_student_in_groups += 1
        
    if (no_of_student != no_of_student_in_groups):
        return False

    for i in range(len(bool_lst)):
        if (bool_lst[i] == False):
            ans = False

    return ans

lst_groups = [[1,2,3,4], [5,6,7,8], [9,10,11,12]]
lst_student_no = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(are_valid_groups(lst_student_no, lst_groups))