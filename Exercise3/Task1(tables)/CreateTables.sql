-- create DB
CREATE DATABASE e-commerce

USE [e-commerce]

-- Table Creation

-- 1. Customers
CREATE TABLE Customers(
Customer_id INT PRIMARY KEY,
First_name VARCHAR(30),
Last_name VARCHAR(30),
Email VARCHAR(255),
Phone INT	
)

-- 2.Products
CREATE TABLE Products(
Product_id INT PRIMARY KEY,
Product_name VARCHAR(30),
Price INT,
Stock_quantity INT
)

-- 3. Orders
CREATE TABLE Orders(
Order_id INT PRIMARY KEY,
Customer_id INT,
CONSTRAINT Customer_id_FK1 FOREIGN KEY (Customer_id)
REFERENCES Customers (Customer_id),
Order_date DATE
)

--4. OrderItems
CREATE TABLE OrderItems(
Order_item_id INT PRIMARY KEY,
Order_id INT, 
CONSTRAINT Order_id_FK1 FOREIGN KEY (Order_id)
REFERENCES Orders(Order_id),
Product_id INT,
CONSTRAINT Product_id_FK1 FOREIGN KEY (Product_id)
REFERENCES PRODUCTS (Product_id),
Quantity INT, 
Subtotal INT
)
