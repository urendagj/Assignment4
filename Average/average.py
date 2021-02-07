#Code to calculate the avergae of a list

def Average(lst):
    total = 0
    for i in range(0,len(lst)):
        total = total + lst[i] 
    return round(total / len(lst), 2)

# lst = [15, 9, 55, 41, 35, 20, 62, 49]
# average = Average(lst)
# print("Average of the list = ", round(average,2))