import pandas as pd

# 2877. Create a DataFrame from List
def createDataframe(student_data: List[List[int]]) -> pd.DataFrame:
    df = pd.DataFrame(student_data,columns= ["student_id", "age"] )
    return df

# 2878. Get the Size of a DataFrame
def getDataframeSize(players: pd.DataFrame) -> List[int]:
    [r,c] = players.shape
    return [r,c]
    
# 2880. Select Data
def selectData(students: pd.DataFrame) -> pd.DataFrame:
    return students.loc[students["student_id"] == 101, "name" :]

# 2881. Create a New Column
def createBonusColumn(employees: pd.DataFrame) -> pd.DataFrame:
    employees['bonus'] = employees['salary'] * 2
    return employees

# 2882. Drop Duplicate Rows
def dropDuplicateEmails(customers: pd.DataFrame) -> pd.DataFrame:
    return customers.drop_duplicates('email')

# 2883. Drop Missing Data
def dropMissingData(students: pd.DataFrame) -> pd.DataFrame:
    return students.dropna(subset= ['name'])

# 2879. Display the First Three Rows
def selectFirstRows(employees: pd.DataFrame) -> pd.DataFrame:
    top_3 =employees.head(3)
    return top_3
    