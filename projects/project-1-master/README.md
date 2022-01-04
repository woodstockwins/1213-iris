# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis

### Overview

### This Project will explore standardized test scores in California:
- How do Charter schools and Public school test scores compare.
- Where are the most affordable Counties in Calfiornia to live with good schools?
- Where are the top ranked Counties in California ranked by standardized test scores?

### Problem Statement:
This project will explore standardized test scores between public schools and charter schools. Parents can choose to use the information uncovered to aid in the decision of where to raise and how to educate their children.

### Target Audience:
Parents with children preparing for the SAT/ACT looking to relocate in California.


### Collecting the Data:
The first step in the data analysis process is gathering the relevant data necessary to perform analysis on. To do this, we inspect the supplied data to get an initial idea of direction. ACT & SAT data was readily available to peak through on the California Department of Education's website. [[CA Department of Education]](https://www.cde.ca.gov/ds/sp/ai/reclayoutact19.asp)

Charter schools have been in the news in California recently, so tackling a project that is topical and potentially insightful appeared to have value. However, no data on charter schools was supplied. The California Department of Education is a great resource. Their website allows one to filter by county, school type, and many other features. I put together a Selenium scraper to naviage the 50+ County pages for California and compiled all the information into a tidy .csv file. The web scraper can be found in the './school_scraper/' directory along with the raw charter school data. To be sure no private schools were included in the analysis the CDE was also able to provide a list of private schools for a quick cross-referencing.
[[CA Department of Education]](https://www.cde.ca.gov/SchoolDirectory/)

Housing data was need for a more detailed inspection of where parents might want to consider locating their family. The National Association of Realtors was the perfect place to gather median home values for every county. Their websites provided a tidy .csv document. 
[[NAR]](https://www.nar.realtor/research-and-statistics/housing-statistics/county-median-home-prices-and-monthly-mortgage-payment)

Lastly, the United States Census Bureau generously indexed all the cities, counties, states (and more) into a nice numerical formal. This indexing is refereed to as the Federal Information Processing Standards (FIPS). FIPS data would be needed for graphical displays. [[US Census Bureau]](https://www.census.gov/geographies/reference-files/2016/demo/popest/2016-fips.html) 


### Cleaning the Data:
1. 0_school_parse.ipynb is the first of 3 workbooks included in the project. Inside, the initial steps of Expoloritory Data Analysis are completed. Data is previewed, NULL values are handled and the data itself is cleaned/prepared for analysis. Further details are included within the Notebook.

2. 1_exam_score_exploration.ipynb is the second step in the project. Here data is cleaned a little further as it is aggregated and merged into useable data frames and the first visualizations of the data are formed. Initial insights are shared and the data begins to tell it's story. As insights were uncovered, the plot thickens. I was quite surprised with the findings. They are shared inside the Notebook and shared as the story unfolds.

3. 2_housing_values.ipynb is the final stage of the data analysis. The goal of the Notebook is to pivot from expoloritory analysis into usable insights. Here is where parents can process the data and make important decisions for themselves. My intention is not to tell parents what to think or how to raise their children, but rather to share the data in a way that will allow parents to think objectively about the decisions that will work best for their specific circumstances. The scope is intended to be broad.

### Housekeeping:
- Raw data files are stored in the './data/' directory. The data here has not been modified heavily. It remains there so the data cleaning process can be appreciated.

- Cleaned data are stored in the './data-clean/ directory after working its way thru the 0_school_parse.ipynb Notebook.

- The Notebooks (described above) used to clean, analyse, and visualize the data are stored in the './code/' directory.

- Images used in the 'choosing_education.pdf' slide-deck are saved in the './images/' directory.


### Takeaway Nugget:
Please enjoy the analysis prepared. I hope it sparks thought and inspires you to do your own research on charter schools in California or around the World. Fun fact for making it this far into the README: charter schools first came about in 1733 to provide a 'Protestant education' to the poorest of the Catholic citizens of Ireland.
