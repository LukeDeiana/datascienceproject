# datascienceproject
This project analyzes SpaceX launch data to investigate factors influencing launch success. It employs data collection, cleaning, exploratory data analysis (EDA), interactive visualization, and predictive modeling.

Project Overview

Data Collection: Data was gathered via the SpaceX API (endpoints: /launches, /rockets, /capsules) and supplemented with web scraping from Wikipedia using BeautifulSoup.
Data Wrangling: The dataset was cleaned and prepared using pandas, including date conversion and handling missing values.

Exploratory Data Analysis (EDA): Visualizations (scatter plots, bar charts) were created with matplotlib and seaborn to explore relationships between variables like launch site, payload mass, and orbit type.

Interactive Dashboard: A Plotly Dash dashboard was built, featuring a pie chart for success counts and a scatter plot for payload vs. outcome, with a range slider for filtering.

Predictive Analysis: A logistic regression model was trained to predict launch success, achieving 100% accuracy (note: potential overfitting; further validation needed).

Key Findings
Three unique launch sites: CCAFS SLC 40, VAFB SLC 4E, KSC LC 39A.
Total payload mass: 549,446.35 kg.
Success rates vary by orbit type (e.g., 100% for SSO, 60% for ISS).
Yearly success rate peaked at 80% in 2018.
Predictive model achieved 100% accuracy but may require additional testing.
