# Nifty100 Analytics Dashboard

## Overview

Nifty100 Analytics Dashboard is a Streamlit-based financial analytics platform developed for analysing companies using financial ratios, balance sheets, profit & loss statements, cash flow statements, sector analysis and valuation metrics.

---

## Technologies

- Python
- Streamlit
- SQLite
- Pandas
- Plotly
- OpenPyXL

---

## Project Structure

src/
├── analytics/
│ └── valuation.py
├── dashboard/
│ ├── app.py
│ ├── utils/
│ │ └── db.py
│ └── pages/
│ ├── 01_home.py
│ ├── 02_profile.py
│ ├── 03_screener.py
│ ├── 04_peers.py
│ ├── 05_trends.py
│ ├── 06_sectors.py
│ ├── 07_capital.py
│ └── 08_reports.py

---

## Features

### Home Dashboard

- KPI Cards
- Sector Distribution
- Top Companies
- Financial Overview

### Company Profile

- Company Information
- Financial Ratios
- Profit & Loss
- Balance Sheet
- Cash Flow

### Stock Screener

- ROE Filter
- PE Filter
- Debt Filter
- CSV Export

### Peer Comparison

- KPI Comparison
- Radar Chart
- ROE Comparison
- PE Comparison

### Trend Analysis

- Multi Metric Trend
- Cash Flow Trend
- Balance Sheet Trend
- YoY Growth

### Sector Analysis

- Sector Distribution
- Bubble Chart
- Sector Summary

### Capital Allocation

- Assets
- Liabilities
- Equity
- Capital Summary

### Annual Reports

- Company Reports
- Report Links
- Company Details

### Valuation

- FCF Yield
- Sector PE
- Discount Detection
- Caution Detection

---

## Run Dashboard

```bash
streamlit run src/dashboard/app.py
```

---

## Generate Valuation

```bash
python src/analytics/valuation.py
```

---

## Output Files

output/

- valuation_summary.xlsx
- valuation_flags.csv

---

## Developed Using

- Streamlit
- Plotly
- SQLite
- Pandas