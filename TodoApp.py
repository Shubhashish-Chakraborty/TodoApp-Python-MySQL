import mysql.connector as mysqlconnector
import os
import datetime



print("Welcome to the Todo App, Made by Shubhashish Chakraborty!")

myConnection = mysqlconnector.connect(
    host='localhost',
    user='root',
    passwd='root',#Ask for all These Later
    database='mytodo'
)

myCursor = myConnection.cursor()




def AddTask():

    TaskNumber = int(input("Enter Task Number:"))
    Task = input("Enter Task:")
    TaskProgress = "---"
    TaskAddedDate = datetime.date.today()
    ExpectedCompletionDate = "2024-07-14"


    query = "INSERT INTO tododata VALUES({} , '{}' , '{}' , '{}' , '{}')".format(TaskNumber,Task,TaskProgress,TaskAddedDate,ExpectedCompletionDate)

    myCursor.execute(query)
    myConnection.commit()

    if (myCursor.rowcount) > 0:

        print("Data Added")
        return True
    


def ShowTasks():


    query = "SELECT * FROM tododata"
    myCursor.execute(query)
    Tasks = myCursor.fetchall()
    
    for task in Tasks:
        
        print(list(task),'\n') #can remove the gap if you want!

    


#MAIN_MENU_DRIVE

while True:

    options = ["1-> Add Task" , "2-> Show Tasks" , "3-> EXIT"]




    optList = []

    for opt in range(len(options)):

        to_append = opt + 1
        optList.append(to_append)
        print(options[opt])


    getChoice = input(f"Enter Your Choice {optList}:")




    if (getChoice.isdigit()):

        if (int(getChoice) == 1):

            AddTask()
        
        elif (int(getChoice) == 2):
            
            ShowTasks()
        
        elif (int(getChoice) == 3): #EXIT

            break

        else:

            print("Invalid Input, Try Again!")


    else:

        print("Invalid Input, Try Again!")