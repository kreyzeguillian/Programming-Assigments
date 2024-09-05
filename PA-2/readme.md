## PA-2 Documentation
#### ![image](https://github.com/user-attachments/assets/a965b897-176f-4698-84c0-6a6dc8c1b479)
##### Before anything else, the numpy library is imported
### 1. **NORMALIZATION PROBLEM**: Normalization is one of the most basic preprocessing techniques in data analytics. This involves centering and scaling process. Centering means subtracting the data from the mean and scaling means dividing with its standard deviation. Mathematically, normalization can be expressed as:
### Z = $\frac{X - x̄}{\sigma}$
### In Python, element-wise mean and element-wise standard deviation can be obtained by using .mean() and .std() calls. 
### In this problem, create a random 5 x 5 ndarray and store it to variable X. Normalize X. Save your normalized ndarray as X_normalized.npy
##### **Code**:
#### ![image](https://github.com/user-attachments/assets/ddf66572-e285-4721-b882-2e98dc9a7a53)
- ##### **line2**: A random 2d array with size (5,5) is generated using the numpy function ".random", and stored to variable 'X'.
- ##### **line5**: The newly created array is printed.
- ##### **line8**: Normalization formula is applied in all the numbers within the random array. The resulting array, which is now the normalized array, is then stored to variable 'Z'.
- ##### **line11**: The normalized array is printed.
- ##### **line14**: The normalized array stored in 'Z' is saved as 'X_normalized.npy.'
##### **Output**:
#### ![image](https://github.com/user-attachments/assets/7751ef7a-4445-46fc-a1ab-5f90fc5750ae)

### 2. **DIVISIBLE BY 3 PROBLEM**: Create the following 10 x 10 ndarray.
A = $\begin{matrix}1&4&\cdots&81&100\\\\vdots&\vdots&\ddots&\vdots&\vdots\\\\vdots&\vdots&\ddots&\vdots&\vdots\\\8281&8464&\cdots&9801&10000\end{matrix}$
### which are the squares of the first 100 positive integers.
### From this ndarray, determine all the elements that are divisible by 3. Save the results as div_by_3.npy
##### **Code**:
#### ![image](https://github.com/user-attachments/assets/e905d0e5-111b-4fff-a8cc-ebdf9f152124)
- ##### **line2**: Using ".arange" function, a 1d array containing the numbers 1-100 is created and raised to the power of 2. The resulting array is then stored to variable 'A'.
- ##### **line5**: The created array is reshaped into a 10x10 2d array using the ".reshape" function.
- ##### **line8**: The newly reshaped array is then printed.
- ##### **line11**: A subset of array 'A' is created using boolean indexing to contain all numbers divisible by 3. The subset is stored in variable 'D'.
- ##### **line14**: The newly created subset is printed.
- ##### **line17**: The subset stored in 'D' is saved as 'div_by_3.npy.'
##### **Output**:
#### ![image](https://github.com/user-attachments/assets/9bda08f2-4cf2-4725-830f-5717963187d8)
