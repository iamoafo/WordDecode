
# function to read data from file into a list
def readFile():
#initialize empty list
    data = []

#reads from the text file and appends the data to the list
    f = open("coding_qual_input.txt", "r")
    lines = [line.strip().split() for line in f]
    for x in lines:
        data.append(x)
#returns the list with the numbers and words data    
    return data

#Assigns the data into the getData variable 
getData = readFile()



#function to retrieve only the numbers from the list and converts it into int datatype
def getNumbers(getData): 
#initialize empty list   
    numbers=[]

#Retrieves only the numbers from the data.(The numbers are still in string format)  
    for x in getData:
        numbers.append(x[0])

#Converts the numbers into the int datatype    
    for i in range(0, len(numbers)):
        numbers[i] = int(numbers[i])

#Numbers are sorted in ascending order   
    sortedNum = sorted(numbers, key=int)
    # print(sortedNum)
    return sortedNum
    
#The sorted numbers are assigned to the sortedNumbers list to be used in a different function
sortedNumbers = getNumbers(getData)


#Function to create the number pyramid
def pyramid():
   
#Initialize empty list to hold numbers for decoding
    messageNum = []

#Initialize starting number from array of sorted numbers 
    for num in sortedNumbers: 

#outer loop to handle number of rows(limited to 20 rows)
        for i in range(0,20):

#inner loop to handle number of columns 
            for j in range(0,i+1):

#printing the numbers
                
                # print(num, end=" ")

#incrementing number at each column
                num = num +1
#assigning numbers to use for decoding the message
            decodeNumbers = num-1

#appending decode numbers into messageNum list    
            messageNum.append(decodeNumbers)

#Ending line after each row 
            print("\r")
        break

#Return messageNum list 
    return messageNum


#Assigning numbers for decoding into a new list to be used in a different function
message_num = pyramid()

#Function get decoded message from numbers.Accepts sorted numbers and initial file data as parameters
def getMessage(message_num,getData):

#Convert messageNum list into string     
    for i in range(0, len(message_num)):
        message_num[i] = str(message_num[i])
   

#Compares decode numbers to initial file data to retrieve decoded message
    for i in getData:
        if i[0] in message_num:
            print(i[1],end=" ")
    
     
#Calling function to print decoded message
getMessage(message_num,getData)
 





   

