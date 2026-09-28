# Multi-Dataset Data Cleaning & Quality Pipeline

A beginner-friendly to intermediate-level Python and Pandas project for learning how to build a **real-world, modular data cleaning and data-quality pipeline**.

This project works with multiple intentionally messy datasets and demonstrates how raw data can be:

```text
Read
  ↓
Profile
  ↓
Understand Problems
  ↓
Clean
  ↓
Transform
  ↓
Validate
  ↓
Generate Quality Report
  ↓
Export Cleaned Data
```

The project is designed not only to teach Pandas functions, but also to teach students how individual Python functions can be organized into a **real project architecture**.

---

# 1. Project Objective

Real-world datasets are rarely clean.

Data may contain:

* Extra spaces
* Missing values
* Duplicate records
* Inconsistent capitalization
* Inconsistent category names
* Invalid email addresses
* Invalid ages
* Negative numbers
* Currency symbols
* Commas inside numeric values
* Different date formats
* Invalid dates
* Unknown values
* Messy column names
* Duplicate business IDs

For example, a customer dataset may contain:

```text
 Customer ID
C001
 C002
C003
```

A gender column may contain:

```text
Male
male
MALE
M
m
Female
female
F
```

A salary column may contain:

```text
₹50,000
Rs. 60,000
INR 55000
$1,200
75,000
unknown
```

A professional data pipeline should not simply load this data and start analyzing it.

It should first:

```text
Understand the data
       ↓
Identify data-quality problems
       ↓
Apply appropriate cleaning rules
       ↓
Validate the result
       ↓
Generate a quality report
       ↓
Export the cleaned data
```

That is the main purpose of this project.

---

# 2. What Students Learn

This project covers Python, Pandas, data cleaning, validation, configuration, and basic data-pipeline architecture.

## Pandas concepts covered

Students work with:

```python
read_csv()
read_excel()

to_csv()
to_excel()

isna()
sum()
dtypes
unique()
value_counts()
duplicated()
describe()
nunique()

copy()
drop()
dropna()
fillna()

set_option()

set_index()
reset_index()

rename()
replace()
sort_values()

columns
map()
apply()
groupby()
```

Some functions are demonstrated directly in the reusable modules and manual tests, while some advanced analytical usage such as `groupby()` is planned for the next stage of the project.

---

# 3. Project Level

Current project level:

> **Intermediate Python + Pandas + Data Cleaning + Basic Data Engineering**

The project is intentionally built in stages.

## Current completed stage

```text
Python
  ↓
Pandas
  ↓
Data Reading
  ↓
Data Profiling
  ↓
Data Cleaning
  ↓
Data Transformation
  ↓
Validation
  ↓
Quality Reporting
  ↓
Exporting
  ↓
YAML Configuration
  ↓
Multi-Dataset Pipeline
```

## Future advanced stage

The following features are planned but are not yet considered complete:

```text
Rejected Records
      ↓
Advanced Validation
      ↓
Referential Integrity
      ↓
Automated Testing
      ↓
Logging
      ↓
CLI
      ↓
Production Hardening
      ↓
Portfolio Documentation
```

---

# 4. Project Architecture

The current project follows this structure:

