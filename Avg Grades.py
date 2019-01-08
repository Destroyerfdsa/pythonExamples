##
## Nicholaus
## 12/4/18
## Avg Grades
##
##
##gradelist = []
##def getGrade(gradelist):
##
##    while True:
##        maxGrade = 100
##        grade = input("Enter in a grade, or to exit press space bar")
##        if grade == " ":
##            break
##        elif grade.isdigit():
##            grade=float(grade)
##            if grade <= maxGrade:
##                gradelist.append(grade)
##            else:
##                q=input("are sure? "+str(grade)+"is good? y/n")
##                if q == "y":
##                    gradelist.append(grade)
##                else:
##                    print("not good grade")
##        else:
##            print("That is not a good grade")
##
##
##def avgfunction(gradelist):
##    total = sum(gradelist)
##    total = 0
##    for grade in gradelist:
##        total += grade
##    avg = total/len(gradelist)
##    return avg
##
##
##def main(gradelist):
##    
##    getGrade(gradelist)
##    avg = avgfunction(gradelist)
##    xmax = max(gradelist)
##    xmin = min(gradelist)
##    sorted(gradelist)
##    print(gradelist)
##    print(xmin)
##    print(xmax)
##    print("Your average grade is ",avg)
##
##
##main(gradelist)

start = 5
stop = 1000
stepvalue = 2
for i in range(start,stop,stepvalue):
    print(i)

