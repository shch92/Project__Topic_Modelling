# Defining the function that will automatically plot the LDA model
def plot_lda_vis(lda_model, bow_corpus, dic):
    """
    The function accepts the LDA model, bag of words corpus and a dictionary formed by the LDA model corpus to generate a visualization fo the LDA model
    
    """
    
    pyLDAvis.enable_notebook()
    vis = gensimvis.prepare(lda_model, bow_corpus, dic)
    return vis