```text
multi_dataset_data_cleaning_pipeline/
│
├── data/
│   │
│   ├── raw/
│   │   ├── customers.csv
│   │   ├── orders.csv
│   │   ├── products.xlsx
│   │   └── employees.csv
│   │
│   ├── processed/
│   │   ├── customers_cleaned.csv
│   │   ├── orders_cleaned.csv
│   │   ├── products_cleaned.xlsx
│   │   └── employees_cleaned.csv
│   │
│   └── rejected/
│
├── reports/
│
├── config/
│   └── cleaning_rules.yaml
│
├── src/
│   ├── __init__.py
│   │
│   ├── reader.py
│   ├── profiler.py
│   │
│   ├── string_cleaner.py
│   ├── numeric_cleaner.py
│   ├── datetime_cleaner.py
│   ├── cleaner.py
│   ├── transformer.py
│   ├── validator.py
│   ├── report_generator.py
│   ├── exporter.py
│   │
│   ├── config_loader.py
│   │
│   ├── customer_pipeline.py
│   ├── order_pipeline.py
│   ├── product_pipeline.py
│   └── employee_pipeline.py
│
├── tests/
│   ├── test_reader.py
│   ├── test_profiler.py
│   ├── test_string_cleaner.py
│   ├── test_numeric_cleaner.py
│   ├── test_datetime_cleaner.py
│   ├── test_cleaner.py
│   └── test_validator.py
│
├── main.py
├── requirements.txt
└── README.md
```

---

# 5. Understanding the Folder Structure

A student should think about the project like this:

```text
data/
    → actual datasets

config/
    → rules

src/
    → application logic

tests/
    → testing

main.py
    → starts the application

README.md
    → project documentation
```

---

# 6. `data/` Folder

The `data` folder contains the datasets used by the application.

```text
data/
├── raw/
├── processed/
└── rejected/
```

## Why separate these folders?

We don't want to mix:

```text
original data
```

with:

```text
cleaned data
```

because we should always preserve the original input.

---

# 7. `data/raw/`

This folder contains the original datasets.

```text
data/raw/
├── customers.csv
├── orders.csv
├── products.xlsx
└── employees.csv
```

These files intentionally contain data-quality problems.

### `customers.csv`

Contains customer information:

```text
Customer ID
Customer Name
Age
Gender
City
Email
```

Problems include:

* Extra spaces
* Missing names
* Missing emails
* Invalid ages
* Inconsistent gender values
* Inconsistent city capitalization
* Invalid emails
* Duplicate customer IDs
* Suspicious names

---

### `orders.csv`

Contains order information:

```text
Order ID
Customer ID
Product ID
Quantity
Unit Price
Order Date
```

Problems include:

* Missing customer IDs
* Missing product IDs
* Invalid quantities
* Zero quantity
* Negative quantity
* Unknown quantity
* Currency symbols
* Currency text
* Missing prices
* Multiple date formats
* Invalid dates
* Duplicate orders

---

### `products.xlsx`

Contains:

```text
Product ID
Product Name
Category
Price
```

Problems include:

* Missing product name
* Missing price
* Duplicate product ID
* Inconsistent category values
* Currency-formatted prices
* Negative price
* Unknown price
* Suspicious product names

---

### `employees.csv`

Contains:

```text
Employee ID
Employee Name
Department
Salary
Joining Date
```

Problems include:

* Missing employee name
* Inconsistent employee names
* Inconsistent departments
* Currency-formatted salaries
* Missing salary
* Negative salary
* Unknown salary
* Invalid joining dates
* Duplicate employee records

---

# 8. `data/processed/`

This folder contains the output generated by the pipeline.

Example:

```text
data/processed/
├── customers_cleaned.csv
├── orders_cleaned.csv
├── products_cleaned.xlsx
└── employees_cleaned.csv
```

The raw files are never intentionally overwritten.

The pipeline creates cleaned versions separately.

---

# 9. `data/rejected/`

This folder is reserved for records that fail validation.

Current status:

> Folder created, but rejected-record processing is part of the next advanced stage.

The future design will be:

```text
Valid records
      ↓
processed/

Invalid records
      ↓
rejected/
```

This is important in real data engineering because invalid records should often be preserved for investigation rather than simply deleted.

---

# 10. `reports/`

This folder is intended to store data-quality reports.

Example future output:

```text
reports/
├── customers_quality_report.json
├── orders_quality_report.json
├── products_quality_report.json
└── employees_quality_report.json
```

The current project already generates quality reports in Python and prints them to the console.

Saving reports as files is planned as a future improvement.

---

