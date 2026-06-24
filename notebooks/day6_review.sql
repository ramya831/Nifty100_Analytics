-- 5 random companies

SELECT *
FROM companies
ORDER BY RANDOM()
LIMIT 5;


-- Year coverage

SELECT company_id, COUNT(year)
FROM profitandloss
GROUP BY company_id;


-- Companies with less than 5 years

SELECT company_id, COUNT(year)
FROM profitandloss
GROUP BY company_id
HAVING COUNT(year) < 5;


-- Missing company names

SELECT *
FROM companies
WHERE company_name IS NULL;