# Exploratory Data Analysis on Spotify 2023 Dataset



## Table of Contents
- Introduction
  - About the Dataset
  - Exploration Questions
  - Formatting Conventions
- Exploratory Data Analysis
  - Essentials
  - Overview of the Data
  - Data Cleaning and Preprocessing
    - Handling Missing Values
    - Handling Data Type Inconsistencies
    - Handling Duplicates
  - Data Exploration and Analysis
    - Summary of Statistics
    - Data Visualization
  - Key Insights
- References
- About Me



## Introduction

This project focuses on performing an exploratory data analysis (EDA) on a Spotify dataset, utilizing Jupyter Notebook as the primary IDE for an interactive and efficient workflow. Using Python libraries such as pandas for data preprocessing, matplotlib and seaborn for detailed visualizations, the analysis aims to uncover patterns, trends, and insights within the dataset. Through EDA, the project seeks to clean, transform, and visualize data to understand key aspects of song popularity, audio features, and streaming performance across platforms.


### About the Dataset

This dataset, created by Data Scientist Nidula Elgiriyewithana, provides a detailed look at 2023's most popular songs as highlighted on Spotify, one of the world's leading music streaming platforms known for its vast library, curated playlists, and personalized recommendations. The dataset includes more than the usual metrics, covering track names, artist/s, release dates, and streaming characteristics. It also tracks each song's presencec on Spotify playlists and charts, along with appearances on Apple Music, Deezer, and Shazam. With various musical attributes included, the dataset is a comprehensive tool for analyzing song popularity across platforms.


### Exploration Questions
The following are some questions that this EDA aims to answer:

1. Overview of Dataset  
  1.1 How many rows and columns does the dataset contain?  
  1.2 What are the data types of each column? Are there any missing values?  

2. Basic Descriptive Statistics  
  2.1 What are the mean, median, and standard deviation of the streams column?  
  2.2 What is the distribution of released_year and artist_count? Are there any noticeable trends or outliers?  

3. Top Performers  
  3.1 Which track has the highest number of streams? Display the top 5 most streamed tracks.  
  3.2 Who are the top 5 most frequent artists based on the number of tracks in the dataset?  

4. Temporal Trends  
  4.1 Analyze the trends in the number of tracks released over time. Plot the number of tracks released per year.  
  4.2 Does the number of tracks released per month follow any noticeable patterns? Which month sees the most releases?  

5. Genre and Music Characteristics  
  5.1 Examine the correlation between streams and musical attributes like bpm, danceability_%, and energy_%. Which attributes seem to influence streams the most?  
  5.2 Is there a correlation between danceability_% and energy_%? How about valence_% and acousticness_%?  

6. Platform Popularity  
  6.1 How do the numbers of tracks in spotify_playlists, spotify_charts, and apple_playlists compare? Which platform seems to favor the most popular tracks?  

7. Advanced Analysis  
  7.1 Based on the streams data, can you identify any patterns among tracks with the same key or mode (Major vs. Minor)?  
  7.2 Do certain genres or artists consistently appear in more playlists or charts? Perform an analysis to compare the most frequently appearing artists in playlists or charts.  

Note: Some questions might be answered earlier than it should be.


### Formatting Conventions
The following formatting conventions are used throughout this project to enhance clarity and readability for the reader:
* Values, in all data types, are bolded.  
  Example: **'s'**, **13**, **"Hello, World"**
* Code and output examples are presented in code blocks for easy reference  
  Example:
```python
# Code Block
```
* Variables, functions, and data types are presented in inline code formatting.  
  Example: `function_name`, `var`
* Column headers are italicized and quoted to distinguish them from regular text.  
  Example: *"sum"*, *"average"*, *"average"*
* Exploration questions and answers are italicized and bolded.  
  Example: ***Exploration Question and Answer***



## Exploratory Data Analysis
This section covers the exploratory data analysis process, including all essential steps of importing necessary libraries, data cleaning, statistical analysis, and visualization to uncover insights from the data.


