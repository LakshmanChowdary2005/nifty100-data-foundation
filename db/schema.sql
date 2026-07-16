PRAGMA foreign_keys = ON;

-- Companies
CREATE TABLE IF NOT EXISTS companies (
    company_id INTEGER PRIMARY KEY,
    company_name TEXT NOT NULL,
    ticker TEXT UNIQUE,
    sector TEXT
);

-- Profit & Loss
CREATE TABLE IF NOT EXISTS profitandloss (
    company_id INTEGER,
    year INTEGER,
    sales REAL,
    net_profit REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Balance Sheet
CREATE TABLE IF NOT EXISTS balancesheet (
    company_id INTEGER,
    year INTEGER,
    assets REAL,
    liabilities REAL,
    equity REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Cash Flow
CREATE TABLE IF NOT EXISTS cashflow (
    company_id INTEGER,
    year INTEGER,
    operating_cf REAL,
    investing_cf REAL,
    financing_cf REAL,
    PRIMARY KEY(company_id, year),
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Analysis
CREATE TABLE IF NOT EXISTS analysis (
    company_id INTEGER,
    year INTEGER,
    rating TEXT,
    remarks TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Documents
CREATE TABLE IF NOT EXISTS documents (
    company_id INTEGER,
    document_type TEXT,
    url TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Pros & Cons
CREATE TABLE IF NOT EXISTS prosandcons (
    company_id INTEGER,
    pros TEXT,
    cons TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Sectors
CREATE TABLE IF NOT EXISTS sectors (
    sector_id INTEGER PRIMARY KEY,
    sector_name TEXT
);

-- Stock Prices
CREATE TABLE IF NOT EXISTS stock_prices (
    company_id INTEGER,
    date TEXT,
    open REAL,
    high REAL,
    low REAL,
    close REAL,
    volume INTEGER,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Financial Ratios
CREATE TABLE IF NOT EXISTS financial_ratios (
    company_id INTEGER,
    roe REAL,
    roa REAL,
    de_ratio REAL,
    pe_ratio REAL,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);

-- Peer Groups
CREATE TABLE IF NOT EXISTS peer_groups (
    company_id INTEGER,
    peer_company TEXT,
    FOREIGN KEY(company_id) REFERENCES companies(company_id)
);