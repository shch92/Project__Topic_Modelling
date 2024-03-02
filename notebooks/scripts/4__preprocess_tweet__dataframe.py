# Defining function to preprocess tweets by lemmatization and removing stopwords and convert it into a corpus

def preprocess_tweet(df):
    
    """
    The function accepts a dataframe. The column in the dataframe which contains the text data to preprocess should be called 'text'
    otherwise the function will not work. 
    
    The function uses an empty list which is appended by words that are not in the stopwords_corpus and if they are non-stop words then 
    they are lemmatized.
    
    """
    
    # Instantiating the empty list
    corpus_LDA=[]
    
    # Instantiating the lemmatizer and stopwords_corpus 
    lem=WordNetLemmatizer()
    stopwords_corpus=set(stopwords.words('english'))
    
    # Assigning rules for each word in the tweet
    for tweet in df['text']:
        
        # In this rule 'word' is assigned to a tokenized
        words=[w for w in word_tokenize(tweet) if (w not in stopwords_corpus)]
        
        # Lemmatizes words that have more than 2 characters
        words=[lem.lemmatize(w) for w in words if len(w)>2]
        
        # Appends the lemmatized words into the corpus_LDA list
        corpus_LDA.append(words)
        
    # Returns the corpus_LDA list which can be assigned to a variable while calling the function 
    return corpus_LDA