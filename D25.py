# A student will not be allowed to sit in an exam if his/her attendance is less than 75%.Take following
# input from the user. Number of classes held. Number of classes attended. And print, percentage of
# class attended. Is the student is allowed to sit in the exam or not.

a=int(input("number of class held"))
b=int(input("number of class attended"))
percentage=b/a*100
if percentage<70:
    print("not allowed")
else:
    print("allowed")