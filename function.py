#User defined function


#defining a function
'''syntax --> 

def functionName():
    #code
    #code
'''
def countWordsFromFile():
    fileName =  input("Enter the file name:- ")

    numberOfWords = 0

    file =  open(fileName, 'r')
    for line in file:
        
        words = line.split()
        numberOfWords = numberOfWords + len(words)
    print("Number of words:")
    print(numberOfWords)

#call / excution of the function 
#syntax --> functionName()
countWordsFromFile()