# 11. `config/`

The `config` folder contains configuration files.

Current file:

```text
config/cleaning_rules.yaml
```

The purpose of configuration is to separate:

```text
RULES
```

from:

```text
PYTHON CODE
```

For example:

```yaml
age:
  minimum: 18
  maximum: 100
```

Instead of hardcoding:

```python
if age < 18:
```

everywhere in Python, the rule can be stored in configuration.

This makes the application easier to modify.

---

# 12. `cleaning_rules.yaml`

This file contains dataset-specific rules.

The configuration currently contains sections for:

```yaml
customers:
orders:
products:
employees:
```

For example:

```yaml
customers:

  required_columns:
    - customer_id
    - customer_name
    - age
    - gender
    - city
    - email

  required_values:
    - customer_id
    - customer_name
```

This means customer data must contain these columns and required fields.

The configuration also contains rules for:

* gender standardization
* city standardization
* age range
* unique IDs
* email validation
* positive numeric values
* currency columns
* date columns
* category mapping
* department mapping

The configuration-driven system is currently being expanded and refined.

---

# 13. `src/` Folder

The `src` folder contains the application's Python code.

Instead of writing everything inside:

```text
main.py
```

we divide the application into modules.

This is called:

> **Modular programming**

Each module has a specific responsibility.

---

# 14. `src/reader.py`

### Responsibility

Read input datasets.

It supports:

```text
CSV
Excel
```

Main function:

```python
read_dataset()
```

Internally it uses:

```python
pd.read_csv()
pd.read_excel()
```

Example:

```python
df = read_dataset(
    "data/raw/customers.csv"
)
```

The function also checks whether the file exists and whether its extension is supported.

### Responsibility

```text
File
 ↓
reader.py
 ↓
DataFrame
```

It does **not** clean the data.

---

# 15. `src/profiler.py`

### Responsibility

Understand the dataset before cleaning.

Main function:

```python
profile_dataset()
```

It collects:

```text
Number of rows
Number of columns
Column names
Data types
Missing values
Duplicate rows
Descriptive statistics
Unique values
Value frequencies
```

Important Pandas operations include:

```python
df.isna()
df.dtypes
df.describe()
df.nunique()
df.value_counts()
df.duplicated()
```

The important concept for students is:

> **Never blindly clean data before understanding it.**

---

# 16. `src/string_cleaner.py`

### Responsibility

Clean text-based data.

It contains functions for:

```text
Whitespace
Names
Categories
Column names
```

Important functions:

```python
clean_whitespace()
standardize_categories()
clean_name()
clean_name_column()
standardize_column_names()
```

Important concepts:

```python
.str.strip()
.str.replace()
replace()
apply()
regex
```

Example:

```text
"  Rahul Sharma  "
```

becomes:

```text
"Rahul Sharma"
```

Another example:

```text
"MALE"
"male"
"M"
"m"
```

can be standardized to:

```text
"Male"
```

---

# 17. `src/numeric_cleaner.py`

### Responsibility

Clean numeric and currency-related data.

Important functions:

```python
extract_currency()
clean_numeric_string()
clean_currency_column()
convert_numeric_column()
find_negative_values()
```

For example:

```text
₹50,000
```

can be separated into:

```text
currency = INR
amount   = 50000
```

And:

```text
$1,200
```

becomes:

```text
currency = USD
amount   = 1200
```

This is important because:

```text
50000 INR
```

and:

```text
50000 USD
```

are not the same monetary value.

Therefore, the currency information should not simply be thrown away.

---

# 18. `src/datetime_cleaner.py`

### Responsibility

Handle date and time values.

Important functions:

```python
convert_to_datetime()
find_invalid_dates()
extract_date_only()
extract_year()
find_future_dates()
```

The project contains multiple date formats such as:

```text
2026-01-15
15/01/2026
Jan 20 2026
2026/01/22
22-01-2026
```