### Essentials
The following code imports the necessary python libraries and dependencies that will be used in this project:
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
```
In this project, pandas is used for data preprocessing and cleaning, allowing for effective transformation of the dataset. On the other hand, matplotlib and seaborn are utilized for creating visualizations, enabling the representation of data patterns and insights through various plots.

The following imports the spotify dataset using the `pd.read_csv` function. An additional parameter of `encoding = 'ISO-8859-1'` is added within the function to read non UTF-8 csv files.
```python
df = pd.read_csv('spotify-2023.csv', encoding = 'ISO-8859-1')
```


### Overview of the Data
The following is a preview of the Spotify dataset, displayed in tabular form, showing the first few rows using `df.head()` and the last few rows using `df.tail()`:
```python
df.head()
```
Output:
|    | track_name                          | artist(s)_name   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|---:|:------------------------------------|:-----------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
|  0 | Seven (feat. Latto) (Explicit Ver.) | Latto, Jung Kook |              2 |            2023 |                7 |             14 |                    553 |                 147 | 141381703 |                   43 |               263 |                    45 |                 10 |                826 |   125 | B     | Major  |               80 |          89 |         83 |               31 |                    0 |            8 |               4 |
|  1 | LALA                                | Myke Towers      |              1 |            2023 |                3 |             23 |                   1474 |                  48 | 133716286 |                   48 |               126 |                    58 |                 14 |                382 |    92 | C#    | Major  |               71 |          61 |         74 |                7 |                    0 |           10 |               4 |
|  2 | vampire                             | Olivia Rodrigo   |              1 |            2023 |                6 |             30 |                   1397 |                 113 | 140003974 |                   94 |               207 |                    91 |                 14 |                949 |   138 | F     | Major  |               51 |          32 |         53 |               17 |                    0 |           31 |               6 |
|  3 | Cruel Summer                        | Taylor Swift     |              1 |            2019 |                8 |             23 |                   7858 |                 100 | 800840817 |                  116 |               207 |                   125 |                 12 |                548 |   170 | A     | Major  |               55 |          58 |         72 |               11 |                    0 |           11 |              15 |
|  4 | WHERE SHE GOES                      | Bad Bunny        |              1 |            2023 |                5 |             18 |                   3133 |                  50 | 303236322 |                   84 |               133 |                    87 |                 15 |                425 |   144 | A     | Minor  |               65 |          23 |         80 |               14 |                   63 |           11 |               6 |
```python
df.tail()
```
Output:
|     | track_name                | artist(s)_name     |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:--------------------------|:-------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 948 | My Mind & Me              | Selena Gomez       |              1 |            2022 |               11 |              3 |                    953 |                   0 |  91473363 |                   61 |                13 |                    37 |                  1 |                  0 |   144 | A     | Major  |               60 |          24 |         39 |               57 |                    0 |            8 |               3 |
| 949 | Bigger Than The Whole Sky | Taylor Swift       |              1 |            2022 |               10 |             21 |                   1180 |                   0 | 121871870 |                    4 |                 0 |                     8 |                  0 |                  0 |   166 | F#    | Major  |               42 |           7 |         24 |               83 |                    1 |           12 |               6 |
| 950 | A Veces (feat. Feid)      | Feid, Paulo Londra |              2 |            2022 |               11 |              3 |                    573 |                   0 |  73513683 |                    2 |                 0 |                     7 |                  0 |                  0 |    92 | C#    | Major  |               80 |          81 |         67 |                4 |                    0 |            8 |               6 |
| 951 | En La De Ella             | Feid, Sech, Jhayco |              3 |            2022 |               10 |             20 |                   1320 |                   0 | 133895612 |                   29 |                26 |                    17 |                  0 |                  0 |    97 | C#    | Major  |               82 |          67 |         77 |                8 |                    0 |           12 |               5 |
| 952 | Alone                     | Burna Boy          |              1 |            2022 |               11 |              4 |                    782 |                   2 |  96007391 |                   27 |                18 |                    32 |                  1 |                  0 |    90 | E     | Minor  |               61 |          32 |         67 |               15 |                    0 |           11 |               5 |

***Exploration Question 1.1 How many rows and columns does the dataset contain?  
Based on the preview of the dataset above, there are exactly 953 rows and 24 columns without the inclusion of the table headers.***


### Data Cleaning and Preprocessing
Cleaning and preprocessing the data is essential for data analysis. It considers several key aspects as the preparation of data is done by verifying its structure and relevance to ensure data quality and readiness for analysis. Here are some factors that will be taken into account in this Exploratory Analysis:
* Null/**NaN** values
* Data type inconsistencies
* Duplicates


#### Handling Missing Values
Missing values are common in datasets, especially with large ones. Due to these values, analysis cannot be done and same goes for visualization which wastes the data's potential and neglects its importance.

The following code gives an overview of columns that contain **NaN** values.
```python
print(df.isna().sum())
```
Output:
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

***Exploration Question 1.2 What are the data types of each column? Are there any missing values?  
To answer the second question, yes and there are two columns that contains such. Having a non-zero value, the columns *"in_shazam_charts"* and *"key"* is indicated to contain **NaN** values, and to be more precise, there is 145 of them.***

As part of the cleaning process, the following code fills these **NaN** values with **"unrecorded"**. Since these blank data were diregarded, filling them so makes it more meaningful:
```python
df = df.fillna('unrecorded')
print(df.isna().sum())
```
Output:
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


#### Handling Data Type Inconsistencies
The code below shows a list of each column's data type:
```python
# Prints the data type of each column
print(df.dtypes)
```
Output:
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

***Exploration Question 1.2 What are the data types of each column? Are there any missing values?
To answer the data type question, listed above is the data type of each column in the dataset. As we can see, only two data types are present which is `object` and `int64`.***

As we can observe in the list, some columns that are meant to be numerical are listed to have an object data type.

An object data type is a heterogeneous data type that can contain a combination of varied primitive data types. If we were to disregard such data type, we won't be able to perform mathematical functions that are necessary for data analysis.

The goal is to perform numeric conversion to some of these columns' data types. Here are the columns that need conversion:
* streams
* in_deezer_playlists
* in_shazam_charts

<details>
  <summary><strong>What about the other columns?</strong></summary>
  <p>The rest of the columns' data type can stay as it is. The only reason why we picked a select few is because of their relevance to the data. Consider the column that contains the number of streams per track. Despite being a numeric column, there is an unknown factor that is preventing it from being so</p>
</details>

The following code shows the factors that causes the columns' object data type:
```python
streams_column = df['streams']
deezerp_column = df['in_deezer_playlists']
shazamc_column = df['in_shazam_charts']

