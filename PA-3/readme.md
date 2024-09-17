# PA-3 Documentation
#### Before anything else, the `cars.csv` file is placed within the same directory as the notebook
![Alt text](https://github.com/kreyzeguillian/Programming-Assigments/blob/main/PA-3/ss.png)  
---
1\. **PROBLEM 1**: Save your file as Surname_Pandas-P1.py  

Using knowledge obtained from the experiment and demonstrations:  

&nbsp;&nbsp;&nbsp;&nbsp;a. Load the corresponding .csv file into a data frame named cars using pandas  

&nbsp;&nbsp;&nbsp;&nbsp;b. Display the first five and last five rows of the resulting cars.

### **Code/Explanations**:  

**Cell 1**:
```
# Imports the pandas library
import pandas as pd

# Loads the .csv file into a data frame named 'cars'
cars = pd.read_csv('cars.csv')
```
- The pandas library is imported as `pd` and the `cars.csv` file that contains the dataframe is stored to variable `cars`.
  
**Cell 2**:
```
# Prints the first five rows of the data frame 'cars'
cars.head()
```
- The first five rows of the data frame is printed using function `.head(default = 5)`.

**Output of Cell 2**:

|    | Model             |   mpg |   cyl |   disp |   hp |   drat |    wt |   qsec |   vs |   am |   gear |   carb |
|---:|:------------------|------:|------:|-------:|-----:|-------:|------:|-------:|-----:|-----:|-------:|-------:|
|  0 | Mazda RX4         |  21   |     6 |    160 |  110 |   3.9  | 2.62  |  16.46 |    0 |    1 |      4 |      4 |
|  1 | Mazda RX4 Wag     |  21   |     6 |    160 |  110 |   3.9  | 2.875 |  17.02 |    0 |    1 |      4 |      4 |
|  2 | Datsun 710        |  22.8 |     4 |    108 |   93 |   3.85 | 2.32  |  18.61 |    1 |    1 |      4 |      1 |
|  3 | Hornet 4 Drive    |  21.4 |     6 |    258 |  110 |   3.08 | 3.215 |  19.44 |    1 |    0 |      3 |      1 |
|  4 | Hornet Sportabout |  18.7 |     8 |    360 |  175 |   3.15 | 3.44  |  17.02 |    0 |    0 |      3 |      2 |

**Cell 3**:
```
# Prints the last five rows of the data frame 'cars'
cars.head()
```
- The last five rows of the data frame is displayed using function `.tail(default = 5)`.

**Output of Cell 3**:  

|    | Model          |   mpg |   cyl |   disp |   hp |   drat |    wt |   qsec |   vs |   am |   gear |   carb |
|---:|:---------------|------:|------:|-------:|-----:|-------:|------:|-------:|-----:|-----:|-------:|-------:|
| 27 | Lotus Europa   |  30.4 |     4 |   95.1 |  113 |   3.77 | 1.513 |   16.9 |    1 |    1 |      5 |      2 |
| 28 | Ford Pantera L |  15.8 |     8 |  351   |  264 |   4.22 | 3.17  |   14.5 |    0 |    1 |      5 |      4 |
| 29 | Ferrari Dino   |  19.7 |     6 |  145   |  175 |   3.62 | 2.77  |   15.5 |    0 |    1 |      5 |      6 |
| 30 | Maserati Bora  |  15   |     8 |  301   |  335 |   3.54 | 3.57  |   14.6 |    0 |    1 |      5 |      8 |
| 31 | Volvo 142E     |  21.4 |     4 |  121   |  109 |   4.11 | 2.78  |   18.6 |    1 |    1 |      4 |      2 |

**Cell 4**:
```
# Saves the block of code inside string variable
code = """
# Imports the pandas library
import pandas as pd

# Loads the .csv file into a data frame named 'cars'
cars = pd.DataFrame(pd.read_csv('cars.csv'))

# Prints the first and last five rows of the data frame 'cars'
print(cars.head())
print(cars.tail())
"""

# Creates a python file in write mode
file = open('Ramos_Pandas-P1.py', 'w')
# Writes the content of 'code' into 'file'
file.write(code)
# Closes the file
file.close()
```
- 
---
2\. **PROBLEM 2**: Save your file as Surname_Pandas-P2.py

Using the dataframe cars in problem 1, extract the following information using subsetting, slicing and indexing operations.

&nbsp;&nbsp;&nbsp;&nbsp;a. Display the first five rows with odd-numbered columns (columns 1, 3, 5, 7…) of cars.

&nbsp;&nbsp;&nbsp;&nbsp;b. Display the row that contains the ‘Model’ of ‘Mazda RX4’.

&nbsp;&nbsp;&nbsp;&nbsp;c. How many cylinders (‘cyl’) does the car model ‘Camaro Z28’ have?

&nbsp;&nbsp;&nbsp;&nbsp;d. Determine how many cylinders (‘cyl’) and what gear type (‘gear’) do the car models ‘Mazda RX4 Wag’, ‘Ford Pantera L’ and ‘Honda Civic’ have.

### **Code/Explanations**:  

**Cell 1**:
```
# Imports the pandas library
import pandas as pd

# Loads the .csv file into a data frame named 'cars'
cars = pd.read_csv('cars.csv')
```
- The pandas library is imported as `pd` and the `cars.csv` file that contains the dataframe is stored to variable `cars`.

**Cell 2**:
```
# Performs slicing to print the first five rows with odd-numbered columns of data frame 'cars'
cars.iloc[:5, 1::2]
```
- Using the `.iloc[]` function, the data frame is sliced to display only the first five rows and the odd-numbered columns
- Since we are to deal with odd numbers, `.iloc` is used to allow data access using integer-based indexing
- In `[:5, 1::2]`, `:5` is inputted to display the first five rows while `1::2` is placed to display the column with index 1, then increases with step 2, to display the odd columns.

**Output of Cell 2**:

|    |   mpg |   disp |   drat |   qsec |   am |   carb |
|---:|------:|-------:|-------:|-------:|-----:|-------:|
|  0 |  21   |    160 |   3.9  |  16.46 |    1 |      4 |
|  1 |  21   |    160 |   3.9  |  17.02 |    1 |      4 |
|  2 |  22.8 |    108 |   3.85 |  18.61 |    1 |      1 |
|  3 |  21.4 |    258 |   3.08 |  19.44 |    0 |      1 |
|  4 |  18.7 |    360 |   3.15 |  17.02 |    0 |      2 |

**Cell 3**:
```
# Performs boolean indexing to display the row that contains 'Mazda RX4'
cars[cars['Model'] == 'Mazda RX4']
```
- Indexing with `[]`, the rows in the column `Model` is filtered to display only the `Model` with value `'Mazda RX4'`.
- `[cars['Model']` refers to the column `'Model'` will be the one that is filtered.
- `'Mazda RX4']` refers to the value of the column that will be selected.
- `[cars['Model'] == 'Mazda RX4']` refers to the condition that will allow selection

**Output of Cell 3**:

|    | Model     |   mpg |   cyl |   disp |   hp |   drat |   wt |   qsec |   vs |   am |   gear |   carb |
|---:|:----------|------:|------:|-------:|-----:|-------:|-----:|-------:|-----:|-----:|-------:|-------:|
|  0 | Mazda RX4 |    21 |     6 |    160 |  110 |    3.9 | 2.62 |  16.46 |    0 |    1 |      4 |      4 |

**Cell 4**:
```
# Performs boolean indexing to display the row of 'Camaro Z28' and columns of 'Model' and 'cyl' 
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```
- In the previous cell, only the rows has been filtered with the conditiond depending on the value of `Model`. Now, we are indexing through `.loc[]` to be able to filter the columns and use their respective labels.
- `cars['Model'] ==  'Camaro Z28'` refers to the condition for selecting rows only with models `Camaro Z28`.
- `['Model', 'cyl']` refers to the columns that will be displayed by using their labels.

**Output of Cell 4**:

|    | Model      |   cyl |
|---:|:-----------|------:|
| 23 | Camaro Z28 |     8 |

**Cell 5**:
```
# Stores the 'Model' conditions for simplification
condition = (cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic')

# Performs boolean indexing to display the given 'Model' and columns of 'cyl' and 'gear'
cars.loc[condition, ['Model', 'cyl', 'gear']]
```
- 

**Output of Cell 5**:

|    | Model          |   cyl |   gear |
|---:|:---------------|------:|-------:|
|  1 | Mazda RX4 Wag  |     6 |      4 |
| 18 | Honda Civic    |     4 |      4 |
| 28 | Ford Pantera L |     8 |      5 |

**Cell 6**:
```
# Saves the block of code inside string variable
code = """
# Imports the pandas library
import pandas as pd

# Loads the .csv file into a data frame named 'cars'
cars = pd.DataFrame(pd.read_csv('cars.csv'))

# Performs slicing to print the first five rows with odd-numbered columns of data frame 'cars'
print(cars.iloc[:5, 1::2])

# Performs boolean indexing to display the row that contains 'Mazda RX4'
print(cars[cars['Model'] == 'Mazda RX4'])

# Performs boolean indexing to display the row of 'Camaro Z28' and columns of 'Model' and 'cyl' 
print(cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']])

# Stores the 'Mode' conditions for simplification
condition = (cars['Model'] == 'Mazda RX4 Wag') | (cars['Model'] == 'Ford Pantera L') | (cars['Model'] == 'Honda Civic')

# Performs boolean indexing to display the given 'Model' and columns of 'cyl' and 'gear'
print(cars.loc[condition, ['Model', 'cyl', 'gear']])
"""

# Creates a python file in write mode
file = open('Ramos_Pandas-P2.py', 'w')
# Writes the content of 'code' into 'file'
file.write(code)
# Closes the file
file.close()
```
- 