Invalid dates such as:

```text
2026-02-30
```

should become invalid/missing datetime values rather than causing the entire application to crash.

### Important real-world issue

Dates such as:

```text
03/05/2026
```

can be ambiguous.

It may mean:

```text
March 5
```

or:

```text
May 3
```

Therefore, production systems should define the expected date convention rather than silently guessing.

---

# 19. `src/cleaner.py`

### Responsibility

Provide general-purpose cleaning operations.

Functions include:

```python
copy_dataframe()
remove_duplicate_rows()
drop_empty_columns()
drop_empty_rows()
fill_missing_values()
fill_missing_with_mean()
drop_rows_with_missing()
set_display_options()
```

Important concepts:

```python
df.copy()
df.dropna()
df.fillna()
df.drop_duplicates()
pd.set_option()
```

One of the most important concepts is:

```python
cleaned_df = df.copy()
```

We don't want to accidentally modify the original raw DataFrame.

---

# 20. `src/transformer.py`

### Responsibility

Perform DataFrame transformations.

Functions include:

```python
rename_columns()
replace_values()
map_values()
apply_function()
sort_by_column()
set_dataframe_index()
reset_dataframe_index()
select_columns()
get_column_names()
```

Important Pandas concepts:

```python
rename()
replace()
map()
apply()
sort_values()
set_index()
reset_index()
columns
```

Example:

```python
df = df.rename(
    columns={
        "Customer Name": "customer_name"
    }
)
```

---

# 21. `src/validator.py`

### Responsibility

Determine whether cleaned data satisfies defined quality rules.

Validation functions include:

```python
validate_required_columns()
validate_required_values()
validate_range()
validate_positive()
validate_non_negative()
validate_unique()
validate_email_format()
validate_datetime()
create_validation_summary()
```

For example, an age rule can be:

```text
Minimum = 18
Maximum = 100
```

So:

```text
25 → valid
35 → valid
150 → invalid
-4 → invalid
```

Email validation checks basic formatting.

Unique validation checks business identifiers such as:

```text
customer_id
order_id
product_id
employee_id
```

---

# 22. `src/report_generator.py`

### Responsibility

Generate data-quality information before and after cleaning.

Important functions:

```python
count_missing_values()
count_total_missing_values()
count_duplicate_rows()
compare_row_counts()
compare_columns()
summarize_validation_results()
generate_data_quality_report()
print_data_quality_report()
```

The report can show:

```text
Original rows
Cleaned rows
Rows removed
Added columns
Removed columns
Original missing values
Cleaned missing values
Original duplicates
Cleaned duplicates
Validation results
```

Example:

```text
ROWS

Original rows : 15
Cleaned rows  : 14
Rows removed  : 1
```

This allows us to measure what happened during cleaning.

---

# 23. `src/exporter.py`

### Responsibility

Save cleaned datasets.

Functions:

```python
ensure_output_directory()
export_to_csv()
export_to_excel()
export_dataset()
```

It uses:

```python
df.to_csv()
df.to_excel()
```

The exporter automatically creates the output directory if required.

Example:

```python
export_dataset(
    cleaned_df,
    "data/processed/customers_cleaned.csv"
)
```

---

# 24. `src/config_loader.py`

### Responsibility

Load YAML configuration.

Main functions:

```python
load_config()
get_dataset_config()
```

Example:

```python
config = load_config(
    "config/cleaning_rules.yaml"
)
```

Then:

```python
customer_config = get_dataset_config(
    config,
    "customers"
)
```

This allows the application to retrieve only the rules required for a particular dataset.

---

# 25. Dataset-Specific Pipeline Modules

The project does not use exactly the same cleaning logic for every dataset.

Instead, we have separate processors:

```text
customer_pipeline.py
order_pipeline.py
product_pipeline.py
employee_pipeline.py
```

This follows the principle:

> **Common pipeline + dataset-specific rules**