print(streams_column[~streams_column.str.isnumeric()], '\n')
print(deezerp_column[~deezerp_column.str.isnumeric()].head(), '\n')
print(shazamc_column[~shazamc_column.str.isnumeric()].head(), '\n')
```
Output:
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
The value that is responsible for the *"streams"* column's object data type can be observed above. Based on the value resulted, a minor corruption seems to have happened in the dataset. On the other hand, the column *"in_deezer_playlist"* seems to have string values due to the presence of the coma. The same goes for *"in_shazam_charts"* with an additional problem because it contains **unrecorded** values due to filling the **NaN** values earlier.

The following numerically converts the non-numeric column:
```python
df['streams'] = pd.to_numeric(df['streams'], errors = 'coerce')
df['in_deezer_playlists'] = pd.to_numeric(df['in_deezer_playlists'].str.replace(',', ''), errors='coerce')
df['in_shazam_charts'] = pd.to_numeric(df['in_shazam_charts'].str.replace(',', ''), errors='coerce')

print(df['streams'].dtype)
print(df['in_deezer_playlists'].dtype)
print(df['in_shazam_charts'].dtype)
```
Output:
```
float64
int64
float64
```
As observed, the columns now have been converted to a numeric data type. Being a numeric column, they are now able to be used in mathematical functions.

<details>
  <summary><strong>What does pd.to_numeric(df, errors = 'coerce') do?</strong></summary>
  <p>This pandas function converts a data frame or series' data type to a numeric data type. The additional parameter, errors = 'coerce', is responsible for replacing all non-numeric values with NaN. This is a necessary parameter as it allows for the whole column to be converted numerically.</p>
</details>
<details>
  <summary><strong>What is the purpose of str.replace(',', '')?</strong></summary>
  <p>This function is necessary to remove the coma, which is a character that is responsible for making the column an object type. Without it, pd.to_numeric() function will convert all these string values to NaN, deleting a huge chunk of important data.</p>
</details>


#### Handing Duplicates
Duplicated data is another problem that often occur in raw data. Their presence could affect the results in data analysis especially when dealing with numerous of them.

The following code checks for any existing duplicates in the data frame:
```python
# Filters the rows with existing duplicates
df[df.duplicated()]
```
Output:
| track_name   | artist(s)_name   | artist_count   | released_year   | released_month   | released_day   | in_spotify_playlists   | in_spotify_charts   | streams   | in_apple_playlists   | in_apple_charts   | in_deezer_playlists   | in_deezer_charts   | in_shazam_charts   | bpm   | key   | mode   | danceability_%   | valence_%   | energy_%   | acousticness_%   | instrumentalness_%   | liveness_%   | speechiness_%   |
|--------------|------------------|----------------|-----------------|------------------|----------------|------------------------|---------------------|-----------|----------------------|-------------------|-----------------------|--------------------|--------------------|-------|-------|--------|------------------|-------------|------------|------------------|----------------------|--------------|-----------------|

As seen above, there are no duplicates within the data. This means that all rows are unique from each other, containing varied values. However, this is without considering the `artist(s)_name` column. Some tracks were produced by multiple artists, hence we cannot rule out the possibility that there may have been duplicated artists.

The following checks duplicates for the *"artist(s)_name"* column:
```python
# Splits the artists' names and converts them into a list
df['artist(s)_name'] = df['artist(s)_name'].str.split(', ')

