# Todo List App Using Python - With MySQL Database


## Steps Before you start the app:


### Step 1: Create a MySQL Database, Give any name to it as you want, Im naming it as `mytodo`


```
CREATE DATABASE mytodo;
```

```
USE mytodo;
```

<hr>

### Step 2: Create a table for the Todo Application, Give any name to it as you want, Im naming it as `tododata`


### MySQL table creation code to create the table (tododata):

```
CREATE TABLE tododata (
    Task_Number INT PRIMARY KEY,
    Task VARCHAR(255) NOT NULL,
    Task_Progress VARCHAR(50),
    Task_Added_Date DATE,
    Expected_Completion_Date DATE
);
```


> IMP NOTE: Make sure in the python code you give the proper name for your Database and Table!!