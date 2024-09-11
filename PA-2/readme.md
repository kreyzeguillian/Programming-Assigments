# PA-2 Documentation
#### Before anything else, the numpy library is imported
```
import numpy as np
```
---
1\. **NORMALIZATION PROBLEM**: Normalization is one of the most basic preprocessing techniques in data analytics. This involves centering and scaling process. Centering means subtracting the data from the mean and scaling means dividing with its standard deviation. Mathematically, normalization can be expressed as:  

<p align="center">
  $Z = \frac{X - x̄}{\sigma}$
</p>  

In Python, element-wise mean and element-wise standard deviation can be obtained by using `.mean()` and `.std()` calls.

In this problem, create a random 5 x 5 ndarray and store it to variable `X`. Normalize `X`. Save your normalized ndarray as *X_normalized.npy*.

**Code**:
```
1  # Creates a 5x5 2d array containing random values ranging from 0-1
2  X = np.random.random((5,5))
3 
4  # Prints the 5x5 array
5  print("5x5 array\n", X)
6
7  # Calculates and stores the normalized array
8  Z = (X - X.mean())/X.std()
9
10 # Prints the normalized array
11 print("Normalized array\n", Z)
12 
13 # Saves the arrays on disk
14 np.save('X_normalized', Z)
```
- **line2**: A random 2d array with size (5,5) is generated using the numpy function `.random`, and stored to variable `X`.
- **line5**: The newly created array is printed.
- **line8**: Normalization formula is applied in all the numbers within the random array. The resulting array, which is now the normalized array, is then stored to variable `Z`.
- **line11**: The normalized array is printed.
- **line14**: The normalized array stored in `Z` is saved as `X_normalized.npy`.

**Output**:
```
5x5 array
 [[0.66918045 0.20397396 0.2240664  0.04579046 0.0888551 ]
 [0.20238418 0.62631451 0.57317644 0.69110196 0.59836721]
 [0.45813194 0.93741406 0.0685882  0.32832756 0.97648851]
 [0.3412026  0.96567758 0.58598277 0.04873852 0.74004227]
 [0.06144668 0.08759669 0.22802044 0.35793601 0.70222383]]
Normalized array
 [[ 0.78849945 -0.76094771 -0.69402652 -1.28780403 -1.14437014]
 [-0.76624275  0.64572734  0.46874223  0.86151266  0.55264426]
 [ 0.08556749  1.68189587 -1.2118724  -0.34676748  1.81203979]
 [-0.30388502  1.77603221  0.51139584 -1.27798502  1.02451648]
 [-1.23565841 -1.14856149 -0.68085694 -0.24815165  0.89855591]]
```
---
2\. **DIVISIBLE BY 3 PROBLEM**: Create the following 10 x 10 ndarray.

$$
A = \begin{bmatrix}
1 & 4 & \cdots & 81 & 100 \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
\vdots & \vdots & \ddots & \vdots & \vdots \\
8281 & 8464 & \cdots & 9801 & 10000
\end{bmatrix}
$$

which are the squares of the first 100 positive integers.

From this ndarray, determine all the elements that are divisible by 3. Save the results as *div_by_3.npy*

**Code**:
```
1  # Creates a 1d array containing numbers 1-100 then takes the square of each number
2  A = (np.arange(1,101)**2)
3
4  # Reshapes the array into a 10x10 2d matrix
5  A = A.reshape(10,10)
6
7  # Prints the 10x10 array
8  print("squares of the first 100 positive integers:\n", A)
9
10 # Subsets array 'A' for all numbers divisible by 3 then stores it to 'D'
11 D = A[A%3==0]
12
13 # Prints the subset
14 print("numbers divisible by 3:\n", D)
15
16 # Saves the arrays on disk
17 np.save('div_by_3', D)
```
- **line2**: Using `.arange` function, a 1d array containing the numbers 1-100 is created and raised to the power of 2. The resulting array is then stored to variable `A`.
- **line5**: The created array is reshaped into a 10x10 2d array using the `.reshape` function.
- **line8**: The newly reshaped array is then printed.
- **line11**: A subset of array `A` is created using boolean indexing to contain all numbers divisible by 3. The subset is stored in variable `D`.
- **line14**: The newly created subset is printed.
- **line17**: The subset stored in `D` is saved as `div_by_3.npy`.

**Output**:
```
squares of the first 100 positive integers:
 [[    1     4     9    16    25    36    49    64    81   100]
 [  121   144   169   196   225   256   289   324   361   400]
 [  441   484   529   576   625   676   729   784   841   900]
 [  961  1024  1089  1156  1225  1296  1369  1444  1521  1600]
 [ 1681  1764  1849  1936  2025  2116  2209  2304  2401  2500]
 [ 2601  2704  2809  2916  3025  3136  3249  3364  3481  3600]
 [ 3721  3844  3969  4096  4225  4356  4489  4624  4761  4900]
 [ 5041  5184  5329  5476  5625  5776  5929  6084  6241  6400]
 [ 6561  6724  6889  7056  7225  7396  7569  7744  7921  8100]
 [ 8281  8464  8649  8836  9025  9216  9409  9604  9801 10000]]
numbers divisible by 3:
 [   9   36   81  144  225  324  441  576  729  900 1089 1296 1521 1764
 2025 2304 2601 2916 3249 3600 3969 4356 4761 5184 5625 6084 6561 7056
 7569 8100 8649 9216 9801]
```