# Checks for duplicates
has_duplicates = df['artist(s)_name'].apply(lambda x: len(x) != len(set(x)))

# Filters rows that has duplicates
df[has_duplicates]
```
Output:
|     | track_name      | artist(s)_name                                                   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:----------------|:-----------------------------------------------------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 209 | Area Codes      | Kaliii, Kaliii                                                   |              2 |            2023 |                3 |             17 |                   1197 |                  13 | 113509496 |                   44 |                34 |                    25 |                  1 |                171 |   155 | C#    | Major  |               82 |          51 |         39 |                2 |                    0 |            9 |              49 |
| 503 | Fingers Crossed | Lauren Spencer Smith, Lauren Spencer Smith, Lauren Spencer Smith |              3 |            2022 |                1 |              5 |                   2235 |                   0 | 349585590 |                   65 |                 7 |                    70 |                 16 |                  6 |   109 | F     | Major  |               60 |          45 |         47 |               62 |                    0 |           31 |               5 |

As we can see, there are indeed duplicate artists. As part of data preprocessing, we need to remove this to avoid complications in the analysis:
```python
# Removes the duplicates
df['artist(s)_name'] = df['artist(s)_name'].apply(lambda x: list(set(x)))
df[has_duplicates]
```
Output:
|     | track_name      | artist(s)_name                                                   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:----------------|:-----------------------------------------------------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 209 | Area Codes      | Kaliii, Kaliii                                                   |              2 |            2023 |                3 |             17 |                   1197 |                  13 | 113509496 |                   44 |                34 |                    25 |                  1 |                171 |   155 | C#    | Major  |               82 |          51 |         39 |                2 |                    0 |            9 |              49 |
| 503 | Fingers Crossed | Lauren Spencer Smith, Lauren Spencer Smith, Lauren Spencer Smith |              3 |            2022 |                1 |              5 |                   2235 |                   0 | 349585590 |                   65 |                 7 |                    70 |                 16 |                  6 |   109 | F     | Major  |               60 |          45 |         47 |               62 |                    0 |           31 |               5 |

After removing the duplicates, let us also fix their corresponding "artist_count":
```python
df['artist_count'] = df['artist(s)_name'].str.len()
df[has_duplicates]
```
Output:
|     | track_name      | artist(s)_name                                                   |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |   streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |   bpm | key   | mode   |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|----:|:----------------|:-----------------------------------------------------------------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|----------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|------:|:------|:-------|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| 209 | Area Codes      | Kaliii, Kaliii                                                   |              2 |            2023 |                3 |             17 |                   1197 |                  13 | 113509496 |                   44 |                34 |                    25 |                  1 |                171 |   155 | C#    | Major  |               82 |          51 |         39 |                2 |                    0 |            9 |              49 |
| 503 | Fingers Crossed | Lauren Spencer Smith, Lauren Spencer Smith, Lauren Spencer Smith |              3 |            2022 |                1 |              5 |                   2235 |                   0 | 349585590 |                   65 |                 7 |                    70 |                 16 |                  6 |   109 | F     | Major  |               60 |          45 |         47 |               62 |                    0 |           31 |               5 |



### Data Exploration and Analysis

After data cleaning comes data exploration and analysis wherein we uncover patterns. In this segment, the dataset will be narrated both numerically and visually. Patterns, relationships, correlations, as well as trends will be focused and understood, setting the foundation for further analysis.


#### Summary of Statistics

The following shows the statistics of the dataset:
```python
df.describe()
```
Output:
|       |   artist_count |   released_year |   released_month |   released_day |   in_spotify_playlists |   in_spotify_charts |        streams |   in_apple_playlists |   in_apple_charts |   in_deezer_playlists |   in_deezer_charts |   in_shazam_charts |      bpm |   danceability_% |   valence_% |   energy_% |   acousticness_% |   instrumentalness_% |   liveness_% |   speechiness_% |
|:------|---------------:|----------------:|-----------------:|---------------:|-----------------------:|--------------------:|---------------:|---------------------:|------------------:|----------------------:|-------------------:|-------------------:|---------:|-----------------:|------------:|-----------:|-----------------:|---------------------:|-------------:|----------------:|
| count |     953        |        953      |        953       |      953       |                 953    |            953      |  952           |             953      |          953      |               953     |          953       |           903      | 953      |         953      |    953      |   953      |         953      |            953       |     953      |       953       |
| mean  |       1.55194  |       2018.24   |          6.03358 |       13.9307  |                5200.12 |             12.0094 |    5.14137e+08 |              67.8122 |           51.9087 |               385.188 |            2.66632 |            59.9956 | 122.54   |          66.9696 |     51.4313 |    64.2791 |          27.0577 |              1.58132 |      18.213  |        10.1312  |
| std   |       0.886215 |         11.1162 |          3.56644 |        9.20195 |                7897.61 |             19.576  |    5.66857e+08 |              86.4415 |           50.6302 |              1130.54  |            6.0356  |           161.161  |  28.0578 |          14.6306 |     23.4806 |    16.5505 |          25.9961 |              8.4098  |      13.7112 |         9.91289 |
| min   |       1        |       1930      |          1       |        1       |                  31    |              0      | 2762           |               0      |            0      |                 0     |            0       |             0      |  65      |          23      |      4      |     9      |           0      |              0       |       3      |         2       |
| 25%   |       1        |       2020      |          3       |        6       |                 875    |              0      |    1.41636e+08 |              13      |            7      |                13     |            0       |             0      | 100      |          57      |     32      |    53      |           6      |              0       |      10      |         4       |
| 50%   |       1        |       2022      |          6       |       13       |                2224    |              3      |    2.90531e+08 |              34      |           38      |                44     |            0       |             2      | 121      |          69      |     51      |    66      |          18      |              0       |      12      |         6       |
| 75%   |       2        |       2022      |          9       |       22       |                5542    |             16      |    6.73869e+08 |              88      |           87      |               164     |            2       |            37      | 140      |          78      |     70      |    77      |          43      |              0       |      24      |        11       |
| max   |       8        |       2023      |         12       |       31       |               52898    |            147      |    3.7039e+09  |             672      |          275      |             12367     |           58       |          1451      | 206      |          96      |     97      |    97      |          97      |             91       |      97      |        64       |

***Exploration Question 2.1 What are the mean, median, and standard deviation of the streams column?  
As shown in the above statistics, the *"streams"* column has a mean of **5.14e+08**, a median of **2.90e+08**, and a standard deviation of **5.66e+08**.***


#### Data Visualization

The following code plots the distribution of *"released_year"* and *"artist_count"*:
```python
# Sets the figure size to shape (12, 6)
plt.figure(figsize=(12, 6))

