This is a ReadMe file for the capstone of Shreyas Chitransh submitted as part of the BrainStation DataScience Diploma.


# <p align="center"> Topic Modelling Covid-19 Tweets </p> 

## Project Summary

A Topic Modeling Project using Twitter (later X) data to analyze underlying discussions during the first global Covid-19 major surge in March/April 2020. 

Topic modelling such as this can be used by government entities, influencers and promoters who get thousands of Tweets related to their policies or products. Using this workflow they can automatically get to know a summary of the mass opinions being shared, to better cater to their audience. 

This MVP can be custom tailored for, and scaled to the specific requirements of individuals, entities or organizations depending on their requirements. Once tailored, it can result in a quicker turn around time to track the trending opinions in more detail.


### Intro to the Problem Space

The Covid19 pandemic swept across the world starting in March 2020 and was continuing throughout the time this report was generated in June 2021. On the negative side it saw a lot of fear, grief, sadness while causing "great unrest in society and unprecedented changes in lifestyle, work and social interactions."[[1](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9052715/)].
Though, it also led to a lot of social solidarity and improvements "community involvement, family communication, behavior, sanitation, cleanliness, online learning, and distance learning."[[2](https://journals.lww.com/jfmpc/fulltext/2023/12090/positive_impacts_of_covid_19_on_social_life_and.75.aspx)]. All the while, social media (like Twitter (later X)) provides an outlet for people to discuss what they are going through. 

The unprecedented impacts of the pandemic in terms of loss of human lives and health were evident, 
however they also caused a chain reaction that disrupted most of the industries, and in turn the world economy. All of this was also being discussed on the global social platforms. 

This project was conducted to find out the globally discussed Covid19 pandemic related themes in depth. The focus was to elicit the underlying topics being discussed under the Covid-19 umbrella by analyzing Twitter data from the first major surge of global Covid19 cases, in March/April 2020. It conducted Topic Modelling using the Latent Dirichlet Allocation (LDA) model, and generated a summary list of topics discussed by the mass English speaking Twitter users.

### Intro to Data
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


### [Cleaning and EDA](https://github.com/shch92/Project__Topic_Modelling/blob/main/notebooks/1_DataLoading_Cleaning_and_Exploratory_Data_Analysis.ipynb)
The data was cleaned by removing duplicates and null values followed by filtering for English Tweets. In general, the data was quite clean, however it would’ve been preferred to have Tweets with more Covid19 related octothorps or ‘hashtags’. A final dataset of ~81k English Tweets was selected which represented the March/April 2020 timeframe. Exploration of the Tweet texts gave some great insights. 
- Majority of the Tweets comprised of 15-35 words (100-280 characters) with a long tail where they extended to upwards of 90 words (850 characters). 
- These outliers were found to be Tweets where the number of 'mentions' was high and/or the tweets contained shared website link(s).


### Methodology
In the modeling workflow the optional hyperparameters were not usable since they required a-priori knowledge about the number of topics or word probability expected. Therefore, the iterative model improvement was undertaken by:
- Changing the input data preprocessing 
- Number of topics were changed as methods to yield improved results. 

The model efficacy was evaluated using 2 methods:
- The Model Coherence Score, which evaluates the degree of semantic similarity between high scoring words in the topic.
- A self-devised method called Mixture and Randomness Score (MRS) which evaluates the amount of randomness in a model using the randomness of words in the top 30 terms associated with the topic. 

### Modelling
Overall there were tens of models attempted but only 4 are presented in the final notebooks due to relevance. PyLDAvis interactive visualization is used for analysing and understanding the results.  

**[Models 1 & 2](https://github.com/shch92/Project__Topic_Modelling/blob/main/notebooks/3_Topic_Modeling_Book_1.ipynb)**
- Corpus generated using Tweet preprocessing where the ‘stop words’, ‘links’, ‘&amp’, ‘dashes’ and ‘dots’ were removed, and the text tokenized as well as lemmatized.  
- Model 1 was generated using 5 topics, Model 2 was generated after finding the optimum number of topics (20) using coherency as a measure. 
- Lessons learnt from models 1 & 2 were used to change the preprocessing methodology as a means to improve models 3 & 4, 

**[Models 3 & 4](https://github.com/shch92/Project__Topic_Modelling/blob/main/notebooks/4_Topic_Modeling_Book_2.ipynb)**
- Changes include corpus bieng generated with additional steps of converting all words to lowercase while unifying all the Covid19 synonyms. 
- Model 3 generated using 5 topics and Model 4 generated after finding the optimum number of topics (being 10) that gave the highest coherence score. 


### Model Summary

The models and their respective evaluation parameters, as well as observations and issues can be seen below. It shows the successive improvement of model performance over preceding ones.

| Model Type (name) | Corpus Characteristics   | Number of Topics |  Coherence Score (%)  | Mixture & Randomness Score  | Comments   |
|:------:|:------:|:------:|:------:|:------:|:------:|
|  LDA Model 1  |corpus_LDA_with_Covid19_synonyms | 5   |~35.0|0.5 (in a range between: 0.2 - 1.2)| Model seemed to fit well to the corpus however 1 topic lacked specificity leading to the given randomness score.  | 
| LDA Model 2   | corpus_LDA_with_Covid19_synonyms|  20 | ~46.0| 0.625 (in a range between: 0.05 - 1.05) | Some topics showed high specificity however model seemed to overfit to the data. Lot's of small topic clusters with completely random terms. Undesirable even though higher Coherence Score as the MRS also increased.   |
|  LDA Model 3  |corpus_LDA_with_Only_Covid19|  5  | ~47.5|0.4 (in a range between 0.2 - 1.2) |  Changes in preprocessing show more promising results and better topic specificity. This is displayed in the improved MRS score.  Coherence score has increased as well. |
| LDA Model 4  | corpus_LDA_with_Only_Covid19| 10  | ~51.5 |0.35 (in a range between 0.1 - 1.2) |Topics showed high specificity however there is a small overfit to the data. First model with a specifically 'positive' point of view for Covid19. The smaller clusters are still quite coherent in the beginning but then increase in randomness. |


### Results
Model 4 was chosen while keeping in mind that a balance between coherence score and number of topics is required to maintain a low MRS. It was chosen because it:
- Had the highest Coherence score with the lowest MRS compared to all previous models.  
- Gave a better representation to most topics, and some of the smaller topics were able to identify underlying subtle discussions taking place.  


There was 1 completely random topic still present, which showed that even the best models cannot classify everything. In the final model, the main themes of the different topics (in order of prevalence) are given below with a reasoning:

1. Quarantine Silver Lining - showing how people were showing solidarity in the face of adversity with words such as ‘love’, ‘family’, ‘exercise’, ‘fun’ and ‘enjoy’;   
2. Business and Financial Impacts – because it out to be more severe than expected;  
3. Covid19 Tracking – this was an imperative out of the necessity to monitor the spread of Covid19; 
4. Covid19 Medical Advances – medical response for prevention, treatment and cure; 
5. USA Republican Politics – as a consequence of the US election with an outspoken president; 
6. Indian Politics w/ Randomness - India being the 3rd largest English Tweeting community with a proactive Prime Minister who used fight against Covid19 as a political tool; 
7. USA Democratic and Canadian Politics – as in 5; 
8. Random – contained words that couldn’t fit into other topics; 
9. Negative Lockdown Aspects – response of the suffering masses due to emotional/financial strains; 
10. American Conspiracy Theories – as a political and infodemic fallout from vested interests.

### Future Potential
In the future other aspects can also be tested such as:
- Vectorizing using TF-IDF or specific word embeddings instead of Bag of Words.
- Using a more updated dataset or using other topics. 

More details can be found in the [Final Report](https://github.com/shch92/Project__Topic_Modelling/blob/main/deliverables/Discussing%20the%20Covid19%20Pandemic_Report.pdf). Summaries of the project can also be seen in this midway [Progress Presentation](https://github.com/shch92/Project__Topic_Modelling/blob/main/deliverables/ChitranshShreyas_Progress_Standuup.pdf) and [Final Presentation](https://github.com/shch92/Project__Topic_Modelling/blob/main/deliverables/ChitranshShreyas_Final_Presentation_Capstone.pdf) of the capstone.

## Technical ReadMe

Welcome to the technicals folks! Here is the folder structure for running the project



### Directory Tree

Project__Topic_Modelling
```
.
├── README.md
├── deliverables
│   ├── ChitranshShreyas_Final_Presentation_Capstone.pdf
│   ├── ChitranshShreyas_Progress_Standuup.pdf
│   └── Discussing the Covid19 Pandemic_Report.pdf
├── image.png
├── notebooks
│   ├── 1_DataLoading_Cleaning_and_Exploratory_Data_Analysis.ipynb
│   ├── 2_Tweet_Exploratory_Data_Analysis.ipynb
│   ├── 3_Topic_Modeling_Book_1.ipynb
│   ├── 4_Topic_Modeling_Book_2.ipynb
│   ├── data
│   │   └── data.md
│   └── scripts
│       ├── 0__check_remove_all_link_slash_dot__corpuslistoflists.py
│       ├── 1__compute_coherence_score__ldamodel_corpuslistoflists_dic.py
│       ├── 2__get_lda_objects__corpuslistoflists_numberoftopicsinteger.py
│       ├── 3__plot_lda_vis__lda_model_bowcorpus_dic.py
│       ├── 4__preprocess_tweet__dataframe.py
│       └── 5__show_wordcloud__corpuslistoflists_titlestring.py
└── requirements.txt
```

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
It contains 34 csv files with a combined 4GB of data. Please contact the author through [LinkedIn](https://www.linkedin.com/in/schitransh/) if there are any problems with these steps. Thanks!
