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
code1 = """
# Imports the pandas library
import pandas as pd

# Loads the .csv file into a data frame named 'cars'
cars = pd.DataFrame(pd.read_csv('cars.csv'))

# Prints the first and last five rows of the data frame 'cars'
print(cars.head())
print(cars.tail())
"""

# Creates a python file in write mode
file1 = open('Ramos_Pandas-P1.py', 'w')
# Writes the content of 'code1' into 'file1'
file1.write(code1)
# Closes the file
file1.close()
```
- The whole code block is saved on variable `code1` as a string.
- `file1 = open('Ramos_Pandas-P1.py', 'w'` creates a file named `Ramos_Pandas-P1.py` with write mode. This returns a file object that is then stored to variable `file1`.
- `file1.write(code1)` function then writes the contents of the previously saved string `code1` to that file.
- `file1.close()` makes sure that the file is properly saved, freeing up any resources that were being used to keep the file open.
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
- The `.iloc[]` function is used to slice the data frame, displaying only the first five rows and the odd-numbered columns.
- Since we are working with odd numbers, `.iloc` is used for integer-based indexing to access data.
- In `[:5, 1::2]`, `:5` selects the first five rows, while `1::2` starts from column with index 1 and selects every second column (i.e., the odd-numbered columns, starting from 1).

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
- `[cars['Model']` refers to the column `'Model'` in the data frame.
- `'Mazda RX4']` is the specific value in the `'Model'` column that will be matched.
- `[cars['Model'] == 'Mazda RX4']` creates a condition that checks which rows have `'Mazda RX4'` as the value in the `'Model'` column. 
- Indexing with `[]` filters the rows of the data frame to display only those where the `Model` column has the value `'Mazda RX4'`.

**Output of Cell 3**:

|    | Model     |   mpg |   cyl |   disp |   hp |   drat |   wt |   qsec |   vs |   am |   gear |   carb |
|---:|:----------|------:|------:|-------:|-----:|-------:|-----:|-------:|-----:|-----:|-------:|-------:|
|  0 | Mazda RX4 |    21 |     6 |    160 |  110 |    3.9 | 2.62 |  16.46 |    0 |    1 |      4 |      4 |

**Cell 4**:
```
# Performs boolean indexing to display the row of 'Camaro Z28' and columns of 'Model' and 'cyl' 
cars.loc[cars['Model'] == 'Camaro Z28', ['Model', 'cyl']]
```
- `.loc[]` is used to filter both rows and columns based on their labes. Previously, we only filtered rows; now, we are also selecting specific columns.
- `cars['Model'] ==  'Camaro Z28'` specifies the condition to select rows where the `'Model'` column matches the value `Camaro Z28`.
- `['Model', 'cyl']` are the labels of the specific columns that will be displayed in the output.

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
- The variable `condition` stores a boolean expression that will be used to filter rows based on the value in the `'Model'` column. The `|` operator is used to combine the conditions, meaning that if any of the conditions are true, the row will be selected.
- `.loc[]` function is used to filter the data frame `cars` using the selected columns' respective labels.

**Output of Cell 5**:

|    | Model          |   cyl |   gear |
|---:|:---------------|------:|-------:|
|  1 | Mazda RX4 Wag  |     6 |      4 |
| 18 | Honda Civic    |     4 |      4 |
| 28 | Ford Pantera L |     8 |      5 |

**Cell 6**:
```
# Saves the block of code inside string variable
code2 = """
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
file2 = open('Ramos_Pandas-P2.py', 'w')
# Writes the content of 'code2' into 'file2'
file2.write(code2)
# Closes the file
file2.close()
```
- The whole code block is saved on variable `code2` as a string.
- `file2 = open('Ramos_Pandas-P2.py', 'w'` creates a file named `Ramos_Pandas-P2.py` with write mode. This returns a file object that is then stored to variable `file2`.
- `file2.write(code2)` function then writes the contents of the previously saved string `code2` to that file.
- `file2.close()` makes sure that the file is properly saved, freeing up any resources that were being used to keep the file open.
