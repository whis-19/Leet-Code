-- 1661. Average Time of Process per Machine
SELECT machine_id, ROUND(AVG(end_time - start_time), 3) AS processing_time
FROM (
    SELECT machine_id, process_id,
           MAX(CASE WHEN activity_type = 'end' THEN timestamp END) AS end_time,
           MIN(CASE WHEN activity_type = 'start' THEN timestamp END) AS start_time
    FROM Activity
    GROUP BY machine_id, process_id
) AS process_times
GROUP BY machine_id;

-- 1378. Replace Employee ID With The Unique Identifier
SELECT e.name, eu.unique_id
FROM Employees e
LEFT JOIN EmployeeUNI eu ON e.id = eu.id
ORDER BY e.id;

-- 1581. Customer Who Visited but Did Not Make Any Transactions
SELECT v.customer_id, COUNT(*) AS count_no_trans
FROM Visits v
LEFT JOIN Transactions t ON v.visit_id = t.visit_id
WHERE t.transaction_id IS NULL
GROUP BY v.customer_id;

-- 197. Rising Temperature
SELECT w.id
FROM Weather w
JOIN Weather w_prev ON w.recordDate = DATE_ADD(w_prev.recordDate, INTERVAL 1 DAY)
WHERE w.temperature > w_prev.temperature;

-- 1068. Product Sales Analysis I
SELECT product_name, year, price
FROM Sales s
JOIN Product p ON s.product_id = p.product_id;

-- 1683. Invalid Tweets
SELECT tweet_id  
FROM Tweets
WHERE LENGTH(content)>15;

-- 1148. Article Views I
SELECT distinct author_id AS id
FROM Views
WHERE author_id=viewer_id
ORDER BY id ASC;

-- 595. Big Countries
SELECT name, area, population FROM World
WHERE area>=3000000 OR population>=25000000;

-- 584. Find Customer Referee
SELECT name
FROM Customer 
WHERE referee_id!=2 OR referee_id is NULL ;

-- 1757. Recyclable and Low Fat Products
SELECT product_id FROM Products WHERE low_fats='Y' AND recyclable ='Y';
