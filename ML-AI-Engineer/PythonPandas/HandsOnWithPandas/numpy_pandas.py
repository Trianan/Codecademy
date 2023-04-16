import numpy as np
import pandas as pd


# ----------------------------------------------------------------------------------------------------------------------

def print_rule(length=80):
    print('-'*length)


# ----------------------------------------------------------------------------------------------------------------------
# NUMPY ARRAYS AND PANDAS DATAFRAMES:

# Turning list into Numpy n-dimensional array:
list_2d = [[1, 0, 2, 1], [0, 1, 2, 2], [1, 0, 2, 0], [1, 0, 0, 0]]
ndarray = np.array(list_2d)
print(list_2d, type(list_2d))
print(ndarray, type(ndarray))
print_rule()

# Operations are performed on all elements of numpy array without iterating through array.
print(ndarray * 7)
print_rule()
# Including more complex expressions:
print(((ndarray + 1) * 7) % 2)
print_rule()

# Creating a Pandas Series object from a numpy array (can also use lists, dictionaries, and scalar values).
list_1d = [3, 7, 1, 5, 3]
ndarray = np.array(list_1d)
indexed_series = pd.Series(ndarray)
print(indexed_series)
print_rule()
# Creating labels for the Series objects elements.
labelled_series = pd.Series(ndarray, index=['Apples', 'Bananas', 'Kiwis', 'Pears', 'Watermelons'])
print(labelled_series)
print_rule()

# Creating a Pandas DataFrame. Each column must contain one data type, and all columns must have the
# same number of elements, such that the DataFrame may rely on all rows containing the same number of
# columns when creating its table-like representation of the data:
inventory = [
    ['apple', 253, 2.19],
    ['pear', 120, 3.40],
    ['banana_bunch', 201, 2.45],
    ['kiwi', 86, 4.25],
    ['mango', 35, 5.10],
    ['strawberries_2kg', 86, 6.64],
    ['blueberries_500g', 60, 5.50],
    ['lemons', 198, 2.30]
]
# Columns given names as argument for columns parameter.
inventory_frame = pd.DataFrame(inventory, columns=['item', 'count', 'price'])
print(inventory_frame)
print_rule()

# We can set the indexing to one of the columns like so:
print(inventory_frame.set_index('item'))
print_rule()
# Does not have to be the first column:
print(inventory_frame.set_index('price'))
print_rule()

# Using Pandas to create a list of dates:
month = pd.date_range('20230401', periods=30)
print(month)
print_rule()

# Using a list not within the dataframe as an index.
measurements = pd.DataFrame(
    np.random.randn(len(month), 3),
    index=month,
    columns=['reading_1', 'reading_2', 'reading_3']
)
print(measurements)
print_rule()

# Constructing a dataframe from a dictionary:
statuses = np.random.randint(0, 6, len(month))
status_reports = pd.DataFrame(
    {
        'type': 'status_report',
        'date': month,
        'status': statuses,
        'priority': ['action_needed' if status > 2 else 'low_priority' for status in statuses]
    }
)
print(status_reports)
print(status_reports.dtypes)
print_rule()

# ----------------------------------------------------------------------------------------------------------------------
# VIEWING DATA IN A DATAFRAME:

# Viewing the first and last rows of a dataframe:
print(status_reports.head(3))
print(status_reports.tail(3))

# Viewing the indices and columns:
print(status_reports.index)
print(status_reports.columns)
print_rule()

# Converting dataframe to numpy array (note all data types were converted to objects so array can contain same type):
status_reports_ndarray = status_reports.to_numpy()
print(status_reports_ndarray, status_reports_ndarray.dtype)
print_rule()

# Using the extremely useful describe() function in order to summarize a dataframe:
print(status_reports.describe())
print_rule()

# Transposing dataframe:
print(status_reports.T)
print_rule()

# Sorting dataframe by axes:
print(status_reports.sort_index(ascending=False))  # Sort rows in descending order.
print_rule()

print(status_reports.sort_index(axis=1))  # Sorting columns in alphabetical order.
print_rule()

# Sorting dataframe by value:
print(status_reports.sort_values(by='status'))
print_rule()

# ----------------------------------------------------------------------------------------------------------------------
# GETTING ROW OR COLUMN:

# Getting a single column from a dataframe:
print(status_reports['status'])
print(status_reports.status)  # Equivalent syntax.
print_rule()

# Getting a selection of rows:
print(status_reports[0:5])
print(status_reports.set_index('date')['20230401':'20230405'])  # Indexes can be a range of dates.
print_rule()

# ----------------------------------------------------------------------------------------------------------------------
# SELECTING BY LABEL FROM DATAFRAME:

print(status_reports.loc[0])
print(status_reports.set_index('date').loc[month[0]])
print_rule()

# Selecting by both axes:
print(status_reports.loc[:6, ['date', 'status']])  # Note the range for rows is inclusive.
print_rule()

# Getting a single row with reduced dimensions:
print(status_reports.loc[0, ['date', 'status']])
print_rule()

# Getting a scalar value:
print(status_reports.loc[0, 'status'])
print(status_reports.at[0, 'status'])  # Equivalent syntax.
print_rule()

# ----------------------------------------------------------------------------------------------------------------------
# SELECTING BY POSITION:

print(status_reports.iloc[0:5])  # When accessing by location index, the upper bound is excluded.
print(status_reports.iloc[:5, :])  # Equivalent to slicing by row.
print(status_reports.iloc[:, 1:])  # Slicing by column.
print_rule()

print(status_reports.iloc[1:6, 1:3]) # Selecting by a range of rows and columns positionally.
print(status_reports.iloc[[1, 3, 5], [1, 3]])  # Using list of rows and columns to select.
print_rule()

# Selecting a single value by position:
print(status_reports.iloc[1, 1])
print(status_reports.iat[1, 1])  # Faster method to do equivalent.
print_rule()

# ----------------------------------------------------------------------------------------------------------------------
# BOOLEAN INDEXING

# Using a single columns values to select through conditional expression:
print(status_reports[status_reports['priority'] == 'action_needed'])
print_rule()

grid = pd.DataFrame(
    np.array([
        [5, 6, 5],
        [2, 3, 7],
        [0, 2, 3],
        [2, 3, 5]
    ]),
    columns=list('ABC')
)
# Selecting all values in dataframe which match conditional.
print(grid)
print(grid[grid % 2 == 0])  # Notice non-matching values are converted to NaN.
print_rule()

# Selecting whether based on whether a value exists in a container:
print(grid['B'].isin([3, 6, 9]))  # Returns True or False for each row.
print(grid[grid['B'].isin([3, 6, 9])])  # Uses previous as conditional for selection.
print_rule()

# ----------------------------------------------------------------------------------------------------------------------
# SETTING:

range_table = range(1, 20)
max_multiple = 10
num_table = pd.DataFrame(
    {
        'square': [n**2 for n in range_table],
        'cube': [n**3 for n in range_table],
        'multiples': [[n*m for m in range(1, max_multiple)] for n in range_table]
    },
    index=range_table
)
print(num_table)

# Adding a new column automatically aligns values with indices.
factorials = pd.Series([np.math.factorial(n) for n in range_table], index=range_table)
num_table['factorial'] = factorials
print(num_table)



