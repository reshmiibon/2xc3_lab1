# Helper Functions

def is_member_in_a_group(student_no, group_list):

    c = 0

    for i in range(len(group_list)):
        for j in range(len(group_list[i])):
            if (group_list[i][j] == student_no):
                c += 1

    if (c == 1):
        result = True
    else:
        result = False

    return result

def are_valid_groupsizes(group_list):

    val = True

    for i in range(len(group_list)):
        if (len(group_list[i]) != 2 and len(group_list[i]) != 3):
            val = False

    return val

# Main Function

def are_valid_groups(lst_student_no, group_list):

    result = True
    no_of_student = len(lst_student_no)
    no_of_student_in_groups = 0
    bool_lst = []

    if (are_valid_groupsizes(group_list) == False):
        return False

    for x in range(len(lst_student_no)):
        student_no = lst_student_no[x]
        bool_lst.append(is_member_in_a_group(student_no, group_list))

    for i in range(len(group_list)):
            for j in range(len(group_list[i])):
                no_of_student_in_groups += 1
        
    if (no_of_student != no_of_student_in_groups):
        return False

    for i in range(len(bool_lst)):
        if (bool_lst[i] == False):
            result = False

    return result
