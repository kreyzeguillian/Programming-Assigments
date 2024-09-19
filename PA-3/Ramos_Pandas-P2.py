
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
