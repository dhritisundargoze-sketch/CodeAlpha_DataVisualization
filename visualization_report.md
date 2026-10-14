# Data Visualization Project Report

**Prepared by:** Dhriti Sundar Goze  
**Project:** Visual Analysis of a Scraped Books Dataset  
**Tools:** Python, Pandas, Matplotlib

## 1. Introduction
Data visualization presents raw data in charts and graphs so people can understand distributions, comparisons, and relationships more easily. This project creates a small set of reusable visualizations from a structured book dataset.

## 2. Objectives
- Convert raw book records into clear charts.
- Explore price distribution and rating counts.
- Compare book categories.
- Explore whether prices vary with ratings.
- Produce portfolio-ready PNG images and a summary.

## 3. Questions
1. What is the distribution of book prices?
2. Which ratings occur most frequently?
3. Which categories contain the most books?
4. How do prices vary across ratings?
5. What are the average prices for each rating?

## 4. Visualizations
- **Price histogram:** shows the distribution of prices and possible skew.
- **Rating bar chart:** compares counts for each star rating.
- **Top categories horizontal bar chart:** makes category counts easy to compare.
- **Price-versus-rating scatter plot:** explores a possible relationship between rating and price.
- **Average price by rating bar chart:** compares mean prices across rating groups.

## 5. Storytelling and decision support
A useful data story starts with a question, presents the most relevant chart, explains the observed pattern, and states its limitations. For example, a category-count chart can show which categories are most represented in the collected sample, while a price histogram can show whether prices cluster in a particular range. These observations can guide follow-up analysis but should not be interpreted as causal explanations.

## 6. Limitations
The bundled dataset is a small illustrative sample and is not suitable for broad conclusions. Run the companion scraper to obtain a larger dataset. The charts describe only the records supplied to the script.

## 7. Conclusion
This project demonstrates how Python and Matplotlib can transform structured data into understandable visual outputs. The generated charts and summary can be included in a GitHub portfolio and expanded with a larger dataset or an interactive dashboard in a future iteration.
