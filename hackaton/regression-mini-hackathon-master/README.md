# Predicting Health Care Costs Mini-hackathon Group Challenge

Have fun and develop your modeling skills! 🚀

## Goal

Predict `charges` using the other columns.

Make a model with the lowest RMSE on your randomly determined 25% of the test (holdout) set, without any data leakage. 

Generally, you'll want to dig deeply into your data with EDA and you'll have more information about the data to help you. However, today the focus is on practicing your modeling skills in scikit-learn.


## Roles

Work together

- Each group member is responsible for asking "what?" or why?" if they don't understand the reason the group is doing something.
- Help each other out.
- Usual breakout room norms apply to make for the best learning environment - cameras on and share a screen. 


## Instructions

Use GridSearchCV and any of the following models you like:

- LinearRegression
- Lasso
- Ridge
- ElasticNet
- KNN

- Don't drop rows from your DataFrame or X. You want X_test to be as similar to data your model might encounter in the wild - when it needs to make predicitons - as possible. If you throw out the hard cases from what will become X_test, your score on your test set will look better than it would be in the wild.
- You can make as many models as you like.
- You can use a pipeline and grid search if you like.
- Does your model beat a null baseline model?
- The data is in the `data` folder.
- Use `22` for the `random_state` anytime you have randomization.
- You will have at least 90 minutes to work on this project. The exact stopping time will be shared in Slack at least 15 minutes prior to the stopping time. 
- Very brief (2-3 min), informal presentations from one member per group will follow. Share a notebook, no slides and tell us about ONLY YOUR BEST MODEL.


### Advice
- Get a basic model working quickly. You can start with a single numeric feature. Then iterate. 

### Have fun and good luck! 😀