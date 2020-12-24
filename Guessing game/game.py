#importing the Library ,in the whole program it will be referenced by SG
import PySimpleGUI as sg 
import random

#Global varaibles
upperRangeNo = 0
g= 0


#Setting up theme for GUI Window
sg.theme('dark grey 9')


# Define the window's contents
layout = [[sg.Text("Enter upper bound no for the game")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(80,5), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')] ]




# Create the window
window = sg.Window('THE GUESSING GAME', layout)

# Display and interact with the Window using an Event Loop
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    elif event == 'Ok':
     guessoption = int(values['-INPUT-'])
     print(guessoption) 
     upperRangeNo = guessoption
     window.close()   
     
#layout 2 FOR SECOND WINDOW
layout2 = [
    
          [sg.Text(F"GUESS THE  no for the game Which is between 1 and {upperRangeNo}")],
          [sg.Input(key='-INPUT-')],
          [sg.Text(size=(80,5), key='-OUTPUT-')],
          [sg.Button('Ok'), sg.Button('Quit')] 
]
#CREATE A SECOND WINDOW    
window = sg.Window('THE GUESSING GAME', layout2)
while True:
    event, values = window.read()
    # See if user wants to quit or window was closed
    if event == sg.WINDOW_CLOSED or event == 'Quit' :
        break 

    if  event == 'Ok':
        x= upperRangeNo 
        random_no = random.randint(1,x) 
        g= int(values['-INPUT-'])
        print(random_no)
        if g < random_no:
            window['-OUTPUT-'].update("sorry the no is too low. ")
        elif g > random_no:
            window['-OUTPUT-'].update("sorry the no is too high. ")
        elif g== random_no:
            window['-OUTPUT-'].update(f"yay!! you probably guessed the random no {random_no}:") 

    

  
# Finish up by removing from the screen
window.close()
sg.popup_auto_close("Thank you for using this game",title="Thank you screen ",location=(500,555)) 

           
