# Data Visualization — Books Dataset

**Suggested GitHub repository:** `CodeAlpha_DataVisualization`  
**Author:** Dhriti Sundar Goze  
**Tools:** Python, Pandas, Matplotlib

## Overview
This project turns a structured books dataset into clear visualizations that help explain price distributions, rating patterns, category counts, and the relationship between price and rating. It builds on the sample dataset used in the Web Scraping and EDA projects.

The bundled CSV is a small illustrative preview. For more meaningful findings, run the companion scraper to produce a larger dataset and pass that CSV to this project.

## Questions this project explores
- How are book prices distributed?
- Which ratings appear most often?
- Which categories have the most books?
- Does price appear to vary with rating?
- What are the average prices by rating?

## Project structure
```text
CodeAlpha_DataVisualization/
├── src/
│   └── visualize.py
├── data/
│   └── books_sample.csv
├── reports/
│   └── visualization_report.md
├── requirements.txt
├── .gitignore
└── README.md
```

## Install
Python 3.9+ recommended.

```bash
python -m pip install -r requirements.txt
```

## Run
From the project root:

```bash
python src/visualize.py
```

Use a larger dataset:
```bash
python src/visualize.py --input ../CodeAlpha_Web_Scraping_Project/data/books_scraped.csv
```

Specify a custom output folder:
```bash
python src/visualize.py --input data/books_sample.csv --output-dir reports/charts
```

## Visual outputs
The script creates PNG charts and a concise text summary:
- `price_distribution.png` — histogram of prices
- `rating_counts.png` — count of books by rating
- `top_categories.png` — categories with the most books
- `price_vs_rating.png` — scatter plot of price against rating
- `average_price_by_rating.png` — average price for each rating
- `visualization_summary.txt` — key dataset facts and interpretation cautions

## Design choices
- Titles and axis labels are descriptive.
- Figures use a consistent size and readable layout.
- Categories are sorted for easier comparison.
- Plots are saved as high-quality PNG files suitable for a portfolio README or report.
- The script checks for missing columns and skips charts that cannot be created.

## GitHub details
**Repository name:** `CodeAlpha_DataVisualization`

**Description:** `Python data visualization project using Pandas and Matplotlib to create clear charts from a scraped books dataset, including price distributions, rating and category comparisons, price-rating relationships, and a concise insight summary.`

**Suggested commit name:** `Add data visualization project`

**Commit description:** `Create reusable Matplotlib visualizations for book prices, ratings, categories, and price-rating relationships; include sample data, generated chart outputs, and project documentation.`

## Interpretation and limitations
The bundled data has only a few illustrative rows and should not be used to make broad claims. Use the full scraped dataset for meaningful patterns. A scatter plot or average comparison shows association, not causation.
