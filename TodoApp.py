import mysql.connector as mysqlconnector
import os
import datetime
import time


# Asking For Database Details:

MySQLPasswd = input("Enter your MySQL password: ")

print()
os.system("cls")

print("*"*57) # Selected the string, Looked how many characters is it holding and then replicated the stars

print("Welcome to the Todo App, Made by Shubhashish Chakraborty!")

print("*"*57 , '\n')

myConnection = mysqlconnector.connect(
    host = 'localhost',
    user = 'root',
    passwd = MySQLPasswd,
    database = 'mytodo'
)

myCursor = myConnection.cursor()




def AddTask():

    print()

    print("*"*47)

    print("< Give Valid Inputs and ADD Your Todo Tasks!! >")

    print("*"*47 , '\n')

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


    os.system("cls")

    print("*"*23)

    print("Here is All Your Tasks:")

    print("*"*23 , '\n')

    query = "SELECT * FROM tododata"
    myCursor.execute(query)
    Tasks = myCursor.fetchall()
    
    print(["Task_Number" , "Task" , "Task_Progress" , "Task_Added_Date" , "Expected_Completion_Date"])
    print()
    for task in Tasks:
        
        print(list(task))
    print()


def DeleteAllTask():


    os.system("cls")

    print("*"*36)

    print("WARNING: This Will Delete All Tasks!")

    print("*"*36 , '\n')
    
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

    
    os.system("cls")

    ShowTasks()
    print("*"*50)

    print("< Select the Task Number to mark it as completed >")

    print("*"*50 , '\n')

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


    ShowTasks()

    print("*"*45)

    print("< Select the Task Number to Update the Task >")
    
    print("*"*45 , '\n')
    

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



def RemoveCompletedTask():

    os.system("cls")

    print("*"*72)

    print("< WARNING: This will Remove All the Completed Tasks From you Todo List >")

    print("*"*72 , '\n')

    while (True):

        getPerm = input("CONFIRM REMOVING ALL THE COMPLETED TASKS(y/n) : ")


        if (getPerm.lower() == "y") or (getPerm.lower() == "yes"):

            query = "DELETE FROM tododata WHERE Task_Progress = '--Completed--'"
            myCursor.execute(query)
            myConnection.commit()
            print("Completed Tasks Deleted!!")
            break
               



        elif (getPerm.lower() == "n" or (getPerm.lower() == "no")):

            break
        
    print()


#MAIN_MENU_DRIVE

while True:

    options = ["1-> Add Task" , "2-> Show Tasks" , "3-> Mark Complete" , "4-> Delete All Task" , "5-> Update Task" , "6-> Remove Completed Tasks" , "7-> EXIT\n"]




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

        elif (int(getChoice) == 6):
            
            RemoveCompletedTask()

        elif (int(getChoice) == 7): #EXIT

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