#Hermosisima_Random
import math
def Not_Even(list):
    list.sort()
    lenofList=int(len(list)-1)
    sum = 0
    for a in list:
        sum+=a
    average = sum / (lenofList+1)

    #Range
    lowest = list[0]
    highest = list[-1]
    range = highest-lowest

    #Quartile deviation
    firstHalf = int((lenofList/2)/2)  #Q1
    secondHalf = int((lenofList/2)+1) #Q2
    thirdHalf = int(secondHalf+firstHalf)
    QD = (list[thirdHalf]-list[firstHalf])/2

    #Mean Deviation
    temp = []
    for a in list:
        a = abs(a-average)
        a = round(a,3)
        temp.append(a)
    meanSum = 0
    for a in temp:
        meanSum+=a
    MD = meanSum/(lenofList+1)

    #Standard Deviation
    SD_temp = []
    SD_total = 0
    for a in temp:
        a= round(a, 3)
        SD_temp.append(a**2)

    for a in SD_temp:
        SD_total+=a
    SDAnswer = math.sqrt((SD_total/(lenofList)))
    print(f"Q1 is {list[firstHalf]}\nQ2 is {list[secondHalf]}\nQ3 is {list[thirdHalf]}")
    print(f"Average: {average}")
    print("Range is:", range)
    print("Quartile Deviation is:", QD)
    print("Mean Deviation is:", MD)
    print("Standard Deviation is:", SDAnswer)

def If_Even(input_list):
    input_list.sort() 
    lenofList = len(input_list)
    sum_ = sum(input_list)
    average = sum_ / lenofList

    # Range
    lowest = input_list[0]
    highest = input_list[-1]
    range_ = highest - lowest

    # Quartile Deviation
    firstHalfQ1 = int((lenofList / 2) / 2)
    secondHalfQ1 = int(firstHalfQ1 + 1)
    q1 = (input_list[firstHalfQ1] + input_list[secondHalfQ1]) / 2

    firstHalfQ2 = int(lenofList / 2 - 1)
    secondHalfQ2 = int(lenofList / 2)
    q2 = (input_list[firstHalfQ2] + input_list[secondHalfQ2]) / 2

    firstHalfQ3 = int(firstHalfQ2 + firstHalfQ1)
    secondHalfQ3 = int(firstHalfQ3 + 1)
    q3 = (input_list[firstHalfQ3] + input_list[secondHalfQ3]) / 2
    QD = (q3 - q1) / 2

    # Mean Deviation
    temp = [abs(a - average) for a in input_list]
    MD = sum(temp) / lenofList

    # Standard Deviation
    SD_temp = [round(a ** 2, 3) for a in temp]
    SD_total = sum(SD_temp)
    SD_Answer = math.sqrt(SD_total / (lenofList - 1))
    print(f"Q1 is {q1}\nQ2 is {q2}\nQ3 is {q3}")
    print(f"Average: {average}")
    print(f"Range: {range}")
    print(f"Quartile Deviation: {QD}")
    print(f"Mean Deviation: {MD}")
    print(f"Standard Deviation: {SD_Answer}")


x = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20,22,20,23] #Enter list here

if len(x) % 2 == 0:
    If_Even(x)
else:
    Not_Even(x)
