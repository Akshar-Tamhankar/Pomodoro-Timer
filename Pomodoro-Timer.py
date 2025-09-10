# This is a simple pomodoro timer that students can use for studying. 

import time

def setup():

    print("Welcome to the Pomodoro Timer!")
    print("Please answer the following questions in whole numbers and in terms of minutes.")
    print("")

    studyTime = int(input("How much time do you want to study in one session? "))
    breakTime = int(input("How much break time do you want between sessions? "))
    sessionCount = int(input("How many sessions do you want to complete? "))

    return [studyTime, breakTime, sessionCount]

def timeControls(studyTime, breakTime, sessionCount):

    startTimer = input("Do you want to start the timer? ")

    if (startTimer.lower() == "yes"): 

        for sessions in range(sessionCount): 

            print(str(studyTime) + " " + "minutes of studying starts now!")
            time.sleep((60 * studyTime))

            print(str(breakTime) + " " + "minutes of break time starts now!")
            time.sleep((60 * breakTime))

    else:

        print("Exiting Pomodoro Timer.")
        return

    print("Pomodoro timer complete!")

timeControls(*setup())