-- Allocating random data to our DB 
USE [e-commerce]

INSERT INTO Customers
VALUES
(1,'Carlos','Leon','somewhere@gmaill.com',2020202020)

INSERT INTO Customers
VALUES
(2,'Luisa','Ruiz','here@hotmai.com',533202020)

INSERT INTO Customers
VALUES
(3,'Roberto','Contreras','guate@gmail.com',315202063)

INSERT INTO Orders
VALUES
(1,1,'2023-03-29'),
(2,3,'2023-04-05'),
(3,2,'2023-04-20'),
(4,2,'2023-06-28'),
(5,3,'2023-07-15'),
(6,1,'2023-08-07'),
(7,2,'2023-08-20'),
(8,3,'2023-08-25'),
(9,2,'2023-09-10'),
(10,1,'2023-09-11')

INSERT INTO Products
VALUES
(1,'Jelly',50,10),
(2,'Pizza',100,20),
(3,'Cereal',20,5),
(4,'Milk',10,50),
(5,'Ice Cream',5,100),
(6,'Chocolate',5,60),
(7,'Popcorn',7,15)

INSERT INTO OrderItems
VALUES
(100,1,5,10,50),
(101,2,1,2,100),
(102,3,7,2,30),
(103,4,2,1,100),
(104,5,4,1,10),
(105,6,6,2,10)

SELECT * FROM Customers
SELECT * FROM Orders
SELECT * FROM Products
SELECT * FROM OrderItems


-- CRUD OPERATIONS

--1. Insert product
INSERT INTO Products
VALUES
(8,'Laptop', 1000, 50)

SELECT * FROM Products

--2. Update product id
UPDATE Products SET Product_id = 75
WHERE Product_id = 3

SELECT * FROM Products

--3. Delete an order

INSERT INTO OrderItems
VALUES
(106,10,5,10,50)

SELECT * FROM OrderItems 

DELETE FROM OrderItems
WHERE Order_id = 10

DELETE FROM Orders
WHERE Order_id = 10

SELECT * FROM OrderItems
SELECT * FROM Orders

-- 4. Get Customers' names
SELECT First_name, Last_name FROM Customers
WHERE Customer_id IN (SELECT Customer_id FROM Orders
WHERE Order_id = 5)

--5. Getting total revenue
SELECT SUM (Subtotal) as 'SubTotal'
FROM OrderItems