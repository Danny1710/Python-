# THIS FILE MUST NOT CONTAIN ANYTHING OTHER THAN
# FUNCTION DEFINITIONS AND COMMENTS. You can define
# functions other than the one(s) required.

# You are not being marked on code quality for the programming questions
# If you use resources other than the course material, you must reference it as a comment
# You should submit this file at the submission link in Wattle.

# Part a
def count_if_triple(list_of_ints):
    count= 0
    for item in list_of_ints:
        if type(item) == tuple:
                for tup in item:
                    if type(tup) == list:
                        if  tup == []:
                            pass
                        else:
                            for elem in tup:
                                if elem != 0 and elem %3 == 0:
                                    count += 1
                                else:
                                    pass    
                    elif type(tup) == int and tup % 3 == 0:
                        count += 1  
                                   
        if type(item) == list:
            if item == []:
                pass
            else:
                for elem in item :
                    if elem != 0 and elem %3 == 0:
                        count += 1  
        elif type(item) == int and item != 0 and item%3 == 0:
            count += 1
        else:
            pass
    return count
    
  
  
    
    
        

# Part b
def count_if_multiple(list_of_ints, divisor):
    return set()
    
    