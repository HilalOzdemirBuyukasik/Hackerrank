-- Hackerrank SQL Practices

-- Query all columns for a city in CITY with the ID 1661.

select 
ID,
NAME,
COUNTRYCODE,
DISTRICT,
POPULATION
from CITY
where ID = 1661


-- Query the names of all the Japanese cities in the CITY table. The COUNTRYCODE for Japan is JPN.

select 
NAME
from CITY
where COUNTRYCODE = 'JPN'


-- Query a list of CITY names from STATION for cities that have an even ID number. Print the results in any order, but exclude duplicates from the answer.

select 
distinct CITY
from STATION
where ID % 2 = 0;

-- Query the list of CITY names ending with vowels (a, e, i, o, u) from STATION. Your result cannot contain duplicates.

select 
distinct CITY
from Station
where City like '%a'
    or City like '%e'
    or City like '%i'
    or City like '%o'
    or City like '%u';



-- Query the list of CITY names from STATION that do not start with vowels. Your result cannot contain duplicates.

select 
Distinct City
From Station
Where left(City, 1) not in ('a', 'e', 'i', 'o', 'u');


-- Query the list of CITY names from STATION that do not start with vowels and do not end with vowels. Your result cannot contain duplicates.

SELECT DISTINCT CITY
FROM STATION
WHERE LOWER(LEFT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u')
   and LOWER(RIGHT(CITY, 1)) NOT IN ('a', 'e', 'i', 'o', 'u');


-- Write a query that prints a list of employee names (i.e.: the name attribute) for employees in Employee having a salary greater than  per month who have been employees for less than  months. Sort your result by ascending employee_id.


select
name
from Employee
where salary > 2000 AND months < 10
order by employee_id ASC;

