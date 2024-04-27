import mysql.connector as mysqlconnector
import os
import datetime


print()
print("Welcome to the Todo App, Made by Shubhashish Chakraborty!\n")

myConnection = mysqlconnector.connect(
    host='localhost',
    user='root',
    passwd='root',#Ask for all These Later
    database='mytodo'
)

myCursor = myConnection.cursor()




def AddTask():

    print()
    TaskNumber = int(input("Enter Task Number:"))
    Task = input("Enter Task:")
    TaskProgress = "--pending--"
    TaskAddedDate = datetime.date.today()
    ExpectedCompletionDate = input("Enter Expected Completion Date[yyyy-MM-dd]:")


    query = "INSERT INTO tododata VALUES({} , '{}' , '{}' , '{}' , '{}')".format(TaskNumber,Task,TaskProgress,TaskAddedDate,ExpectedCompletionDate)

    myCursor.execute(query)
    myConnection.commit()

    if (myCursor.rowcount) > 0:

        print("Data Added")
        # return True
    


def ShowTasks():


    print()
    query = "SELECT * FROM tododata"
    myCursor.execute(query)
    Tasks = myCursor.fetchall()
    
    print(["Task_Number" , "Task" , "Task_Progress" , "Task_Added_Date" , "Expected_Completion_Date"])
    print()
    for task in Tasks:
        
        print(list(task))
    print()

    


#MAIN_MENU_DRIVE

while True:

    options = ["1-> Add Task" , "2-> Show Tasks" , "3-> EXIT\n"]




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