---

# 26. `src/customer_pipeline.py`

### Responsibility

Clean and validate customer data.

Flow:

```text
Customer DataFrame
       ↓
Copy DataFrame
       ↓
Clean whitespace
       ↓
Clean customer names
       ↓
Standardize gender
       ↓
Convert age to numeric
       ↓
Remove duplicates
       ↓
Validate
       ↓
Return cleaned data + validation results
```

Main function:

```python
clean_customers()
```

---

# 27. `src/order_pipeline.py`

### Responsibility

Clean and validate orders.

Flow:

```text
Order DataFrame
       ↓
Copy
       ↓
Clean whitespace
       ↓
Convert quantity
       ↓
Clean currency
       ↓
Convert order date
       ↓
Remove duplicates
       ↓
Validate
       ↓
Return results
```

Main function:

```python
clean_orders()
```

---

# 28. `src/product_pipeline.py`

### Responsibility

Clean and validate products.

Flow:

```text
Product DataFrame
       ↓
Copy
       ↓
Clean whitespace
       ↓
Clean product names
       ↓
Clean currency
       ↓
Remove duplicates
       ↓
Validate
       ↓
Return results
```

Main function:

```python
clean_products()
```

---

# 29. `src/employee_pipeline.py`

### Responsibility

Clean and validate employees.

Flow:

```text
Employee DataFrame
       ↓
Copy
       ↓
Clean whitespace
       ↓
Clean employee names
       ↓
Clean salary
       ↓
Convert joining date
       ↓
Remove duplicates
       ↓
Validate
       ↓
Return results
```

Main function:

```python
clean_employees()
```

---

# 30. `src/pipeline.py`

This is the **central orchestrator**.

It does not contain every cleaning rule.

Instead, it decides which dataset processor should be used.

The important function is:

```python
get_dataset_processor()
```

It contains a mapping similar to:

```python
processors = {
    "customers": clean_customers,
    "orders": clean_orders,
    "products": clean_products,
    "employees": clean_employees,
}
```

Therefore:

```text
"customers"
     ↓
clean_customers()

"orders"
     ↓
clean_orders()

"products"
     ↓
clean_products()

"employees"
     ↓
clean_employees()
```

---

# 31. Central Pipeline Flow

The complete central pipeline is:

```text
run_pipeline()
      │
      ├── Load configuration
      │
      ├── Read dataset
      │
      ├── Standardize column names
      │
      ├── Select dataset processor
      │
      ├── Clean dataset
      │
      ├── Validate dataset
      │
      ├── Generate quality report
      │
      └── Export cleaned dataset
```

This is the core architecture of the project.

---

# 32. `main.py`

`main.py` is the application entry point.

It starts the pipelines.

Currently it runs:

```text
customers
orders
products
employees
```

Example:

```python
run_pipeline(
    dataset_name="customers",
    input_path="data/raw/customers.csv",
    output_path="data/processed/customers_cleaned.csv"
)
```

Then it runs the other datasets.

Students can therefore start the entire application using:

```bash
python main.py
```

---

# 33. `tests/`

The `tests` folder is reserved for automated tests.

The project has module-level test files such as:

```text
tests/
├── test_reader.py
├── test_profiler.py
├── test_string_cleaner.py
├── test_numeric_cleaner.py
├── test_datetime_cleaner.py
├── test_cleaner.py
└── test_validator.py
```

The project has also used manual test scripts during development to verify each module independently.

Automated `pytest` coverage is part of the next stage.

---

# 34. Complete Application Flow

The most important diagram for students is:

