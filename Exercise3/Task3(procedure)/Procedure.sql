CREATE PROCEDURE RevenueByCostumer @CostumerName VARCHAR(30), @CostumerSurname VARCHAR(30)
AS 
SELECT SUM(subtotal) AS 'Total Revenue' FROM OrderItems
WHERE Order_id IN (SELECT Order_id FROM Orders
WHERE Customer_id IN (SELECT Customer_id FROM Customers
WHERE (First_name = @CostumerName AND Last_name = @CostumerSurname)
))
GO


EXEC RevenueByCostumer @CostumerName = 'Carlos', @CostumerSurname = 'Leon';