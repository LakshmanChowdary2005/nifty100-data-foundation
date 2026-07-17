-- 1. Total companies
SELECT COUNT(*) AS total_companies
FROM companies;

-- 2. List all companies
SELECT company_name, ticker
FROM companies
ORDER BY company_name;

-- 3. Companies by sector
SELECT sector, COUNT(*) AS total
FROM companies
GROUP BY sector
ORDER BY total DESC;

-- 4. Top 10 companies by net profit
SELECT c.company_name, p.net_profit
FROM profitandloss p
JOIN companies c
ON p.company_id = c.company_id
ORDER BY p.net_profit DESC
LIMIT 10;

-- 5. Top 10 companies by assets
SELECT c.company_name, b.assets
FROM balancesheet b
JOIN companies c
ON b.company_id = c.company_id
ORDER BY b.assets DESC
LIMIT 10;

-- 6. Average net profit
SELECT AVG(net_profit) AS average_profit
FROM profitandloss;

-- 7. Average assets
SELECT AVG(assets) AS average_assets
FROM balancesheet;

-- 8. Highest ROE
SELECT company_id, roe
FROM financial_ratios
ORDER BY roe DESC
LIMIT 10;

-- 9. Highest stock closing prices
SELECT company_id, close
FROM stock_prices
ORDER BY close DESC
LIMIT 10;

-- 10. Number of records in each table
SELECT 'companies', COUNT(*) FROM companies
UNION ALL
SELECT 'profitandloss', COUNT(*) FROM profitandloss
UNION ALL
SELECT 'balancesheet', COUNT(*) FROM balancesheet
UNION ALL
SELECT 'cashflow', COUNT(*) FROM cashflow
UNION ALL
SELECT 'analysis', COUNT(*) FROM analysis
UNION ALL
SELECT 'documents', COUNT(*) FROM documents
UNION ALL
SELECT 'prosandcons', COUNT(*) FROM prosandcons
UNION ALL
SELECT 'sectors', COUNT(*) FROM sectors
UNION ALL
SELECT 'stock_prices', COUNT(*) FROM stock_prices
UNION ALL
SELECT 'financial_ratios', COUNT(*) FROM financial_ratios
UNION ALL
SELECT 'peer_groups', COUNT(*) FROM peer_groups;