```text
                    RAW DATA
                       │
                       ▼
              ┌─────────────────┐
              │     READER      │
              │ reader.py       │
              └────────┬────────┘
                       │
                       ▼
                 RAW DATAFRAME
                       │
                       ▼
              ┌─────────────────┐
              │    PROFILER     │
              │ profiler.py     │
              └────────┬────────┘
                       │
                       ▼
             UNDERSTAND PROBLEMS
                       │
                       ▼
              ┌─────────────────┐
              │     CONFIG      │
              │ cleaning_rules  │
              │     .yaml       │
              └────────┬────────┘
                       │
                       ▼
              SELECT DATASET
                       │
          ┌────────────┼────────────┐
          │            │            │
          ▼            ▼            ▼
     Customers      Orders       Products
          │            │            │
          └────────────┼────────────┘
                       │
                       ▼
                 CLEANING
                       │
       ┌───────────────┼────────────────┐
       │               │                │
       ▼               ▼                ▼
    Strings         Numeric          Datetime
       │               │                │
       └───────────────┼────────────────┘
                       │
                       ▼
                 TRANSFORMATION
                       │
                       ▼
                  VALIDATION
                       │
             ┌─────────┴─────────┐
             │                   │
             ▼                   ▼
           VALID               INVALID
             │                   │
             ▼                   ▼
         PROCESSED           REJECTED
             │
             ▼
           REPORT
             │
             ▼
           EXPORT
```

---

# 35. Example: Customer Pipeline

Suppose the raw customer data contains:

```text
 Customer ID
 C001

Customer Name
 Rahul Sharma 

Gender
male

Age
25
```

The pipeline processes it:

```text
Raw value
    ↓
" Rahul Sharma "
    ↓
Whitespace cleaning
    ↓
"Rahul Sharma"
```

Gender:

```text
"male"
    ↓
mapping
    ↓
"Male"
```

Age:

```text
"25"
    ↓
pd.to_numeric()
    ↓
25
```

The final data becomes more consistent and easier to analyze.

---

# 36. Example: Currency Cleaning

Suppose the dataset contains:

```text
₹50,000
Rs. 60,000
INR 55000
$1,200
```

Instead of simply doing:

```python
remove_everything_except_digits()
```

we preserve the currency.

Conceptually:

```text
Raw Value       Currency       Amount
--------------------------------------
₹50,000         INR            50000
Rs. 60,000      INR            60000
INR 55000       INR            55000
$1,200          USD             1200
```

This is a professional data-cleaning decision.

---

# 37. Why We Don't Automatically Delete Invalid Records

Suppose:

```text
Age = 150
```

We don't immediately delete the customer.

Instead:

```text
150
 ↓
Validation
 ↓
INVALID
```

The system reports the problem.

Similarly:

```text
Email = arjun@@gmail.com
```

becomes:

```text
Validation
     ↓
INVALID EMAIL
```

This distinction is important:

> **Cleaning and validation are different operations.**

Cleaning attempts to standardize data.

Validation determines whether the resulting data satisfies business rules.

---

# 38. Cleaning vs Validation

Students should understand this difference clearly.

## Cleaning

Example:

```text
"  Rahul Sharma  "
```

becomes:

```text
"Rahul Sharma"
```

## Validation

Example:

```text
Age = 150
```

Cleaning may convert it to:

```text
150
```

but validation determines:

```text
150 > 100
```

Therefore:

```text
INVALID
```

---

# 39. Why We Use Multiple Python Files

A beginner may ask:

> Why not put everything into one Python file?

Because large applications become difficult to maintain.

Bad architecture:

```text
main.py
 ├── read data
 ├── clean names
 ├── clean salary
 ├── clean dates
 ├── validate
 ├── report
 ├── export
 ├── customer logic
 ├── order logic
 ├── product logic
 └── employee logic
```

Better:

```text
reader.py
    → reading

profiler.py
    → profiling

string_cleaner.py
    → strings

numeric_cleaner.py
    → numbers/currency

datetime_cleaner.py
    → dates

validator.py
    → validation

report_generator.py
    → reporting

exporter.py
    → output

pipeline.py
    → orchestration
```

This is called:

> **Separation of Concerns**

