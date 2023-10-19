def average(*numbers):
    sum=0
    for i in numbers:
        sum = sum + i
    print("average is:",sum/len(numbers))

average(56,45,8,1)