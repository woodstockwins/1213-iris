# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 1: Standardized Test Analysis

### Overview

### This Project will explore standardized test scores in California:
- How do Charter school and Public school test scores compare.
- Where are the most affordable Counties in California to live with good schools?
- Where are the top ranked Counties in California ranked by standardized test scores?

### Problem Statement:
This project will explore standardized test scores between public schools and charter schools. Parents can choose to use the information uncovered to aid in the decision of where to raise and how to educate their children.

### Target Audience:
Parents with children preparing for the SAT/ACT looking to relocate in California.

### Collecting the Data:
The first step in the data analysis process is gathering the relevant data necessary to perform analysis on. To do this, we inspect the supplied data to get an initial idea of direction. ACT & SAT data was readily available to peak through on the California Department of Education's website. [[CA Department of Education]](https://www.cde.ca.gov/ds/sp/ai/reclayoutact19.asp)

Charter schools have been in the news in California recently, so tackling a project that is topical and potentially insightful appeared to have value. However, no data on charter schools was supplied. The California Department of Education is a great resource. Their website allows one to filter by county, school type, and many other features. I put together a Selenium scraper to navigate the 50+ County pages for California and compiled all the information into a tidy .csv file. The web scraper can be found in the './school_scraper/' directory along with the raw charter school data. To be sure no private schools were included in the analysis the CDE was also able to provide a list of private schools for a quick cross-referencing.
[[CA Department of Education]](https://www.cde.ca.gov/SchoolDirectory/)

Housing data was need for a more detailed inspection of where parents might want to consider locating their family. The National Association of Realtors was the perfect place to gather median home values for every county. Their websites provided a tidy .csv document. 
[[NAR]](https://www.nar.realtor/research-and-statistics/housing-statistics/county-median-home-prices-and-monthly-mortgage-payment)

Lastly, the United States Census Bureau generously indexed all the cities, counties, states (and more) into a nice numerical formal. This indexing is referred to as the Federal Information Processing Standards (FIPS). FIPS data would be needed for graphical displays. [[US Census Bureau]](https://www.census.gov/geographies/reference-files/2016/demo/popest/2016-fips.html) 

### Cleaning the Data:
1. 0_school_parse.ipynb is the first of 3 workbooks included in the project. Inside, the initial steps of Exploratory Data Analysis are completed. Data is previewed, NULL values are handled and the data itself is cleaned/prepared for analysis. Further details are included within the Notebook.

2. 1_exam_score_exploration.ipynb is the second step in the project. Here data is cleaned a little further as it is aggregated and merged into useable data frames and the first visualizations of the data are formed. Initial insights are shared, and the data begins to tell its story. As insights were uncovered, the plot thickens. I was quite surprised with the findings. They are shared inside the Notebook and developed as the story unfolds. My goal was to let the data tell the story.

3. 2_housing_values.ipynb is the final stage of the data analysis. The goal of the Notebook is to pivot from exploratory analysis into usable insights. Here is where parents can process the data and make important decisions for themselves. My intention is not to tell parents what to think or how to raise their children, but rather to share the data in a way that will allow parents to think objectively about the decisions that will work best for their specific circumstances. The scope is intended to be broad.

### Housekeeping:
- Raw data files are stored in the './data/' directory. The data here has not been modified heavily. It remains there so the data cleaning process can be appreciated.

- Cleaned data are stored in the './data-clean/ directory after working its way thru the 0_school_parse.ipynb Notebook.

- Images used in the 'choosing_education.pdf' slide-deck are saved in the './images/' directory.

### Fun Nugget:
Please enjoy the analysis prepared. I hope it sparks thought and inspires you to do your own research on charter schools in California or around the World. Fun fact for making it this far into the README: charter schools first came about in 1733 to provide a 'Protestant education' to the poorest of the Catholic citizens of Ireland.


### Takeaways & Project Spoilers:
#### Public school SAT proficiency outperforms chart schools by roughly 10% on average.
#### If parents want affordable counties with high test scores, they should consider Mariposa, Shasta, Trinity, Fresno, Mono, Amador, Calaveras, Butte or Humboldt.
#### If parents want the BEST education, they should consider Santa Cruz, Shasta, Santa Clara, Alameda, or Marin

## Data Dictionary
|Feature|Type|Dataset|Description|
|---|---|---|---|
|local_id|float|CA ACT|State assigned identifier: full|
|county_id|float|CA ACT|State assigned identifier: county|
|county_dist_id|float|CA ACT|State assigned identifier: district|
|school_id|float|CA ACT|State assigned identifier: school|
|record_type|object|CA ACT|State assigned categorical identifier|
|school_name|object|CA ACT|Name of the school|
|dist_name|object|CA ACT|Name of the school district|
|county_name|object|CA ACT|Name of the county|
|enrollment_12|float|CA ACT|Number of students enrolled in the school|
|test_takers|float|CA ACT|Number of students that completed the ACT|
|avg_read|int|CA ACT|Average ACT score of all students in sample for the Reading portion of the exam|
|avg_eng|int|CA ACT|Average ACT score of all students in sample for the English portion of the exam|
|avg_math|int|CA ACT|Average ACT score of all students in sample for the Math portion of the exam|
|avg_sci|int|CA ACT|Average ACT score of all students in sample for the Science portion of the exam|
|comp_score|float|CA ACT|Composite ACT score of all students in sample. Commonly referred to as, 'ACT score'|
|abv_avg_num|int|CA ACT|Total number of students to record an ACT composite score at or above 21|
|abv_avg_pct|float|CA ACT|Percentage of test takers to record an ACT composite score at or above 21 (percentage 10.3 = 10.3%)|
|year|int|CA ACT|Year of exam|
|is_charter|int|CA ACT|Charter school categorical identifier (1 = school is a Charter while 0 = school is not a Charter)|
|local_id|float|CA SAT|State assigned identifier: full|
|county_id|float|CA SAT|State assigned identifier: county|
|county_dist_id|float|CA SAT|State assigned identifier: district|
|school_id|float|CA SAT|State assigned identifier: school|
|record_type|object|CA SAT|State assigned categorical identifier|
|school_name|object|CA SAT|Name of the school|
|dist_name|object|CA SAT|Name of the school district|
|county_name|object|CA SAT|Name of the county|
|enrollment_12|float|CA SAT|Number of students enrolled in the school|
|test_takers|float|CA SAT|Number of students that completed the SAT|
|avg_eng|int|CA SAT|Number of students at the school to score at least 480 on the English portion of the exam|
|pct_eng|float|CA SAT|Percentage of test takers at the school to score at least 480 on the English portion of the exam (percentage 10.3 = 10.3%)|
|avg_math|int|CA SAT|Number of students at the school to score at least 530 on the Math portion of the exam|
|pct_math|float|CA SAT|Percentage of test takers at the school to score at least 530 on the Math portion of the exam (percentage 10.3 = 10.3%)|
|abv_avg_both|int|CA SAT|Number of students at the school to score at least 480 on English and at least 530 on the Math portions of the exam|
|abv_pct_both|float|CA SAT|Percentage of test takers at the school to score at least 480 on English and at least 530 on the Math portions of the exam (percentage 10.3 = 10.3%)|
|year|int|CA SAT|Year of exam|
|is_charter|int|CA SAT|Charter school categorical identifier (1 = school is a Charter while 0 = school is not a Charter)|
|county_name|object|Housing Values|Name of the county|
|med_home_value|int|Housing Values|Median home price of the county|
|sat_score_range|object|SAT Score Distribution|Categorical range of SAT scores|
|fips|int|FIPS|CA State assigned code for County classification. Used only for graphing|
|county_name|object|FIPS|Name of the County|

