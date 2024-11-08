# Exploratory Data Analysis on Spotify 2023 Dataset

## Table of Contents

- [Introduction](#introduction)
  - About the Dataset
  - Exploration Questions
- [Overview of the Data]
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
  - Handling Missing Values
- [Data Visualization and Analysis](#data-visualization-and-analysis)
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
#### Output
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
#### Output
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
#### Output
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
#### Output
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

For all of these columns, we use the pandas function `pd.to_numeric(df, errors = 'coerce')` to replace all non-numeric values with NaN, then convert them to a numeric data type.

The following numerically converts the non-numeric column:
```python
df['streams'] = pd.to_numeric(df['streams'], errors = 'coerce')
df['in_deezer_playlists'] = pd.to_numeric(df['in_deezer_playlists'].str.replace(',', ''), errors='coerce')
df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'].str.replace(',', ''), errors='coerce')

print(df['streams'].dtype)
print(df['in_deezer_playlists'].dtype)
print(df['in_shazam_charts'].dtype)
```
#### Output
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
Data duplicates are another problem that often occur in raw data. Their presence could affect the results in data analysis especially when dealing with numerous of them.

