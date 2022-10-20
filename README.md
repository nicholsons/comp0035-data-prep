# Data cleansing activity for COMP0035

## Setup

Please create a Python project and install pandas and matplotlib.

If you are creating a project with a new `venv` then remember to:

- create the venv
- activate the venv
- install the requirements e.g. `pip install -r requirements.txt` or `pip install pandas matplotlib openpyxl`

## Acknowledgements

The idea for this activity was inspired by an article published in the Centre for Global Development by Shelby Carvalho
and Lee Crawford on 25th March 2020 called [School’s Out: Now What?](https://www.cgdev.org/blog/schools-out-now-what).

The data set used is that referred to in the article and was
made [publicly available here by the Centre for Global Development]( https://docs.google.com/spreadsheets/d/1ndHgP53atJ5J-EtxgWcpSfYG8LdzHpUsnb6mWybErYg/edit?ts=5e6f893e#gid=0)
. The data set builds on UNESCO data on global school closures and gives detail about the closures and other support
countries are providing whilst schools are closed.

## Activity guidance

Data cleansing and preparation is one of the early steps in any data science project. There is evidence that data
scientists spend up to 70% of their time cleaning data.

This activity walks you through an example of some initial steps of data cleansing in Python.

The dataset that we will use for this activity has already been downloaded and is available as `cgd_raw.csv`
or `cgd_raw.xlsx`. The dataset was downloaded from the Centre for Global Development.

Let's assume that the aim of the project is to answer the question:

> "At what point in the Covid pandemic should a country close schools?"

We are going to try to answer this by creating a bar chart showing the median reported cases of Covid at the time
schools were closed in each region. This activity focuses on preparing the data that would be needed in the bar chart.

In this illustration, we will create the bar chart; however this is not part of the data preparation and cleaning phase.

This is a simplistic use of the data set, however it introduces the concept of data cleaning.

### Step 1 Create a python file, import pandas and create an empty function for your code

For example, you could:

- Create a python file e.g. data_prep.py
- From pathlib import Path (this will be used to reference the data file in a way that should work for Windows and
  macOS)
- Import the pandas library
- Create a `process_data` function
- Add a main function that you will later use to run the `process_data` function

```python
from pathlib import Path
import pandas as pd


def process_data(data):
    """
    Main function to introduce pandas functions for data preparation and understanding.

    Uses the CGD example data set for tracking school closures during the Covid pandemic.

    Args:
        data: Pandas dataframe of the Covid data

    Returns:
        None
    """
    pass


if __name__ == "__main__":
    pass


```

### Step 2 Open the data file

Add code to the `main` function to open the data file and then pass this as an argument to the `process_data` function.

The following shows the syntax for either excel or csv, you don't need to use both, pick one!

```python
if __name__ == "__main__":
    # Define the path to the csv and excel versions of the datafile in a way that works on both Mac and Windows
    cgd_raw_csv = Path(__file__).parent.joinpath('data', 'cgd_raw.csv')
    cgd_raw_xlsx = Path(__file__).parent.joinpath('data', 'cgd_raw.xlsx')

    # Load the xlsx file into a pandas DataFrame and skip the first line which contains the logo
    df_cgd_raw_xlsx = pd.read_excel(cgd_raw_xlsx, sheet_name='School closure tracker- Global', skiprows=1)

    # Load the csv file into a pandas DataFrame
    df_cgd_raw_csv = pd.read_csv(cgd_raw_csv, skiprows=1)

    # Call the data_prep function and pass the data, choose either the csv or the xslx version
    process_data(df_cgd_raw_csv)
```

### Step 3 Explore the shape of the data

Using pandas, add to the `process_data` function code to explore:

- the number of rows and columns
- the data types of the columns
- the first few rows of data

```python
def process_data(data):
    # Dataframe with the data
    df = data
    # Print the total number of rows and columns in the DataFrame
    print(df.shape)
    # Print the column headings only
    print(df.columns)
    # Print details about the rows and columns, including data types
    print(df.info(verbose=True))
    # Print the first 5 rows
    print(df.head(5))
```

The columns printed will be truncated to the width of the terminal. You can show all the columns by setting the view in
pandas to be the width of the dataset (or you can specify a particular number).

```python
# Set pandas display options to the number of columns and tows in the dataframe
pd.set_option('display.max_rows', df.shape[0] + 1)
pd.set_option('display.max_columns', df.shape[1] + 1)
```

### Step 4 Delete unnecessary columns

Delete columns that you either don't need or contain values that you are not useful to you. In this example we don't
need the columns with URLs and large amounts of text.

The pandas DataFrame `drop()` method can be used to delete columns.

The following code shows examples of some ways you can remove
columns. [See Pandas documentation](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.drop.html)
for more details.

```python
# Remove a single column with the name 'Source for Re-opening'. The parameter axis=1 refers to a column (row would be axis=0).
df = df.drop(['Source for Re-opening'], axis=1)

# Remove two columns named 'Facebook Page' and 'Official COVID Education Policy Document'
df = df.drop(['Facebook Page', 'Official COVID Education Policy Document'], axis=1)

# Remove columns 40 and 41
df = df.drop(df.columns[[40, 41]], axis=1)

# Check the final 5 columns have been removed
print(df.columns)
print(df.shape)  # Should have 40 columns instead of 45
```

> Challenge: Add your own code to remove at least one other unnecessary column.

### Step 5 Handle missing values

Missing values can be the most common feature of unclean data. These values are usually in the form of NaN or None.

There are many reasons for values to be missing, for example because they don't exist, or because of improper data
collection or improper data entry. For example, if someone is underage and the issue applies to someone older than 18,
the question will contain missing values.

There are many ways to deal with missing values:

- Do nothing (this may be appropriate in some circumstances).
- If your data set is large enough and/or the percentage of missing values is high, you may choose to delete the rows
  and columns that contain the missing data;
- Use an imputation technique to fill the missing values (e.g. mean, median, most frequent etc)

The decision will depend on the type of data, the actions you want to perform on the data, and the reasons for the
missing
values. [This article on Towards Data Science](https://towardsdatascience.com/6-different-ways-to-compensate-for-missing-values-data-imputation-with-examples-6022d9ca0779)
gives pros and cons of some common imputation techniques. You are not expected to understand the specific imputation
techniques and make an informed choice to apply to your coursework. For this course it is sufficient that you understand
the implications of missing data and make an informed decision whether to do nothing, remove data or use imputation.

[The pandas documentation](https://pandas.pydata.org/pandas-docs/stable/user_guide/missing_data.html) explains how to
work with missing data.

Let's add code to delete all rows that have empty columns and any columns that have more than 50% of the values missing:

```python
  # MISSING VALUES

# Count the number of rows where all the columns are empty (null)
print(df.isna().all(axis=1).sum())

# Remove the rows where all columns are empty
# Pandas would return a copy of the dataset, however we want to replace it rather than copy
# To do this you can re-assign the variable name (as below) or
# using the 'inplace=True' parameter:   df.dropna(how='all', inplace=True)
df = df.dropna(how='all')

# Print the columns showing the % of missing values
print(df.isnull().sum() / len(df))

# Delete columns that have more than 50% of the values missing
half_count = len(df) / 2
df = df.dropna(thresh=half_count, axis=1)

# Print the shape of the data; the number of columns should be reduced
print(df.shape)

```

### Step 6 Handle inconsistent values

When there are different unique values in the column, an inconsistency can occur. Examples include:

- **Text data**: Imagine a text field that contains 'Juvenile', 'juvenile' and ' juvenile ' in the same column, you
  could remove spaces and convert all data to lowercase. If there are a large number of inconsistent unique entries, you
  cannot manually check the closest match, in which case there are various packages that can be used (e.g. Fuzzy Wuzzy
  string matching).
- **Date/time data**: Inconsistent date format, such as dd / mm / yy and mm / dd / yy in the same column. Your date
  value may not be the correct data type, which will not allow you to perform actions efficiently and gain insight from
  it.

Add code to check for date formats in the `Date` columns and find the unique values in the `School closures` column.

```python
    # INCONSISTENT VALUES

# Print the unique values in the `Date` column
print(df['Date'].unique())

# Print the unique values in the `School Closures` column
print(df['School Closures'].unique())
```

The 'Date' column appears OK, however the values in the 'School Closures' suggest there may be different terms used for
the same meaning:

```text
'Yes' 
'Yes '
'Yes (some areas)' 
'Yes (partial)' 
'Yes (some)' 
'No' 
nan 
```

### Step 6 Add, or compute, additional data

We need to calculate the median Covid cases at the date of closure for a region.

We can aggregate the data in the region column using ‘Group By’ and then calculate the median for the number of cases.

```python
df.groupby("Region")["Cases"].median()
```

However, if you check the datatype of the ‘Cases’ column by entering `print(df.types)` you will see that ‘Cases’ has a
datatype of Object rather than int. We cannot calculate a median for an object datatype so we first need to convert it
to a numeric format.

```python
# Rename the column 'Number of confirmed cases at time of closure' to 'Cases'
df = df.rename(columns={'Number of confirmed cases at time of closure': 'Cases'})

# Change the datatype to numeric
df["Cases"] = pd.to_numeric(df["Cases"], errors="coerce")

# Aggregate on median cases per region
chart_df = df.groupby("Region")["Cases"].median()
```

### Step 7 Visualise the data as a final check

Let's have a look at the data to see if we do have the data we will need for our final chart.

We will create a 'quick and dirty' chart; that is we won't spend any time formatting it for visual impact.

To do this we will need code that will render the chart so add the import `import matplotlib.pyplot as plt`

Create
a [horizontal bar chart](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.plot.barh.html#pandas.DataFrame.plot.barh)
.

```python
import matplotlib.pyplot as plt

# Draw a horizontal bar chart
chart_df.plot.barh(x="Region", y="Cases", title="Median number of reported COVID-19 cases at school closure, by region")

# Show the chart
plt.show()
```

### Step 8 Save the prepared data

You may wish to save the prepared data rather than repeating the cleaning steps.

Add this code before the `plt.show()` otherwise the code won't run until you close the plot window.

```python
    # Save the chart DataFrame back to a new csv. 
chart_csv_name = Path(__file__).parent.joinpath('data', 'chart_data.csv')
chart_df.to_csv(chart_csv_name)

# The DataFrame before the grouping to a new xlsx. 'index=False' indicates that row names should not be saved.
prepared_data_xlsx_name = Path(__file__).parent.joinpath('data', 'prepared_data.xlsx')
df.to_excel(prepared_data_xlsx_name, index=False)
```
