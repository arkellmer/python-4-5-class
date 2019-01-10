#andrew kellmer 12/4/18
#avg grade

grade_list = []

def get_grade(grade_list):

    while True:
        max_grade = 100
        grade = input("enter a grade to exit press space bar and enter")
        
        if grade == " ":
            break
        
        elif grade.isdigit():
            grade = float(grade)
            
            if grade <= max_grade:
                grade_list.append(grade)
                
            else:
                q = input("are you sure this is a good grade y or n")
                
                if q == "y":
                    grade_list.append(grade)

                else:
                    print("thats not a good grade")
                    
        else:
            print("thats not a good grade")

get_grade(grade_list)
print(grade_list)

def avg_function(grade_list):
    total = sum(grade_list)
    
    avg = total/len(grade_list)
    return avg

def main(grade_list):

    get_grade(grade_list)
    avg = avg_function(grade_list)
    xmax = max(grade_list)
    xmin = min(grade_list)
    sorted(grade_list)
    print("the max is",xmax,"\nand the min is",xmin)
    print("your grade is ", avg)
    
main(grade_list)

