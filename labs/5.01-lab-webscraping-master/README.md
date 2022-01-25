
# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Web Scraping  Lab


In this lab, you will use `BeautifulSoup` to scrape data from [this page](https://pages.git.generalassemb.ly/rldaggie/for-scraping/) and create a DataFrame of food items from each restaurant. Your DataFrame should look something like this:

| restaurant | category | name    | calories | carbs | fat |
|------------|----------|---------|----------|-------|-----|
| McDonald's | Burgers  | Big Mac | 540      | 45    | 29  |
| Burger King | Burgers  | Whopper | 900      | 51    | 57  |
| ... | ...  | ... | ...      | ...    | ...  |
| Chili's | Ribs  | Shiner Bock® BBQ Ribs | 2310      | 168    | 123  |


**Note**: Your DataFrame should have just over 5,000 rows.

---

## Materials We Provide


| Topic | Description | Link |
| --- | --- | --- |
| Lab |  Web Scraping Jupyter Notebook | [Link](./starter-code.ipynb)|

---

## Prerequisites

Before this activity, students should already be able to:
- Understand basic HTML
- Use the inspector to interpret a website's HTML
- Use the `requests` and `BeautifulSoup` libraries
- Use the `pd.read_html` function to scrape tables