---

# 40. Common vs Dataset-Specific Logic

Not every dataset should use exactly the same cleaning rules.

For example:

```text
Customer
→ gender
→ age
→ email
```

Orders:

```text
→ quantity
→ unit price
→ order date
```

Products:

```text
→ category
→ price
```

Employees:

```text
→ department
→ salary
→ joining date
```

Therefore the project uses:

```text
COMMON COMPONENTS
        +
DATASET-SPECIFIC PROCESSORS
```

This makes the architecture reusable.

---

# 41. Current Dataset Results

The application has successfully processed all four datasets.

Example results:

```text
CUSTOMERS
15 rows → 14 rows

ORDERS
15 rows → 14 rows

PRODUCTS
12 rows → 11 rows

EMPLOYEES
15 rows → 14 rows
```

The removed rows are duplicate records.

The remaining validation failures are expected because the raw datasets intentionally contain invalid records.

For example:

```text
Customers
→ missing required values
→ invalid ages
→ invalid emails

Orders
→ missing required values
→ invalid quantities/prices
→ invalid dates

Products
→ missing required values
→ invalid prices

Employees
→ missing required values
→ invalid salaries
→ invalid dates
```

The important lesson is:

> A pipeline completing successfully does not mean every record is valid.

The pipeline itself can succeed while reporting data-quality failures.

---

# 42. How to Install the Project

Make sure Python is installed.

Create a virtual environment if desired:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

The project uses libraries such as:

```text
pandas
openpyxl
PyYAML
```

---

# 43. How to Run

From the project root:

```bash
python main.py
```

The application will process:

```text
customers
orders
products
employees
```

and create cleaned files inside:

```text
data/processed/
```

---

# 44. Recommended Student Learning Order

Students should not try to understand the entire project at once.

Learn it in this order:

```text
1. Python basics
        ↓
2. Pandas DataFrame basics
        ↓
3. Reading CSV/Excel
        ↓
4. Data profiling
        ↓
5. Missing values
        ↓
6. Duplicate handling
        ↓
7. String cleaning
        ↓
8. Numeric cleaning
        ↓
9. Currency cleaning
        ↓
10. Date/time cleaning
        ↓
11. Transformation
        ↓
12. Validation
        ↓
13. Reporting
        ↓
14. Exporting
        ↓
15. Configuration
        ↓
16. Modular architecture
        ↓
17. Multi-dataset pipeline
```

---

# 45. Important Developer Principles Learned

This project teaches several principles beyond Pandas.

## Principle 1 — Don't modify raw data

Use:

```python
cleaned_df = df.copy()
```

Keep the original input untouched.

---

## Principle 2 — Understand before cleaning

First:

```text
Profile
```

then:

```text
Clean
```

Do not blindly transform unknown data.

---

## Principle 3 — Use the right tool

Different problems require different techniques.

```text
Whitespace
    → strip / regex

Categories
    → replace / map

Numbers
    → to_numeric

Currency
    → currency extraction + numeric conversion

Dates
    → to_datetime

Missing values
    → isna / dropna / fillna

Duplicates
    → duplicated / drop_duplicates

Custom transformations
    → apply

Aggregations
    → groupby
```

---

## Principle 4 — Cleaning is not validation

Cleaning:

```text
Standardize data
```

Validation:

```text
Check whether data is acceptable
```

---

## Principle 5 — Don't blindly delete information

For example:

```text
$1,200
```

should not become only:

```text
1200
```

without considering currency.

Preserving information is important.

---

## Principle 6 — Dataset-specific rules matter

A customer dataset and employee dataset don't have identical business rules.

Therefore:

```text
Common pipeline
+
Dataset-specific logic
```

is more maintainable.

---

# 46. What Has Been Completed?

## Completed

