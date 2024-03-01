This is a ReadMe file for the capstone of Shreyas Chitransh submitted as part of the BrainStation DataScience Diploma.


# <p align="center"> Topic Modelling Covid-19 Tweets </p> 

A Topic Modeling Project using Twitter (later X) data to analyze underlying discussions during the first global Covid-19 major surge in March/April 2020. 


## Intro to the Problem Space

The Covid19 pandemic swept across the world starting in March 2020 and was continuing throughout the time this report was generated in June 2021. On the negative side it saw a lot of fear, grief, sadness while causing "great unrest in society and unprecedented changes in lifestyle, work and social interactions."[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9052715/).
Though, it also led to a lot of social solidarity and improvements "community involvement, family communication, behavior, sanitation, cleanliness, online learning, and distance learning."[[2](https://journals.lww.com/jfmpc/fulltext/2023/12090/positive_impacts_of_covid_19_on_social_life_and.75.aspx)]. All the while, social media (like Twitter (later X)) provides an outlet for people to discuss what they are going through. 

The unprecedented impacts of the pandemic in terms of loss of human lives and health were evident, 
however they also caused a chain reaction that disrupted most of the industries, and in turn the world economy. All of this was also being discussed on the global social platforms. 

This project was conducted to find out the globally discussed Covid19 pandemic related themes in depth. The focus was to elicit the underlying topics being discussed under the Covid-19 umbrella by analyzing Twitter data from the first major surge of global Covid19 cases, in March/April 2020. It conducted Topic Modelling using the Latent Dirichlet Allocation (LDA) model, and generated a summary list of topics discussed by the mass English speaking Twitter users.

## Intro to Data
Data Dictionary 
The information that each column provides is generally taken from BirdIQ here and is given below:
| COLUMN  | DESCRIPTION |
|:---|:---|
|`status_id`  |  A unique identification number associated with the Tweet |
|`user_id`| A unique identification number associated with the user generating the Tweet|  
|`created_at`| The date on which the Tweet was generated|  
|`screen_name`| The user name of the user generating the Tweet|  
|`text`| The actual text of the Tweet|  
|`source`| Utility (e.g. Web client etc.) used to post the Tweet|  
|`reply_to_status_id`| If the represented Tweet is a reply, this will contain the original Tweet’s ID|  
|`reply_to_user_id`| If the represented Tweet is a reply, this will contain the original Tweet’s author ID|  
|`reply_to_screen_name`| If the represented Tweet is a reply, this will contain the screen name of the original Tweet’s author|  
|`is_quote`| Indicates whether this Tweet is a quote or not|  
|`is_retweet`| Indicates whether this Tweet has been retweeted by the authenticating user|  
|`favourites_count`| Approximate number of times the original Tweet has a 'like' by a Twitter user|  
|`retweet_count`| The number of times this Tweet has been retweeted|  
|`country_code`| The shortened country code representing the country containing the place|  
|`place_full_name`| Short human-readable representation of the place’s name this Tweet is associated with but not necessarily originating from|  
|`place_type`| The type of location represented by this place|  
|`followers_count`| The number of 'followers' this account currently has|  
|`friends_count`| The number of users this account is following|  
|`account_lang`| The language code for the user’s self-declared user interface language|  
|`account_created_at`| The UTC date and time that the user account was created on Twitter|  
|`verified`| Whether an account of public interest is verified by Twitter to be authentic|
|`lang`| Language identifier corresponding to the machine-detected language of the Tweet text| 

## Technical ReadMe

Welcome to the technicals folks! Here is the folder structure for running the project



### Directory Tree

├── notebooks  
│   ├── 1_DataLoading_Cleaning_and_Exploratory_Data_Analysis.ipynb  
│   ├── 2_Tweet_Exploratory_Data_Analysis.ipynb  
│   ├── 3_Topic_Modeling_Book_1.ipynb  
│   ├── 4_Topic_Modeling_Book_2.ipynb  
│   ├── data  
│   │  
│   ├── scripts  
│   │   ├──function__check_remove_all_link_slash_dot__corpuslistoflists.py  
│   │   ├──function__compute_coherence_score__ldamodel_corpuslistoflists_dic.py  
│   │   ├──function__get_lda_objects__corpuslistoflists_numberoftopicsinteger.py  
│   │   ├──function__plot_lda_vis__lda_model_bowcorpus_dic.py  
│   │   ├──function__preprocess_tweet__dataframe.py  
│   │   ├──function__show_wordcloud__corpuslistoflists_titlestring.py  
│   │   │  
│   │   │  
├── .gitignore  
├── README.md  
├── requirements.txt  
  


### Environment
You can create the environment for the project on gitbash (Windows) or Terminal (Mac) by downloading the requirements.txt and running:

 - Using pip
`pip install -r requirements.txt`

 - Using Conda
`conda create --name <env_name> --file requirements.txt`


### Data
This should be done before running the first notebook. 
Please use [this link](https://drive.google.com/drive/folders/1wr3j5ksoKTn7A1BeIStQ4NEJry6NGu8p?usp=sharing) to download the original dataset into the 'data' folder.
Please Note: The link leads you to a google drive folder called 'Shreyas_Chitransh_Capstone_Data'. This folder has a compressed file within it, called 'data'.
This compressed file should be unzipped and the 'data' folder added to the 'Chitransh_Shreyas_Capstone' folder.
It contains 34 csv files with a combined 4GB of data. Please contact Shreyas at +1-416-262-0992 (or shch92@gmail.com) if there are any problems with these steps. Thanks!
