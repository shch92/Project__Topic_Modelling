
# Defining a function to generate a wordcloud with a specific title

def show_wordcloud(corpus, title = "Word Cloud of Corpus"):
    """
    This function takes a corpus as a list of lists and generates a word cloud with 150 words while removing any stopwords that may be present.

    The collocations is switched off. Collocations can be turned on, however it  allows for bi-grams to be present in the wordcloud,
    however since this repeats some of the top words, it decreases space for other top words. 

    The default title of the plot being generated is "Word Cloud of Corpus", however this can be changed by inputting a string as a second variable
    while calling the function.

    """
    from wordcloud import WordCloud
    from wordcloud import *
    
    # Instantiating the wordcloud with the relevant settings such as maximum words, background color 
    word_cloud = WordCloud(background_color='white',
        stopwords=set(stopwords.words('english')),
        max_words=150,
        max_font_size=30,
        scale=3,
        random_state=13, collocations=False)

    # Generating the wordcoud and assigning it to the 'wordcloud' variable
    word_cloud=word_cloud.generate(str(corpus))

    #Instantiating the figure to plot the wordcloud
    fig = plt.figure(1, figsize=(12, 12))
    plt.axis('off')

    # Using imshow to display the wordcloud
    plt.imshow(word_cloud)
    plt.title(title, size = 25)
    plt.show()