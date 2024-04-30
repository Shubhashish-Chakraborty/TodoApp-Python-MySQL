import mysql.connector as mysqlconnector
import os
import datetime
import time

print()
os.system("cls")
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
    TaskNumber = int(input("Enter Task Number : "))
    Task = input("Enter Task : ")
    TaskProgress = "--pending--"
    TaskAddedDate = datetime.date.today()
    ExpectedCompletionDate = input("Enter Expected Completion Date[yyyy-MM-dd] [Enter to Skip] : ")


    # Checking Condition to skip the ExpectedCompletionDate

    if (ExpectedCompletionDate == ""):

        ExpectedCompletionDate = datetime.date.today()
    
    else:
        pass
    

    query = "INSERT INTO tododata VALUES({} , '{}' , '{}' , '{}' , '{}')".format(TaskNumber,Task,TaskProgress,TaskAddedDate,ExpectedCompletionDate)

    myCursor.execute(query)
    myConnection.commit()

    if (myCursor.rowcount) > 0:

        print("Task Added !")
        time.sleep(0.8)
        # return True
    
    os.system("cls")
    print()


def ShowTasks():


    print()
    os.system("cls")
    query = "SELECT * FROM tododata"
    myCursor.execute(query)
    Tasks = myCursor.fetchall()
    
    print(["Task_Number" , "Task" , "Task_Progress" , "Task_Added_Date" , "Expected_Completion_Date"])
    print()
    for task in Tasks:
        
        print(list(task))
    print()


def DeleteAllTask():

    print()
    os.system("cls")

    while (True):

        getPerm = input("CONFIRM DELETING ALL TASKS(y/n) : ")


        if (getPerm.lower() == "y") or (getPerm.lower() == "yes"):

            query = "DELETE FROM tododata"
            myCursor.execute(query)
            myConnection.commit()
            print("All Tasks Deleted!!")
            break
               



        elif (getPerm.lower() == "n" or (getPerm.lower() == "no")):

            break
        
    print()






def MarkComplete():

    print()
    os.system("cls")

    ShowTasks()

    print("< Select the Task Number to mark it as completed >")
    print()

    taskAmtList = []

    for num in range(1 , (myCursor.rowcount + 1)):

        taskAmtList.append(num)

    

    getTaskNumber = input(f"Select the Task to Mark Complete {taskAmtList} : ")


    if (getTaskNumber.isdigit()):

        query = "UPDATE tododata SET Task_Progress = '--Completed--' WHERE Task_Number = {}".format(getTaskNumber)

        myCursor.execute(query)
        myConnection.commit()
        print("TASK COMPLETED!!")
    else:
        print("Invalid Input, Try Again!")
        print()


    print()

def UpdateTask():

    print()


    ShowTasks()
    print("< Select the Task Number to Update the Task >")
    print()

    taskAmtList = []

    for num in range(1 , (myCursor.rowcount + 1)):

        taskAmtList.append(num)

    getTaskNumber = input(f"Select the Task to Update {taskAmtList} : ")
    print()
    
    if (getTaskNumber.isdigit()):

        getUpdation = input(f"UPDATE TASK {getTaskNumber} : ")

        query = "UPDATE tododata SET Task = '{}' WHERE Task_Number = {}".format(getUpdation,getTaskNumber)

        myCursor.execute(query)
        myConnection.commit()
        print("TASK UPDATED!!")
    else:
        print("Invalid Input, Try Again!")
        print()


    print()



#MAIN_MENU_DRIVE

while True:

    options = ["1-> Add Task" , "2-> Show Tasks" , "3-> Mark Complete" , "4-> Delete All Task" , "5-> Update Task" , "6-> EXIT\n"]




    optList = []

    for opt in range(len(options)):

        to_append = opt + 1
        optList.append(to_append)
        print(options[opt])


    getChoice = input(f"Enter Your Choice {optList} : ")




    if (getChoice.isdigit()):

        if (int(getChoice) == 1):

            AddTask()
        
        elif (int(getChoice) == 2):
            
            ShowTasks()
        
        elif (int(getChoice) == 3):
            
            MarkComplete()

        elif (int(getChoice) == 4):

            DeleteAllTask()

        elif (int(getChoice) == 5):

            UpdateTask()

        elif (int(getChoice) == 6): #EXIT

            print("Program closed successfully!")
            time.sleep(1)
            os.system('cls')
            break

        else:

            os.system("cls")
            print("Invalid Input, Try Again!")
            


    else:

        os.system("cls")
        print("Invalid Input, Try Again!")