# Creates a subplot that has 2 plots in position 1
plt.subplot(1,2,1)

# Plots a histogram with 'released_year' as the column being considered
sns.histplot(data = df, x = 'released_year', bins=11, color = 'Red')

# Adds the necessary labels for the graph 
plt.title('Distribution of Released Year')
plt.xlabel('Released Year')
plt.ylabel('No. of Tracks Produced')

# Creates a subplot that has 2 plots in position 2
plt.subplot(1,2,2)

# Plots a histogram with 'released_year' as the column being considered
sns.histplot(data = df, x = 'artist_count', bins = 11, color='Orange')

# Adds the necessary labels for the graph 
plt.title('Distribution of Artist Count')
plt.xlabel('Number of Artists')
plt.ylabel('No. of Tracks Produced')

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/c6395f30-f4fb-4744-980c-8e2f48e1065b)

***Exploration Question 2.2 What is the distribution of released_year and artist_count? Are there any noticeable trends or outliers?  
Based on the plot, there is a noticeable increase in the number of tracks produced over the years, with a rise around the 2000's, and a much larger spike in recent years. As for artist count distribution, we can see a substantial drop for tracks involving multiple artists. Tracks with two artists are the second most common, while tracks involving three or more artists become rare.***  

***As for outliers, it can be obsrved that there are tracks in the 90's but in a very small amount. For artist count, there are some tracks that involved 8 artists, which is a signifciant outlier considering that most tracks are produced by one or two persons commonly.***

