# Data cleansing activity for COMP0035

## Setup

Please create a Python project and install pandas and matplotlib.

If you are creating a project with a new `venv` then remember to:

- create the venv
- activate the venv
- install the requirements e.g. `pip install -r requirements.txt` or `pip install pandas matplotlib openpyxl`

Note that this activity was originally created in a Jupyter notebook, the previous .ipynb file is in the `pre-2022`
directory.

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
    df_cgd_raw_csv = pd.read_csv(cgd_raw_csv)

    # Call the data_prep function and pass the data, choose either the csv or the xslx version
    process_data(df_cgd_raw_csv)
```

### Step 3

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

