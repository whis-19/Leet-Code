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

-- 175. Combine Two Tables
SELECT 
    p.FirstName, p.LastName, a.City, a.State
FROM 
    Person p
LEFT JOIN 
    Address a
ON 
    p.PersonId = a.PersonId;

-- 176. Second Highest Salary
SELECT 
    MAX(Salary) AS SecondHighestSalary
FROM 
    Employee
WHERE 
    Salary < (SELECT MAX(Salary) FROM Employee);

-- 177. Nth Highest Salary
CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
SET N = N-1;
  RETURN (
      SELECT DISTINCT(salary) from Employee order by salary DESC
      LIMIT 1 OFFSET N
      
  );
END

-- 178. Rank Scores
SELECT
    Score, DENSE_RANK() OVER (ORDER BY Score DESC) AS "Rank"
FROM
    Scores
ORDER BY
    Score DESC;

-- 262. Trips and Users
SELECT
    request_at AS day,
    ROUND(SUM((status <> 'completed')) / COUNT(*), 2) AS "Cancellation Rate"
FROM Trips
WHERE
    request_at BETWEEN '2013-10-01' AND '2013-10-03'
    AND
    (client_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes'))
    AND
    (driver_id NOT IN (SELECT users_id FROM Users WHERE banned = 'Yes'))
GROUP BY 1

-- 550. Game Play Analysis IV
SELECT
  ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) AS fraction
FROM
  Activity
WHERE
  (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
  IN (
    SELECT player_id, MIN(event_date) AS first_login FROM Activity GROUP BY player_id
  )
