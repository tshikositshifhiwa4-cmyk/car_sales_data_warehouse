<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=FFB6C1,FFC0CB&height=220&section=header&text=Car%20Sales%20Data%20Engineering%20Project&fontSize=32&fontColor=000000&animation=twinkling" />
</p>

<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?color=F8C8DC&size=28&center=true&vCenter=true&width=600&lines=Python" />
</p>

#  Car Sales Analysis

## 🎀 Overview

This project showcases a **data engineering workflow using Python**, where a raw car sales dataset is transformed into a structured **star schema** for analytics.

Starting from a single flat file, the data is cleaned, modeled, and split into **fact and dimension tables** to improve organization, scalability, and query performance.

The project combines **data modeling, Python-based transformation, and analytical thinking** to simulate how real-world data pipelines are designed and prepared for reporting tools.

It serves as a foundation for building **ETL pipelines, data warehouses, and business intelligence solutions**.

---

##  Tech Stack

<p>
  <img src="https://img.shields.io/badge/Python%20(pandas)-F8C8DC?style=for-the-badge&logo=python&logoColor=black"/>
  <img src="https://img.shields.io/badge/SQL-000000?style=for-the-badge&logo=sql&logoColor=white"/>
  <img src="https://img.shields.io/badge/Snowflake-F8C8DC?style=for-the-badge&logo=snowflake&logoColor=black"/>
  <img src="https://img.shields.io/badge/GitHub-000000?style=for-the-badge&logo=github&logoColor=white"/>
</p>

---

## 📁 Dataset Overview

| Column Name   | Description                    |
| ------------- | ------------------------------ |
| Car_id        | Unique identifier for each car |
| Date          | Transaction date               |
| Customer Name | Name of the customer           |
| Gender        | Customer gender                |
| Annual Income | Customer income level          |
| Dealer_Name   | Name of the dealer             |
| Company       | Car brand                      |
| Model         | Car model                      |
| Engine        | Engine type                    |
| Transmission  | Transmission type              |
| Color         | Car color                      |
| Price ($)     | Sale price                     |
| Dealer_No     | Dealer identifier              |
| Body Style    | Car body type                  |
| Phone         | Customer contact               |
| Dealer_Region | Dealer location                |

---

## ⭐ Star Schema Design

###  Fact Table

| Column           | Description                 |
| ---------------- | --------------------------- |
| sales_id (PK)    | Unique sale identifier      |
| car_id (FK)      | Links to car dimension      |
| customer_id (FK) | Links to customer dimension |
| dealer_id (FK)   | Links to dealer dimension   |
| date_id (FK)     | Links to date dimension     |
| price            | Sale amount                 |

---

###  Dimension: dim_car

| Column       | Description           |
| ------------ | --------------------- |
| car_id (PK)  | Unique car identifier |
| company      | Brand name            |
| model        | Model name            |
| engine       | Engine type           |
| transmission | Transmission type     |
| color        | Car color             |
| body_style   | Body type             |

---

###  Dimension: dim_customer

| Column           | Description                |
| ---------------- | -------------------------- |
| customer_id (PK) | Unique customer identifier |
| customer_name    | Customer name              |
| gender           | Gender                     |
| annual_income    | Income level               |
| phone            | Contact number             |

---

###  Dimension: dim_dealer

| Column         | Description              |
| -------------- | ------------------------ |
| dealer_id (PK) | Unique dealer identifier |
| dealer_name    | Dealer name              |
| dealer_no      | Dealer number            |
| dealer_region  | Region                   |

---

###  Dimension: dim_date

| Column       | Description            |
| ------------ | ---------------------- |
| date_id (PK) | Unique date identifier |
| full_date    | Full date              |
| year         | Year                   |
| month        | Month                  |
| day          | Day                    |

---

##  Relationships

* dim_car → fact_sales (1:M)
* dim_customer → fact_sales (1:M)
* dim_dealer → fact_sales (1:M)
* dim_date → fact_sales (1:M)

---

##  Objectives

* Transform a raw, flat car sales dataset into a structured **analytical data model**
* Design and implement a **star schema**, including fact and dimension tables
* Perform data cleaning and transformation using **Python (pandas)**
* Prepare data for loading into a **cloud data warehouse (Snowflake)**
* Enable data visualization and insights using **Tableau**

---

##  Future Improvements

* Build ETL pipeline using Python
* Load data into Snowflake
* Create dashboards (Power BI / Looker Studio)
* Add data validation and testing

---

## 👩🏽‍💻 Author

**Data Analyst | Junior Data Engineer**

