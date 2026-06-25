-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;


-- 2. Show companies
SELECT company_name
FROM companies
LIMIT 10;


-- 3. Profit and Loss count
SELECT COUNT(*)
FROM profitandloss;


-- 4. Balance sheet count
SELECT COUNT(*)
FROM balancesheet;


-- 5. Cashflow count
SELECT COUNT(*)
FROM cashflow;


-- 6. Year coverage
SELECT year, COUNT(*)
FROM profitandloss
GROUP BY year;


-- 7. Companies with maximum records
SELECT company_id, COUNT(*)
FROM profitandloss
GROUP BY company_id
ORDER BY COUNT(*) DESC
LIMIT 5;


-- 8. Stock price records
SELECT COUNT(*)
FROM stock_prices;


-- 9. Sector list
SELECT *
FROM sectors
LIMIT 10;


-- 10. Financial ratios
SELECT *
FROM financial_ratios
LIMIT 10;