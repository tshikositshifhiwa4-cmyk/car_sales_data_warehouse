from dotenv import load_dotenv
import os
import snowflake.connector

load_dotenv()

conn = snowflake.connector.connect(
    user=os.getenv("SNOWFLAKE_USER"),
    password=os.getenv("SNOWFLAKE_PASSWORD"),
    account=os.getenv("SNOWFLAKE_ACCOUNT"),
    warehouse=os.getenv("SNOWFLAKE_WAREHOUSE"),
    database=os.getenv("SNOWFLAKE_DATABASE"),
    schema=os.getenv("SNOWFLAKE_SCHEMA")
)

print("Connected")

cursor = conn.cursor()
#-cresting dim_customer table
cursor.execute("""
CREATE OR REPLACE TABLE dim_customer (
    customer_id INT AUTOINCREMENT PRIMARY KEY,
    customer_name STRING,
    gender STRING,
    annual_income FLOAT,
    phone STRING
);
""")

#-creating dim_car
cursor.execute("""
CREATE OR REPLACE TABLE dim_car (
    car_id STRING PRIMARY KEY,
    company STRING,
    model STRING,
    engine STRING,
    transmission STRING,
    color STRING,
    body_style STRING
);
""")

#-creating dim_dealer
cursor.execute("""
CREATE OR REPLACE TABLE dim_dealer (
    dealer_id INT AUTOINCREMENT PRIMARY KEY,
    dealer_name STRING,
    dealer_no STRING,
    dealer_region STRING
);
""")

#-creating dim_date
cursor.execute("""
CREATE OR REPLACE TABLE dim_date (
    date_id INT AUTOINCREMENT PRIMARY KEY,
    full_date DATE,
    year INT,
    month INT,
    day INT
);
""")

#-creating the fact table
cursor.execute("""
CREATE OR REPLACE TABLE fact_sales (
    sales_id INT AUTOINCREMENT PRIMARY KEY,
    car_id STRING,
    customer_id INT,
    dealer_id INT,
    date_id INT,
    price FLOAT
);
""")