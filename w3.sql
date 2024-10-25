-- w3

-- Del 2: Grundlæggende dataudtræk

-- 2

SELECT *
FROM products
ORDER BY
UnitPrice;

-- 3

SELECT *
 FROM customers
 WHERE
 Country
 LIKE
 Spain;

-- 4

SELECT *
FROM products
WHERE
UnitsInStock > 100 AND UnitPrice >= 25;

-- 5

SELECT DISTINCT ShipCountry
FROM orders;

-- 6

SELECT orderdate
FROM orders
WHERE orderdate
LIKE '1996-10%'; 

-- 7

SELECT *
FROM orders
WHERE 
    ShipRegion IS NULL
    AND ShipCountry = 'Germany'
    AND EmployeeID = '1'
    AND Freight >= 100
    AND OrderDate BETWEEN '1996-01-01' AND '1996-12-31';
    
    
    SELECT *
FROM orders;

-- 8
SELECT *
FROM orders
WHERE ShipDate > RequiredDate;

-- 9
SELECT * FROM orders
WHERE 
ShipCountry like "Canada"
AND (OrderDate LIKE '1997-01-%'
OR OrderDate LIKE '1997-02-%'
OR OrderDate LIKE '1997-03-%'
OR OrderDate LIKE '1997-04-%');

-- 10
SELECT * FROM orders
WHERE
EmployeeID IN (2,5,8)
AND ShipRegion != ''
AND ShipVia IN (1,3)
ORDER BY EmployeeID ASC, ShipVia ASC;

-- 11
SELECT * FROM employees
WHERE
birthdate BETWEEN 0 AND 1960;


