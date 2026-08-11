# 🏢 Moroccan Real Estate Web Scraper & Price Analyzer

A Python-based data pipeline designed to scrape, clean, and analyze rental real estate listings in Marrakech, Morocco from Mubawab.

---

## 📌 Project Overview
This project automates the collection of rental property data across multiple pages. It extracts raw property listings, cleans structural price anomalies (converting non-standard currency strings into clean integer metrics), handles edge cases, and calculates statistical metrics for real estate insights.

---

## 🛠️ Tech Stack & Libraries
* **Python 3.x**
* **Selenium:** Dynamic browser automation & web scraping.
* **Pandas:** Data structuring, cleaning, and statistical analysis.

---

## 📊 Key Findings (Marrakech Sample Analysis)
* **Total Listings Scraped:** 33+ ads per page
* **Average Rental Price:** ~18,625 DH
* **Highest Rental Price:** 50,000 DH
* **Cheapest Rental Price:** 1,000 DH

---

## 📂 Project Structure
```text
├── mubawab_scraper.py   # Selenium script for multi-page scraping & cleaning
├── analyze.py           # Pandas analysis script for stats calculation
├── mubawab_marrakech.csv # Output structured CSV dataset
└── README.md            # Project documentation