Output:
![image](https://github.com/user-attachments/assets/d0bdca8f-fdea-4820-b488-88111f3a0d18)

***Exploration Question 3.1 Which track has the highest number of streams? Display the top 5 most streamed tracks.  
As observed in the graph above, it can be seen that **"Blinding Lights"** has the highest number of streams among the top 5.***


For most frequent artists, we need to explode the artists_name column to individualize the tracks with multiple artists
```python
# Explodes the 'artist(s)_name' column
df_exploded = df.explode('artist(s)_name').reset_index(drop=True)

# Counts the total number of tracks each artist produced
artist_trackcount = df_exploded['artist(s)_name'].value_counts()

# Obtains the 5 highest values in the 'artist_trackcount'
top5_artist_intracks = artist_trackcount.nlargest(5).reset_index()

# Converts the previously listed 'artist(s)_name' column into strings
df['artist(s)_name'] = df['artist(s)_name'].apply(lambda x: ', '.join(x))
```
The following code plots the artists with most tracks produced (track collaborations are counted):
```python
# Sets the figure size to shape (10, 6)
plt.figure(figsize=(10, 6))

# Plots a horizontal barplot with 'count' and 'artist(s)_name' as x and y respectively
sns.barplot(data = top5_artist_intracks, x = 'count', y = 'artist(s)_name', hue = 'artist(s)_name', palette = 'crest')

# Adds the necessary labels for the graph
plt.title('Top 5 Artists based on Tracks Released')
plt.xlabel('Total Number of Tracks Produced')
plt.ylabel('Artists')

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/9a5b6222-23d9-46ed-8b46-52ada336a123)

***Exploration Question 3.2 Who are the top 5 most frequent artists based on the number of tracks in the dataset?  
As observed in the plot above, the top 5 most frequent artists based on the number of tracks they produced include Bad Bunny, Taylor Swift, The Weeknd, SZA, and Kendrick Lamar.***

The following counts the number of tracks released per year:
```python
# Counts the total number of tracks released per year
tracks_inyears = df['released_year'].value_counts().reset_index()
```
For plotting, the code below is implemented. A line plot is used to analyze trends over the years:
```python
# Sets the figure size to shape (12, 6)
plt.figure(figsize = (12, 6))

# Plots a line plot with 'released_year' and 'count' as x and y respectively
sns.lineplot(data = tracks_inyears, x = 'released_year', y = 'count', color = 'Blue')

# Adds the necessary labels for the graph
plt.title('Number of tracks Released per Year')
plt.xlabel('Year')
plt.ylabel('Number of Tracks')

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/aae541ed-e2f0-47aa-9ca1-2afebf86243d)

***Exploration Question 4.1 Analyze the trends in the number of tracks released over time. Plot the number of tracks released per year.
Based on the visual plot, the number of tracks produced follows the proportional increase in year produced. Tracks that are produced recently are much higher than tracks released in the 90's***

The following counts the number of tracks released per month:
```python
# Counts the total number of tracks released per month
tracks_inmonths = df['released_month'].value_counts().reset_index()
```
The following code plots the relation between month and tracks produced:
```python
# Sets the figure size to shape (12, 6)
plt.figure(figsize = (12, 6))

# Plots a barplot with 'released_month' and 'count' as x and y respectively
sns.barplot(data = tracks_inmonths, x = 'released_month', y = 'count', hue = 'released_month', palette = 'magma', legend=  False)

# Adds the necessary labels for the graph
plt.title('Number of tracks Released per Month')
plt.xlabel('Month')
plt.ylabel('Total Number of Tracks')

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/367915a0-5247-4cd8-9b68-aeb67efeb2c5)

***Exploration Question 4.2 Does the number of tracks released per month follow any noticeable patterns? Which month sees the most releases?  
Based on the plot above, the number of tracks produced seems to be on the higher side in the first half of the year. Tracks produced later in the year is not as high compared with the first half.***


The following prepares the essentials for plotting heatmaps. `corrwith()` obtains the correlation between *"streams"* and the `columns_to_plot`:
```python
# Filters the dataframe to only contain the following columns
columns_to_plot = df[['bpm', 'danceability_%', 'valence_%', 'energy_%', 'acousticness_%', 'instrumentalness_%', 'liveness_%', 'speechiness_%']]

# Calculates the correlation of each selected attribute with the 'streams' column and converts the result to a DataFrame for plotting
correlation_series = columns_to_plot.corrwith(df['streams'])
correlation_df = correlation_series.to_frame(name='Correlation with Streams')
```
The following plots a heatmap with the correlation annotated:
```python
# Sets the figure size to shape (11, 4)
plt.figure(figsize=(11, 4))

# Plots a heatmap for the data frame 'correlation_df'
sns.heatmap(correlation_df, annot=True, cmap='coolwarm')

