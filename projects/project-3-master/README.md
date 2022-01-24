# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Project 3: Web APIs & NLP

### Description

In this project you'll use your skills with Python, machine learning, APIs, and NLP. 

For project 3, your goal is two-fold:
1. Using [Pushshift's](https://github.com/pushshift/api) API, collect posts from two subreddits of your choosing.
2. Then use NLP to train a classifier to determine which subreddit a given post came from. This is a binary classification problem.


#### About the API

You'll be using Pushshift's API. As an example, if you want to get posts from [`/r/boardgames`](https://www.reddit.com/r/boardgames), use the following url: https://api.pushshift.io/reddit/search/submission?subreddit=boardgames

To help you get started, we have a primer video on how to use the API: https://youtu.be/AcrjEWsMi_E

---
## Checkpoints and Advice

If you aren't familiar with [reddit](https://www.reddit.com/), go check it out and browse different subreddits. Each subreddit is like a forum on a different topic. [Here's a list of subreddits by topic.](https://www.reddit.com/r/ListOfSubreddits/wiki/listofsubreddits)

- In your project you can classify posts, comments, titles, or some combination of those things. What you choose will partly determine how difficult your data cleaning will be and how challenging the classification task will be for your algorithms. In your presentation and executive summary, **tell us what you used**.

- You can also include other information from posts or comments as features, but you must include some text.

- You can make the project more challenging by choosing subreddits that are more similar. 

- You you should have your subreddits chosen by Friday. **You must insert your subreddits into [this Google Sheet](https://docs.google.com/spreadsheets/d/170buASiuu6NmJjCBlsnHHgyPobOGO0sDKFaTTvxMbsc/edit?usp=sharing).** You may not choose the same subreddits as someone else. First come, first reserved. 🙂

- Also by COB  Friday, you should have a function that is pulling data from the API. 

- The more data you can pull the better for your classifier. You will want data from at least 300 unique, non-null posts from each subreddit.

- You can find an example executive summary [here](https://www.proposify.biz/blog/executive-summary).


---

### Requirements

- Gather and prepare your data using the `Pushshift` library.
- **Create and compare at least two models**. One of these must be a Bayes classifier, the other can be a classifier of your choosing: logistic regression, KNN, etc.
- A Jupyter Notebook with your analysis for a peer audience of data scientists.
- An executive summary of your results.
- A short presentation outlining your process and findings for a semi-technical audience.



---

### Necessary Deliverables 

- Code and executive summary must be in a clearly commented Jupyter Notebook.
- You must submit your slide deck by the start of presentations.
- Your repo must be submitted by 9:00PM ET on the day of presentations.

---

## Rubric
Your instructional team will evaluate your project using the following criteria.  

For Project 3 the evaluation categories are as follows:<br>
**The Data Science Process**
- Problem Statement 
- Data Collection
- Data Cleaning & EDA
- Preprocessing & Modeling
- Evaluation and Conceptual Understanding
- Conclusion and Recommendations

**Organization and Professionalism**
- Organization
- Visualizations
- Python Syntax and Control Flow
- Presentation

**Scores will be out of 30 points based on the 10 categories in the rubric.** <br>
*3 points per section*<br>

**You must get at least a _1_ in each section to pass the project.**

| Score | Interpretation                                                                                                                  |
| ----- | ------------------------------------------------------------------------------------------------------------------------------- |
| **0** | *Project fails to meet the minimum requirements for this item.*                                                                 |
| **1** | *Project meets the minimum requirements for this item, but falls significantly short of portfolio-ready expectations.*          |
| **2** | *Project exceeds the minimum requirements for this item, but falls short of portfolio-ready expectations.*                      |
| **3** | *Project meets or exceeds portfolio-ready expectations; demonstrates a thorough understanding of every outlined consideration.* |


### The Data Science Process

**Problem Statement**
- Is it clear what the goal of the project is?
- What type of model will be developed?
- How will success be evaluated?
- Is the scope of the project appropriate?
- Is it clear who cares about this or why this is important to investigate?
- Does the student consider the audience?

**Data Collection**
- Was enough data gathered to generate a significant result?
- Was data collected that was useful and relevant to the project?
- Was thought given to the server receiving the such as considering number of requests per second?

**Data Cleaning and EDA**
- Are missing values imputed/handled reasonably?
- Are distributions examined and described?
- Are outliers identified and addressed?
- Are appropriate summary statistics provided?
- Are steps taken during data cleaning and EDA framed appropriately?
- Does the student address whether they are likely to be able to answer their problem statement with the provided data given what they've discovered during EDA?

**Preprocessing and Modeling**
- Is text data successfully converted to a numeric representation?
- Are methods such as stop words, stemming, and lemmatization explored?
- Does the student properly split and/or sample the data for validation/training purposes?
- Does the student test and evaluate a variety of models to identify a production algorithm (**AT MINIMUM:** Bayes and one other model)?
- Does the student defend their choice of a final model relevant to the data at hand and the problem?
- Does the student explain how the model works and evaluate its performance successes/downfalls?

**Evaluation and Conceptual Understanding**
- Does the student accurately identify and explain the baseline score?
- Does the student select and use metrics relevant to the problem objective?
- Does the student interpret the results of their model for purposes of inference?
- Is domain knowledge demonstrated when interpreting results?
- Does the student provide appropriate interpretation with regards to any descriptive and inferential statistics?

**Conclusion and Recommendations**
- Does the student provide appropriate context to connect individual steps back to the overall project?
- Are the conclusions/recommendations clearly stated?
- Does the conclusion answer the original problem statement?
- Are future steps to move the project forward identified?


### Organization and Professionalism

**Project Organization**
- Are modules imported correctly (using appropriate aliases)?
- Are data imported/saved using relative paths?
- Does the README provide a good executive summary of the project?
- Is Markdown formatting used appropriately to structure notebooks?
- Is the process explained in comments/Markdown?
- Are files & directories organized?
- Do files and directories have well-structured, appropriate, consistent names?

**Visualizations**
- Are sufficient visualizations provided?
- Do plots accurately demonstrate valid relationships?
- Are plots labeled properly?
- Are plots interpreted appropriately?
- Are plots formatted and scaled appropriately for inclusion in a notebook-based technical report?

**Python Syntax and Control Flow**
- Is care taken to write human readable code?
- Is the code syntactically correct (no runtime errors)?
- Does the code generate desired results (logically correct)?
- Does the code follows general best practices and style guidelines?

**Presentation**
- Is the problem statement clearly presented?
- Does a strong narrative run through the presentation building toward a final conclusion?
- Are the conclusions/recommendations clearly stated?
- Is the level of technicality appropriate for the intended audience?
- Does the student appropriately pace their presentation?
- Does the student deliver their message with clarity and volume?
- Are appropriate visualizations generated for the intended audience?
- Are visualizations necessary and useful for supporting conclusions/explaining findings?


---

### Why did we choose this project?
This project encompasses at least four areas that we cover in the course: Classification, Natural Language Processing, Data Acquisition, and Communication.
