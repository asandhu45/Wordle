
import os

def ShowFiles():
    i = 0
    fileList = loadALlFiles()
    for x in fileList:
        print(f"{i} : {x}")
        i += 1

    # List for file thing
    wordList = []

    # Get the user input
    selectF = IsNumeric("Selection [1] : ", '1')
    # Process the file to get the deque of chars
    wordList = process_file(fileList[selectF])
    return (wordList,fileList[selectF])


def process_file(name):
    """
    Open a file and extract all the character from it
    :param name:
    :return:
    """
    # check if the file exist process it if any error occurs return the error
    try:
        with open(name,'r',encoding="utf-8") as file:
            result = []
            for line in file:
                    if line.isascii() :
                        result.append(line.strip().lower())
            return result

    except FileNotFoundError:
        print(f"{name} ain't there Sir!")
        return False
    except Exception as e:
        print(f"{name} lead to an error {e}")
        return False

def loadALlFiles():
    """
    Load all the files in the default directory
    and check if its text or not
    :return: list of files
    """
    #List files
    fileList = os.listdir()
    # List of all text files
    textFileList = ['Select a File : ']
    for x in fileList:
        if x.endswith('.txt'):
            textFileList.append(x)

    #If no text file is found QUit
    if len(textFileList) < 0:
        print("No Text files found SIR!")
        quit()

    #return  the text file list
    return textFileList


def IsNumeric(msg, defau):
    """
     Determine if the input is numeric other wise use the default value
    :param msg: THe message to show to the user
    :param defau: the default value
    :return:
    """
    # Getting and checking the input
    val = input(msg) or ('defau')
    if val.isnumeric():
        return int(val)
    #Else give an error message and return the default value
    else:
        print(f"Using Default Value: {defau}")
        return int(defau)