# Adds the necessary labels for the graph
plt.title('Correlation of Streams with Musical Attributes')
plt.ylabel('Music Attributes')

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/dd61e8ab-e303-4118-9eb1-9a44849250df)

***Exploration Question 5.1 Examine the correlation between streams and musical attributes like bpm, danceability_%, and energy_%. Which attributes seem to influence streams the most?  
Having correlation coefficients of -0.11, both danceability and speechiness have the highest influence on streams. However, this is an inversely proportional relationship due to the coefficIents being negative. Aside from these two, the other columns seems to not have much of an influence compared the two.***


The following plots a heatmap of the columns *"danceability_%"*, *"valence_%"*, *"energy_%"*, and *"acousticness_%"*:
```python
# Sets the figure size to shape (12, 4)
plt.figure(figsize=(12, 4))

# Plots a heatmap for the column_filtered data frame
sns.heatmap(df.iloc[:,17:21].corr(), annot=True, cmap='viridis')

# Adds the necessary label for the graph
plt.title('Correlation Heatmap for danceability, energy, valence, and acousticness')

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/e234bdfa-df5a-4e2a-b294-3ab82fb7bdd9)

***Exploration Question 5.2 Is there a correlation between danceability_% and energy_%? How about valence_% and acousticness_%?  
Based on the graph above, there seems to be a semblance of correlation between danceability and energy. Valence and acousticness, on the other hand, has very low correlation due to its correlation coefficient being -0.082.*** 


The following prepares the data for plotting:
```python
# Obtains the sum of playlist count of each track
total_perplaylist = df[['in_spotify_playlists', 'in_apple_playlists', 'in_deezer_playlists']].sum().reset_index()

# Sets the column names to 'Platform' and 'Total Playlists' respectively
total_perplaylist.columns = ['Platform', 'Total Playlists']

# Renames the values in the 'Platform' column
total_perplaylist['Platform'] = ['Spotify Playlist', 'Apple Playlist', 'Deezer Playlist']
```
The following plots the prepared data
```python
# Sets the figure size to shape (12, 6)
plt.figure(figsize=(12,6))

# Plots a barplot with 'Platform' and 'Total Playlists' as x and y respectively
sns.barplot(data = total_perplaylist, x = 'Platform', y = 'Total Playlists', hue = 'Platform', palette = ['#1DB954', '#FF2D55', '#FF5A1F'])

# Adds the necessary label for the graph
plt.title('Total Number of Playlist per Platform')
plt.xlabel('Platform')
plt.ylabel('Total Number of Playlists')

# Displays the Plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/50834385-d750-4c75-9618-df2ff40a85b4)

***Exploration Question 6.1 How do the numbers of tracks in spotify_playlists, deezer_playlists, and apple_playlists compare? Which platform seems to favor the most popular tracks?  
Based on the output, spotify seems to significantly overwhelm the two other playlist in terms of playlist count. This means that it is spotify that favor the most popular tracks.***

The following groups the data with common *"key"* and *"mode"* values:
```python
# Groups and sums the common values in 'key' with the exception of 'unrecorded' values
key_streams_group = df[df['key'] != 'unrecorded'].groupby('key')['streams'].sum().reset_index()

# Groups and sums the common values in 'mode'
mode_streams_group = df.groupby('mode')['streams'].sum().reset_index()
```
The following plots the grouped data:
```python
# Sets the figure size to shape (12, 6)
plt.figure(figsize=(12,6))

# Creates a subplot that has 2 plots in position 1
plt.subplot(1,2,1)

# Plots a barplot with 'key' and 'streams' as x and y respectively
sns.barplot(data = key_streams_group, x = 'key', y = 'streams', hue = 'key', palette = 'rocket_r')

# Adds the necessary label for the graph
plt.title = 'Streams v.s. Key',
plt.ylabel = 'Streams'
plt.xlabel = 'Key'

# Creates a subplot that has 2 plots in position 2
plt.subplot(1,2,2)

# Plots a barplot with 'mode' and 'streams' as x and y respectively
sns.barplot(data = mode_streams_group, x = 'mode', y = 'streams', hue = 'mode', palette = 'Blues')

# Adds the necessary label for the graph
plt.title = 'Streams v.s. Key',
plt.ylabel = 'Streams'
plt.xlabel = 'Key'

# Displays the plot
plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/5e9c69d2-d039-4534-adca-c71dedb55895)

***Exploration Question 7.1 Based on the streams data, can you identify any patterns among tracks with the same key or mode (Major vs. Minor)?  
Based on the plot, tracks that are in C#, G, G# keys seems to gain the most streams. Followed by these two keys is D. For mode, it seems that tracks that have major as their mode, seems to garner higher number of streams.***


The following code groups and melts the exploded data as part of the preparation for plotting. Melting is necessary to arrange the data frame such that it would be able to graph the playlists categorically:
```python
artist_playlists_group = df_exploded.groupby('artist(s)_name')[['in_spotify_playlists', 'in_apple_playlists', 'in_deezer_playlists']].sum().reset_index()
artist_playlists_group['Total'] = artist_playlists_group.iloc[:,1:].sum(axis=1)
top5_artist_inplaylists = artist_playlists_group.nlargest(5, 'Total')
melted_df_playlist = top5_artist_inplaylists.melt(id_vars='artist(s)_name', value_vars=['in_spotify_playlists', 'in_apple_playlists', 'in_deezer_playlists', 'Total'],
                                                  var_name='Platform', value_name='Total Number of Playlists')

