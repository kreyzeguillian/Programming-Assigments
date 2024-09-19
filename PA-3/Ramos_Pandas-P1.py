
# Imports the pandas library
import pandas as pd

# Loads the .csv file into a data frame named 'cars'
cars = pd.DataFrame(pd.read_csv('cars.csv'))

# Prints the first and last five rows of the data frame 'cars'
print(cars.head())
print(cars.tail())
