-- 1158. Market Analysis I
SELECT u.user_id as buyer_id, u.join_date, count(o.order_id) as 'orders_in_2019'
FROM users u
LEFT JOIN Orders o
ON o.buyer_id=u.user_id AND YEAR(order_date)='2019'
GROUP BY u.user_id

-- 1164. Product Price at a Given Date
select product_id ,10 as price 
from products
group by product_id 
having min(change_date) > '2019-08-16'
union all
select product_id , new_price as price 
from products
where( product_id , change_date) in (
    select product_id , max(change_date) as price from products where change_date <=  '2019-08-16' group by product_id
    )

-- 1174. Immediate Food Delivery II
select ROUND(SUM(IF(ct.o_date = ct.d_date,1,0))*100/(select COUNT(DISTINCT(customer_id)) from Delivery)
,2) as immediate_percentage
from
(

select customer_id, MIN(order_date) as o_date , MIN(customer_pref_delivery_date) as d_date from Delivery 
group by customer_id
order by customer_id

) as ct

-- 1321. Restaurant Growth
# Write your MySQL query statement below
SELECT
    visited_on,
    (
        SELECT SUM(amount)
        FROM customer
        WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
    ) AS amount,
    ROUND(
        (
            SELECT SUM(amount) / 7
            FROM customer
            WHERE visited_on BETWEEN DATE_SUB(c.visited_on, INTERVAL 6 DAY) AND c.visited_on
        ),
        2
    ) AS average_amount
FROM customer c
WHERE visited_on >= (
        SELECT DATE_ADD(MIN(visited_on), INTERVAL 6 DAY)
        FROM customer
    )
GROUP BY visited_on;

-- 1050. Actors and Directors Who Cooperated At Least Three Times
SELECT actor_id, director_id 
FROM ActorDirector 
GROUP BY actor_id, director_id 
HAVING COUNT(actor_id) > 2;

-- 1045. Customers Who Bought All Products
SELECT  customer_id 
FROM Customer 
GROUP BY customer_id
HAVING COUNT(distinct product_key) = (SELECT COUNT(product_key) FROM Product)

-- 627. Swap Salary
UPDATE salary SET sex =
CASE sex
    WHEN 'm' THEN 'f'
    ELSE 'm'
END;

-- 626. Exchange Seats
SELECT id,
    CASE
        WHEN id % 2 = 0 THEN LAG(student) OVER(ORDER BY id)
        ELSE COALESCE(LEAD(student) OVER(ORDER BY id), student)
    END AS student
FROM Seat

-- 620. Not Boring Movies
SELECT *
FROM Cinema
WHERE
  MOD(id, 2) = 1
  AND description != 'boring'
ORDER BY rating DESC;

-- 619. Biggest Single Number
SELECT MAX(num) AS num
FROM (
    SELECT num
    FROM MyNumbers
    GROUP BY num
    HAVING COUNT(num) = 1
) AS unique_numbers;

-- 610. Triangle Judgement
SELECT x,y,z,
case WHEN (x+y) > z AND (x+z) > y AND (y+z) > x THEN 'Yes' ELSE 'No' end AS triangle
FROM Triangle 

-- 608. Tree Node
SELECT id, CASE
    WHEN p_id IS NULL THEN 'Root'
    WHEN id NOT IN (SELECT DISTINCT(p_id) FROM tree WHERE p_id IS NOT NULL) THEN 'Leaf'
    ELSE 'Inner'
END AS 'Type'
FROM Tree
ORDER BY id

-- 607. Sales Person
SELECT DISTINCT sp.name
FROM SalesPerson sp
WHERE sp.sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    LEFT JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);

