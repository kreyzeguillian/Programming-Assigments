# Exploratory Data Analysis on Spotify 2023 Dataset

## Table of Contents
- [Introduction](#introduction)
  - About the Dataset
  - Exploration Questions
- [Overview of the Data]
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
  - Handling Missing Values
  - Handling Data Type Inconsistencies
  - Handling Duplicates
- [Data Exploration and Analysis](#data-exploration-and-analysis)
  - Summary of Statistics
  - Data Visualization
- [References](#references)
- [About Me](#about-the-author)

## Introduction

Provide a detailed overview of your project. Explain the purpose, background, and any relevant goals. This project aims to perform an exploratory data analysis on a spotify dataset. It aims to utilize python libraries, specifically pandas, matplotlib, and seaborn to accomplish data preprocessing and visualization.

## Data Cleaning and Preprocessing
Cleaning and preprocessing the data is essential for data analysis. It considers several key aspects as the preparation of data is done by verifying its structure and relevance to ensure data quality and readiness for analysis. Here are some factors that will be taken into account in this Exploratory Analysis:
* Null values
* Data type inconsistencies
* Duplicates

### Handling Missing Values
Missing values are common in datasets, especially with large ones. Due to these values, analysis cannot be done and same goes for visualization which wastes the data's potential and neglects its importance.

The following code gives an overview of columns that contain _"NaN"_ values.
```python
print(df.isna().sum())
```
#### Output:
```
track_name               0
artist(s)_name           0
artist_count             0
released_year            0
released_month           0
released_day             0
in_spotify_playlists     0
in_spotify_charts        0
streams                  0
in_apple_playlists       0
in_apple_charts          0
in_deezer_playlists      0
in_deezer_charts         0
in_shazam_charts        50
bpm                      0
key                     95
mode                     0
danceability_%           0
valence_%                0
energy_%                 0
acousticness_%           0
instrumentalness_%       0
liveness_%               0
speechiness_%            0
dtype: int64
```
As observed above, there are two of such columns. Having a non-zero value, the columns `in_shazam_charts` and `key` is indicated to contain _"NaN"_ values. So yes, there are indeed _"NaN"_ values and to be more precise, there is **145** of them. 

In circumstances where there is a high proportion of columns containing _"NaN"_ values, it may be more practical to drop the said column rather than fill values. In the spotify dataset's case, it can be said that the _"NaN"_ values is generally low compared to the total row of **953**. Hence, we won't be dropping any column or row as it would affect the dataset's integrity.

Instead, it would be better to replace these _"NaN"_ values with something much more meaningful. Filling them with _"unrecorded"_ is a reasonable choice considering that these blank data have been disregarded:
```python
df = df.fillna('unrecorded')
print(df.isna().sum())
```
#### Output:
```
track_name              0
artist(s)_name          0
artist_count            0
released_year           0
released_month          0
released_day            0
in_spotify_playlists    0
in_spotify_charts       0
streams                 0
in_apple_playlists      0
in_apple_charts         0
in_deezer_playlists     0
in_deezer_charts        0
in_shazam_charts        0
bpm                     0
key                     0
mode                    0
danceability_%          0
valence_%               0
energy_%                0
acousticness_%          0
instrumentalness_%      0
liveness_%              0
speechiness_%           0
dtype: int64
```
### Handling Data Type Inconsistencies
The code below shows a list of each column's data type:
```python
# Prints the data type of each column
print(df.dtypes)
```
#### Output:
```
track_name              object
artist(s)_name          object
artist_count             int64
released_year            int64
released_month           int64
released_day             int64
in_spotify_playlists     int64
in_spotify_charts        int64
streams                 object
in_apple_playlists       int64
in_apple_charts          int64
in_deezer_playlists     object
in_deezer_charts         int64
in_shazam_charts        object
bpm                      int64
key                     object
mode                    object
danceability_%           int64
valence_%                int64
energy_%                 int64
acousticness_%           int64
instrumentalness_%       int64
liveness_%               int64
speechiness_%            int64
dtype: object
```
As we can observe above, some columns that are meant to be numerical are listed to have an object data type.

An object data type is a heterogeneous data type that can contain a combination of varied primitive data types. If we were to disregard such data type, we won't be able to perform mathematical functions that are necessary for data analysis.

The goal is to perform numeric conversion to some of these columns' data types. Here are the columns that need conversion:
* streams
* in_deezer_playlists
* in_shazam_charts

<details>
  <summary><strong>What about the other columns?</strong></summary>
  <p>The rest of the columns' data type can stay as it is. The only reason why we picked a select few is because of their relevance to the data. Consider the column that contains the number of streams per track. Despite being a numeric column, there is an unknown factor that is preventing it from being so</p>
</details>

The following code shows the reason for the columns' object data type:
```python
streams_column = df['streams']
deezerp_column = df['in_deezer_playlists']
shazamc_column = df['in_shazam_charts']

print(streams_column[~streams_column.str.isnumeric()], '\n')
print(deezerp_column[~deezerp_column.str.isnumeric()].head(), '\n')
print(shazamc_column[~shazamc_column.str.isnumeric()].head(), '\n')
```
#### Output:
```
574    BPM110KeyAModeMajorDanceability53Valence75Ener...
Name: streams, dtype: object

48    2,445
54    3,394
55    3,421
65    4,053
73    1,056
Name: in_deezer_playlists, dtype: object

12         1,021
13         1,281
14    unrecorded
17         1,173
24         1,093
Name: in_shazam_charts, dtype: object
```
The value that is responsible for the `streams` column's object data type can be observed above. Based on the value resulted, a minor corruption seems to have happened in the dataset. On the other hand, the column `in_deezer_playlist` seems to have string values due to the presence of the coma. The same goes for `in_shazam_charts` with an additional problem because it contains _"unrecorded"_ values due to filling the _"NaN"_ values earlier.

The following numerically converts the non-numeric column:
```python
df['streams'] = pd.to_numeric(df['streams'], errors = 'coerce')
df['in_deezer_playlists'] = pd.to_numeric(df['in_deezer_playlists'].str.replace(',', ''), errors='coerce')
df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'].str.replace(',', ''), errors='coerce')

print(df['streams'].dtype)
print(df['in_deezer_playlists'].dtype)
print(df['in_shazam_charts'].dtype)
```
#### Output:
```
float64
int64
float64
```
<details>
  <summary><strong>What does pd.to_numeric(df, errors = 'coerce') do?</strong></summary>
  <p>This pandas function converts a data frame or series' data type to a numeric data type. The additional parameter, errors = 'coerce', is responsible for replacing all non-numeric values with NaN. This is a necessary parameter as it allows for the whole column to be converted numerically.</p>
</details>
<details>
  <summary><strong>What is the purpose of str.replace(',', '')?</strong></summary>
  <p>This function is necessary to remove the coma, which is a character that is responsible for making the column an object type. Without it, pd.to_numeric() function will convert all these string values to NaN, deleting a huge chunk of important data.</p>
</details>

As observed, the columns now have been converted to a numeric data type. Being a numeric column, they are now able to be used in mathematical functions.

### Handing Duplicates
Duplicated data is another problem that often occur in raw data. Their presence could affect the results in data analysis especially when dealing with numerous of them.

The following code checks for any existing duplicates in the data frame:
```python
# Filters the rows with existing duplicates
df[df.duplicated()]
```
#### Output:
| track_name   | artist(s)_name   | artist_count   | released_year   | released_month   | released_day   | in_spotify_playlists   | in_spotify_charts   | streams   | in_apple_playlists   | in_apple_charts   | in_deezer_playlists   | in_deezer_charts   | in_shazam_charts   | bpm   | key   | mode   | danceability_%   | valence_%   | energy_%   | acousticness_%   | instrumentalness_%   | liveness_%   | speechiness_%   |
|--------------|------------------|----------------|-----------------|------------------|----------------|------------------------|---------------------|-----------|----------------------|-------------------|-----------------------|--------------------|--------------------|-------|-------|--------|------------------|-------------|------------|------------------|----------------------|--------------|-----------------|

As seen above, there are no duplicates within the data. This means that all rows are unique from each other, containing varied values.

However, this is without considering the `artist(s)_name` column. Some tracks were produced by multiple artists, hence we cannot rule out the possibility that there may have been duplicated artists.
```python
# Splits the artists' names and converts them into a list
df['artist(s)_name'] = df['artist(s)_name'].str.split(', ')

# Checks for duplicates
has_duplicates = df['artist(s)_name'].apply(lambda x: len(x) != len(set(x)))

# Filters rows that has duplicates
df[has_duplicates]
```
#### Output:
|     | track_name      | artist(s)_name                                                   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:----------------|:-----------------------------------------------------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 209 | Area Codes      | Kaliii, Kaliii                                                   |              2 |            2023 |                3 |             17 |                   1197 |                  13 | 113509496 |                   44 |                34 |                    25 |                  1 |                171 |   155 | C#    | Major  |               82 |          51 |         39 |                2 |                    0 |            9 |              49 |
| 503 | Fingers Crossed | Lauren Spencer Smith, Lauren Spencer Smith, Lauren Spencer Smith |              3 |            2022 |                1 |              5 |                   2235 |                   0 | 349585590 |                   65 |                 7 |                    70 |                 16 |                  6 |   109 | F     | Major  |               60 |          45 |         47 |               62 |                    0 |           31 |               5 |

As we can see, there are indeed duplicate artists. As part of data preprocessing, we need to remove this to avoid complications in the analysis.
```python
# Removes the duplicates
df['artist(s)_name'] = df['artist(s)_name'].apply(lambda x: list(set(x)))
df[has_duplicates]
```
#### Output:
|     | track_name      | artist(s)_name                                                   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:----------------|:-----------------------------------------------------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 209 | Area Codes      | Kaliii, Kaliii                                                   |              2 |            2023 |                3 |             17 |                   1197 |                  13 | 113509496 |                   44 |                34 |                    25 |                  1 |                171 |   155 | C#    | Major  |               82 |          51 |         39 |                2 |                    0 |            9 |              49 |
| 503 | Fingers Crossed | Lauren Spencer Smith, Lauren Spencer Smith, Lauren Spencer Smith |              3 |            2022 |                1 |              5 |                   2235 |                   0 | 349585590 |                   65 |                 7 |                    70 |                 16 |                  6 |   109 | F     | Major  |               60 |          45 |         47 |               62 |                    0 |           31 |               5 |

After removing the duplicates, let us also fix their corresponding "artist_count".

```python
df['artist_count'] = df['artist(s)_name'].str.len()
df[has_duplicates]
```
#### Output:
|     | track_name      | artist(s)_name                                                   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:----------------|:-----------------------------------------------------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 209 | Area Codes      | Kaliii, Kaliii                                                   |              2 |            2023 |                3 |             17 |                   1197 |                  13 | 113509496 |                   44 |                34 |                    25 |                  1 |                171 |   155 | C#    | Major  |               82 |          51 |         39 |                2 |                    0 |            9 |              49 |
| 503 | Fingers Crossed | Lauren Spencer Smith, Lauren Spencer Smith, Lauren Spencer Smith |              3 |            2022 |                1 |              5 |                   2235 |                   0 | 349585590 |                   65 |                 7 |                    70 |                 16 |                  6 |   109 | F     | Major  |               60 |          45 |         47 |               62 |                    0 |           31 |               5 |


## Data Exploration and Analysis

After data cleaning comes data exploration and analysis wherein we uncover patterns. In this segment, the dataset will be narrated both numerically and graphically. Patterns, relationships, correlations, as well as trends will be focused and understood, setting the foundation for further analysis.

### Summary of Statistics

The following shows the statistics of the dataset:
```python
df.describe()
```
#### Output:
|       |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   in_apple_playlists |   in_apple_charts |   in_deezer_charts |      bpm |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|:------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|---------------------:|------------------:|-------------------:|---------:|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| count |     953        |        953      |        953       |      953       |                 953    |            953      |             953      |          953      |          953       | 953      |         953      |    953      |   953      |         953      |            953       |     953      |       953       |
| mean  |       1.55614  |       2018.24   |          6.03358 |       13.9307  |                5200.12 |             12.0094 |              67.8122 |           51.9087 |            2.66632 | 122.54   |          66.9696 |     51.4313 |    64.2791 |          27.0577 |              1.58132 |      18.213  |        10.1312  |
| std   |       0.893044 |         11.1162 |          3.56644 |        9.20195 |                7897.61 |             19.576  |              86.4415 |           50.6302 |            6.0356  |  28.0578 |          14.6306 |     23.4806 |    16.5505 |          25.9961 |              8.4098  |      13.7112 |         9.91289 |
| min   |       1        |       1930      |          1       |        1       |                  31    |              0      |               0      |            0      |            0       |  65      |          23      |      4      |     9      |           0      |              0       |       3      |         2       |
| 25%   |       1        |       2020      |          3       |        6       |                 875    |              0      |              13      |            7      |            0       | 100      |          57      |     32      |    53      |           6      |              0       |      10      |         4       |
| 50%   |       1        |       2022      |          6       |       13       |                2224    |              3      |              34      |           38      |            0       | 121      |          69      |     51      |    66      |          18      |              0       |      12      |         6       |
| 75%   |       2        |       2022      |          9       |       22       |                5542    |             16      |              88      |           87      |            2       | 140      |          78      |     70      |    77      |          43      |              0       |      24      |        11       |
| max   |       8        |       2023      |         12       |       31       |               52898    |            147      |             672      |          275      |           58       | 206      |          96      |     97      |    97      |          97      |             91       |      97      |        64       |

### Data Visualization
