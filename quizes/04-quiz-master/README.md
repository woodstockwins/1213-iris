# ![](https://ga-dash.s3.amazonaws.com/production/assets/logo-9f88ae6c9c3871690e33280fcf557f33.png) Quiz 4  

## Task

Your goal is to showcase your data collection skills, through use of an api specifically https://pokeapi.co/. 
It's not enough to just be able to collect data from an API, You should be gearing your collection to the problem at hand. Spend a few moments thinking of a y target, and label as such. Then think of a few features in the data that might be indicative of that target. The goal of this quiz is not to get a good model, but showcase your collection skills. So don't worry about model strength, just make the features make some sense to the target. 

You can collect data for any problem we have covered in class so far. (Classification, Regression, NLP ect) 

Deliverables:
- write a block of code that pulls every pokemon from the poke api database, regardless of how many entries are present, your code should stop once you hit the end of the pokedex.
- Populate the dataframe with at least FOUR features and a target labeled "(name)_TARGET " for example "HP_TARGET" or "Combined_power_TARGET" as well as the poke-name and pokenumber 
- Finally, save the csv to a folder labeled "data", and named "pokedex.csv". Push your code .py or .ipynb (Your choice) and the dataset to submissions and post the link in GC.


Hints
- Get a single pull and parse it for knowledge on which features and targets you want. 
- Avoid the move list as it's a very complex structure of nested dictionaries
- Due to time, the sleep timer is not necessary for this quiz. 
- Each pull comes with a status code. 

As always, this is an open note quiz, but source your help via code comments. 