* [x] Project structure
* [x] Realistic messy datasets
* [x] CSV reading
* [x] Excel reading
* [x] Data profiling
* [x] Missing-value analysis
* [x] Duplicate detection
* [x] Duplicate removal
* [x] String cleaning
* [x] Name cleaning
* [x] Column-name standardization
* [x] Category standardization utilities
* [x] Numeric conversion
* [x] Currency extraction
* [x] Date conversion
* [x] Date validation
* [x] Missing-value utilities
* [x] Data transformation
* [x] Data validation
* [x] Quality reporting
* [x] CSV export
* [x] Excel export
* [x] YAML configuration
* [x] Configuration loader
* [x] Dataset-specific processors
* [x] Central pipeline
* [x] Multi-dataset execution
* [x] `main.py`

---

# 47. What Is Still Planned?

The project is not yet at the final production-style stage.

Next stages include:

```text
1. Complete configuration-driven cleaning
        ↓
2. Improve mixed date handling
        ↓
3. Rejected-record system
        ↓
4. Advanced validation
        ↓
5. Referential integrity
        ↓
6. Data-quality metrics
        ↓
7. groupby-based analytics
        ↓
8. Automated pytest tests
        ↓
9. Logging
        ↓
10. Better error handling
        ↓
11. CLI interface
        ↓
12. Production hardening
        ↓
13. Final documentation
        ↓
14. GitHub portfolio preparation
```

---

# 48. Final Project Vision

The final version of this project is intended to become:

```text
                  DATA QUALITY SYSTEM
                         │
          ┌──────────────┴──────────────┐
          │                             │
       INPUTS                         RULES
          │                             │
 CSV / Excel                    YAML Configuration
          │                             │
          └──────────────┬──────────────┘
                         │
                         ▼
                    PROFILING
                         │
                         ▼
                     CLEANING
                         │
                         ▼
                   TRANSFORMATION
                         │
                         ▼
                    VALIDATION
                         │
              ┌──────────┴──────────┐
              │                     │
            VALID                 INVALID
              │                     │
              ▼                     ▼
          PROCESSED              REJECTED
              │
              ▼
            REPORT
              │
              ▼
            EXPORT
```

The goal is not merely to learn individual Pandas functions.

The goal is to understand how those functions can be combined into a **structured, reusable, maintainable data-processing application**.

---

# 49. Key Takeaway for Students

Do not memorize the project.

Understand the flow:

```text
What data do I have?
        ↓
What problems exist?
        ↓
How should I clean them?
        ↓
What rules should the data satisfy?
        ↓
Did the cleaned data pass those rules?
        ↓
What happened during cleaning?
        ↓
Where should the final data go?
```

Once students understand this thinking, Pandas becomes a tool for solving data problems rather than simply a collection of functions.

---

# 50. Project Status

**Current status: Intermediate stage completed**

```text
Data Input             ████████████████████ 100%
Data Profiling         ████████████████████ 100%
Data Cleaning          ████████████████████ 100%
Transformation         ████████████████████ 100%
Validation             ████████████████████ 100%
Reporting              ████████████████████ 100%
Export                 ████████████████████ 100%
Configuration          ███████████████░░░░░  75%
Multi-Dataset Pipeline ████████████████████ 100%

Rejected Records       ░░░░░░░░░░░░░░░░░░░░   0%
Advanced Validation    ░░░░░░░░░░░░░░░░░░░░   0%
Automated Testing      ░░░░░░░░░░░░░░░░░░░░   0%
Logging                ░░░░░░░░░░░░░░░░░░░░   0%
CLI                    ░░░░░░░░░░░░░░░░░░░░   0%
Production Hardening   ░░░░░░░░░░░░░░░░░░░░   0%
```

---

# 51. One-Sentence Project Description

> A modular Python and Pandas-based multi-dataset data-quality pipeline that reads messy CSV/Excel data, profiles data-quality issues, applies dataset-specific cleaning and transformations, validates business rules, generates quality reports, and exports cleaned datasets.