-- 602. Friend Requests II: Who Has the Most Friends
(SELECT r.requester_id as id,IFNULL(count(requester_id),0) + IFNULL(acc.cnt,0) as num
from (Select count(accepter_id)  as cnt, accepter_id as id
from RequestAccepted r
GROUP BY r.accepter_id
) as acc RIGHT OUTER JOIN RequestAccepted r 
ON acc.id=r.requester_id 
GROUP BY r.requester_id
)
UNION (
Select accepter_id as id,count(accepter_id) as num
from RequestAccepted r
where accepter_id NOT IN (
    SELECT distinct requester_id from RequestAccepted
)
GROUP BY r.accepter_id
)
ORDER BY num desc
limit 1

-- 601. Human Traffic of Stadium
SELECT s.id, s.visit_date, s.people FROM Stadium s, Stadium t, Stadium u
WHERE ((s.id+1 = t.id AND s.id+2 = u.id) 
    OR (s.id-1 = t.id AND s.id+1 = u.id) 
    OR (s.id-1 = t.id AND s.id-2 = u.id))
    AND s.people>=100 AND t.people>=100 AND u.people>=100
GROUP BY s.id
ORDER BY id
    
-- 1179. Reformat Department Table
SELECT Department.id,
sum(if(month='Jan',revenue,null)) as Jan_Revenue,
sum(if(month='Feb',revenue,null)) as Feb_Revenue,
sum(if(month='Mar',revenue,null)) as Mar_Revenue,
sum(if(month='Apr',revenue,null)) as Apr_Revenue,
sum(if(month='May',revenue,null)) as May_Revenue,
sum(if(month='Jun',revenue,null)) as Jun_Revenue,
sum(if(month='Jul',revenue,null)) as Jul_Revenue,
sum(if(month='Aug',revenue,null)) as Aug_Revenue,
sum(if(month='Sep',revenue,null)) as Sep_Revenue,
sum(if(month='Oct',revenue,null)) as Oct_Revenue,
sum(if(month='Nov',revenue,null)) as Nov_Revenue,
sum(if(month='Dec',revenue,null)) as Dec_Revenue
from Department 
GROUP BY id;

-- 1193. Monthly Transactions I
SELECT  SUBSTR(trans_date,1,7) as month, country, count(id) as trans_count, SUM(CASE WHEN state = 'approved' then 1 else 0 END) as approved_count, SUM(amount) as trans_total_amount, SUM(CASE WHEN state = 'approved' then amount else 0 END) as approved_total_amount
FROM Transactions
GROUP BY month, country

-- 1204. Last Person to Fit in the Bus
SELECT 
    q1.person_name
FROM Queue q1 JOIN Queue q2 ON q1.turn >= q2.turn
GROUP BY q1.turn
HAVING SUM(q2.weight) <= 1000
ORDER BY SUM(q2.weight) DESC
LIMIT 1

-- 1211. Queries Quality and Percentage
WITH percentage as(
select query_name, ROUND(AVG(rating<3)*100,2) as percent
from Queries 
GROUP BY query_name 
)

Select Queries.query_name,ROUND(SUM(Queries.rating/Queries.position)/count(Queries.query_name),2) as quality,percentage.percent as poor_query_percentage
from Queries JOIN percentage
ON Queries.query_name=percentage.query_name
Group BY query_name 

-- 1251. Average Selling Price
SELECT p.product_id, IFNULL(ROUND(SUM(units*price)/SUM(units),2),0) AS average_price
FROM Prices p LEFT JOIN UnitsSold u
ON p.product_id = u.product_id AND
u.purchase_date BETWEEN start_date AND end_date
group by product_id

-- 1280. Students and Examinations
SELECT s.student_id, s.student_name, sub.subject_name, COALESCE(e.attended_exams, 0) AS attended_exams
FROM Students s
CROSS JOIN Subjects sub
LEFT JOIN (
    SELECT student_id, subject_name, COUNT(*) AS attended_exams
    FROM Examinations
    GROUP BY student_id, subject_name
) e ON s.student_id = e.student_id AND sub.subject_name = e.subject_name
ORDER BY s.student_id, sub.subject_name;

-- 1327. List the Products Ordered in a Period
SELECT p.product_name, 
       SUM(o.unit) AS unit 
