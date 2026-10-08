import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

#Displays the contents of the Employees table. run python3.main.py
employees = pd.read_sql("""
SELECT *
FROM employees;
""", conn)

print(employees)

#Filtering using = similar to == in Python

filter_individual = pd.read_sql("""
SELECT *
FROM employees
WHERE lastName = "Patterson";
""", conn)

print(filter_individual)

#improved individual_filter

filter_individual2 = pd.read_sql("""
SELECT firstName, lastName, email
FROM employees
WHERE lastName = 'Patterson';
""", conn)

print(filter_individual2)

#select all employees with 5 letters in their first name

five_letters_in_name = pd.read_sql("""
SELECT *, length(firstName) AS name_length
FROM employees

WHERE name_length = 5;
""", conn)

print(five_letters_in_name)

#select all employees with the first initial of "L"

first_initial_as_L = pd.read_sql("""
SELECT *, substr(firstName, 1, 1) AS first_initial
FROM employees
WHERE first_initial = "L";
""",conn)

print(first_initial_as_L)

#select all order details where the price of each, rounded to the nearest integer, is 30 dollars:

price_rounded_to_30_dollars = pd.read_sql("""
SELECT *, CAST(round(priceEach) AS INTEGER) AS
rounded_price_int
FROM orderDetails
WHERE rounded_price_int = 30;
""", conn)

print(price_rounded_to_30_dollars)

#use the strftime function to select all orders placed in January of any year:

january_orders = pd.read_sql("""
SELECT *, strftime("%m", orderDate) AS month
FROM orders
WHERE month = "01";
""", conn)

print(january_orders)

#check to see if any orders were shipped late (shippedDate after requiredDate, i.e., the number of days late is a positive number):

late_shipped_by_days = pd.read_sql("""
SELECT *, julianday(shippedDate) - 
julianday(requiredDate) AS days_late
FROM orders
WHERE days_late > 0;
""", conn)

print(late_shipped_by_days)

conn.close()