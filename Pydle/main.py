####Pydle####
import configparser
import random
import LoadFiles
import PydleFxns
import os
from rich.console import Console
import datetime

# Console for RICH to color
console = Console()

# Vars to use
selection = ''
wordList = ''
selectedList = []
configExist = False

# Setting up config file
configFile = 'wordle.ini'
config = configparser.ConfigParser()

# Checking if the config file exists and if it has data
# Else create one with fresh data
if os.path.exists(configFile):
    config.read(configFile)
    if (config['Words']['filename'] != ''):
        wordList = config['Words']['filename']
    configExist = True
else:
    try:
        with open(f"wordle.ini", 'w') as file:
            config['Average'] = {'currentaverage': '0', 'gamesplayed': '0'}
            config['Words'] = {'filename': ''}
            config['LastPlayed'] = {'lastplayed': ''}
            config.write(file)
    except Exception as e:
        print(f"An error occurred: {str(e)}")


# ---------------------------------------------------------------------------------------------------------------- #
def menu():
    """
    Shows User the menu and ask for input
    Only Quit if Q is entered
    Keeps running in a loop if invalid response is entered
    :return: Nothing - Call other functions
    """
    # User Selection
    global selection
    # The selected List words
    global selectedList
    # Selected List name
    global wordList
    # Colorful Menu
    console.print("------Menu------", style="bold cyan")
    console.print('L : Load Library: ', style=" blue")
    console.print('C : Show Current Config: ', style=" blue")
    console.print('P : Play a New Game', style=" blue")
    console.print('Q : Run Away!', style=" yellow")

    # Get the user selection
    selection = input('Selection : ').lower()

    # Returned Tuple from loading the file has its name and contents
    selectedFile = ()
    # Just to make it easier save the name
    fileName = ''

    # If the user selects c
    if selection == 'l':
        selectedFile = LoadFiles.ShowFiles()
        fileName = (selectedFile[1])
        selectedList = selectedFile[0]
        wordList = fileName
        # Save the new loaded file to config
        try:
            config['Words']['filename'] = f'{fileName}'
            with open("wordle.ini", "w") as configF:
                config.write(configF)
        except Exception as e:
            print(f"An error occurred: {str(e)}")

    # If the user selects t
    if selection == 'c':
        ShowStats()

    # If the user selects s
    if selection == 'p':

        if wordList != '':
            #Getting the info from config file
            totalPlays = int(config['Average']['gamesplayed'])
            currentAvg = float(config['Average']['currentaverage'])
            selectedList = LoadFiles.process_file(wordList)
            #get the Correct word
            correctWord = random.choice(selectedList)
            #Save the data to the module
            PydleFxns.GuessWord(selectedList, correctWord)
            #Start the Game
            gameResult = PydleFxns.CheckWord()
            if gameResult[0]:
                console.print('Congrats You WON! DAYUM', style="green")
            else:
                console.print('LOL Get Better', style="red")
            for x in gameResult[2]:
                print(x)
            newguesses = int(gameResult[1])
            currentAvg = currentAvg*totalPlays +  newguesses
            totalPlays += 1
            newAvg = currentAvg/totalPlays
            config['Average']['gamesplayed'] = str(totalPlays)
            config['Average']['currentaverage'] = str(newAvg)
            config['LastPlayed']['lastplayed'] = str(datetime.datetime.now())

            with open("wordle.ini", "w") as configF:
                config.write(configF)

            print('Total Games Played : ' + config['Average']['gamesplayed'])
            print(f'Average : '+config['Average']['currentaverage'])
            print(f'Time Played : {datetime.datetime.now()}')
            print('------------------------')
        else:
            print('No Word List Saved - Please Go Select One!!')

def ShowStats():
    """
    Show the stats from the config file
    :return:
    """
    console.print('[Average]', style="bold red")
    console.print(f'Total Plays : ' + config['Average']['gamesplayed'], style="blue")
    console.print(f'Average Wins : ' + config['Average']['currentaverage'], style="blue")
    console.print('[Words]', style="bold red")
    console.print(f'Loaded File : {wordList}', style="blue")
    console.print('[Last Played]', style="bold red")
    console.print(f'LastPlayed : ' + config['LastPlayed']['lastplayed'], style="blue")

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    while True:
        menu()
        if selection == 'q':
            break