FROM Products p 
JOIN Orders o 
ON p.product_id = o.product_id 
WHERE o.order_date >= '2020-02-01' 
  AND o.order_date <= '2020-02-29'
GROUP BY o.product_id 
HAVING unit >= 100;

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

-- 180. Consecutive Numbers
SELECT DISTINCT L1.num  AS ConsecutiveNums 
FROM Logs L1, Logs L2,Logs L3 
WHERE L1.id=L2.id - 1 AND L1.num=L2.num and  L2.id=L3.id-1 and L2.num=L3.num;

-- 181. Employees Earning More Than Their Managers
SELECT a.name Employee
FROM employee AS a
JOIN employee AS b ON a.managerId = b.id
WHERE a.salary > b.salary;

-- 182. Duplicate Emails
SELECT DISTINCT(p1.email) from Person p1, Person p2
where p1.id <> p2.id AND p1.email = p2.email;

-- 183. Customers Who Never Order
SELECT name AS Customers
FROM customers
LEFT JOIN orders ON customers.id = orders.customerId
WHERE orders.customerId IS NULL;

-- 184. Department Highest Salary
SELECT d.name AS Department, e.name AS Employee, e.salary AS Salary
FROM Employee e
JOIN Department d ON e.departmentId = d.id
WHERE (e.departmentId, e.salary) IN (
    SELECT departmentId, MAX(salary)
    FROM Employee
    GROUP BY departmentId
);

-- 185. Department Top Three Salaries
SELECT
    d.name AS Department,
    e.name AS Employee,
    e.salary AS Salary
FROM
    Employee e
    JOIN Department d ON e.departmentId = d.id
WHERE
    (
        SELECT COUNT(DISTINCT salary)
        FROM Employee e2
        WHERE e2.departmentId = e.departmentId AND e2.salary >= e.salary
    ) <= 3
ORDER BY
    Department, Salary DESC;

-- 196. Delete Duplicate Emails
DELETE p1 FROM person p1, person p2 
WHERE p1.email=p2.email AND p1.id>p2.id;

-- 511. Game Play Analysis I
SELECT PLAYER_ID,MIN(EVENT_DATE) AS FIRST_LOGIN FROM ACTIVITY GROUP BY PLAYER_ID;

-- 570. Managers with at Least 5 Direct Reports
SELECT a.name 
FROM Employee a 
JOIN Employee b ON a.id = b.managerId 
GROUP BY b.managerId 
HAVING COUNT(*) >= 5

-- 577. Employee Bonus
SELECT Employee.name,Bonus.bonus FROM Employee 
LEFT JOIN Bonus ON Employee.empID = Bonus.empID
WHERE bonus < 1000 OR Bonus IS NULL;

-- 585. Investments in 2016
SELECT ROUND(SUM(tiv_2016), 2) AS tiv_2016
FROM Insurance
WHERE tiv_2015 IN (
    SELECT tiv_2015
    FROM Insurance
    GROUP BY tiv_2015
    HAVING COUNT(*) > 1
)
AND (lat, lon) IN (
    SELECT lat, lon
    FROM Insurance
    GROUP BY lat, lon
    HAVING COUNT(*) = 1
)

-- 586. Customer Placing the Largest Number of Orders
SELECT
    customer_number
FROM Orders
    GROUP BY customer_number
    ORDER BY COUNT(*) DESC
LIMIT 1

-- 596. Classes More Than 5 Students
SELECT class
FROM Courses
GROUP BY class
HAVING COUNT(student) >= 5;

-- 1341. Movie Rating
(SELECT name AS results
FROM MovieRating JOIN Users USING(user_id)
GROUP BY name
ORDER BY COUNT(*) DESC, name
LIMIT 1)

UNION ALL

(SELECT title AS results
FROM MovieRating JOIN Movies USING(movie_id)
WHERE EXTRACT(YEAR_MONTH FROM created_at) = 202002
GROUP BY title
ORDER BY AVG(rating) DESC, title
LIMIT 1);