melted_df_playlist.rename(columns = {'artist(s)_name':'Artist'}, inplace=True)

platform_color = ['#4CAF50', '#F44336', '#FF9800', '#000000']
```
The following plots the grouped/prepared data:
```python
plt.figure(figsize=(12, 6))

sns.barplot(data=melted_df_playlist, x='Artist', y='Total Number of Playlists', hue='Platform', palette=platform_color)
plt.legend(title = "Platform")
plt.xticks(rotation=0)

plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/8e38caf8-db5f-467e-9c5d-58668def278d)

The same is done in the code below, with an addition function used to count the presence of each artist in each chart. Charts generally represent the rankings of tracks. Hence, it is unreasonable to sum the chart values. Instead, we will select non-zero values, and we will treat them as tracks that were able to reach charts. A value of 0 means that the track is not counted in the artist's presence:
```python
def convert_to_binary(x):
    if x > 0:
        return 1
    else:
        return 0

df_exploded.iloc[:,[7,10,12,13]] = df_exploded.iloc[:,[7,10,12,13]].map(convert_to_binary)

artist_charts_group = df_exploded.groupby('artist(s)_name')[['in_spotify_charts', 'in_apple_charts', 'in_deezer_charts', 'in_shazam_charts']].sum().reset_index()

artist_charts_group['Total'] = artist_charts_group.iloc[:,1:].sum(axis=1)
top5_artist_incharts = artist_charts_group.nlargest(5, 'Total')
melted_df_charts = top5_artist_incharts.melt(id_vars='artist(s)_name', value_vars=['in_spotify_charts', 'in_apple_charts', 'in_deezer_charts', 'in_shazam_charts', 'Total'],
                                             var_name='Platform', value_name='Total Number of Charts Achieved')

melted_df_charts.rename(columns = {'artist(s)_name':'Artist'}, inplace=True)

platform_color = ['#4CAF50', '#F44336', '#FF9800', '#0000FF', '#000000']
```
The following plots the resulting grouped data:
```python
plt.figure(figsize=(12, 6))

sns.barplot(data=melted_df_charts, x='Artist', y='Total Number of Charts Achieved', hue='Platform', palette=platform_color)
plt.legend(title = "Platform")
plt.xticks(rotation=0)

plt.show()
```
Output:
![image](https://github.com/user-attachments/assets/e2db501e-9dc2-457a-9e90-7f6e61c7455e)

***Exploration Question 7.2 Do certain genres or artists consistently appear in more playlists or charts? Perform an analysis to compare the most frequently appearing artists in playlists or charts.  
For both the spotify and apple playlist, it can be seen that The Weeknd appeared the most. In the deezer playlist, it is eminem that topped the lists. For the apple, spotify, and deezer charts, it is bad bunny that is most frequently seen. When it comes to shazam charts, on the other hand, it is Taylor Swift that leads the rest.***



### Key Insights
Key insights:
* Tracks produced recently are much common than tracks produced in older dates. This indicate that Spotify focuses on recently produced tracks than older ones.
* Tracks produced are higher in the first months of the year. This means artists tend to produce early at the year.
* Spotify users favor songs that are produced in major mode. For keys, they prefer those produced in C#
* Collaboration between artists is uncommon in producing tracks


## References
Spotify Dataset
ELGIRIYEWITHANA, NIDULA. “Most Streamed Spotify Songs 2023.” Www.kaggle.com, www.kaggle.com/datasets/nelgiriyewithana/top-spotify-songs-2023.

## About Me
Guillian R. Ramos
2ECE-D
guillian.ramos.eng@ust.edu.ph
