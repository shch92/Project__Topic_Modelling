# Compute Coherence Score
def compute_coherence_score(lda_model_name, text_name, dictionary_name):
    """
    The function takes:
     - lda_model
     - corpus for generating the lda model
     - dictionary used to generate the lda model 
    
    It then instantiates the CoherenceModel using this information and uses the get_coherence method to get the coherence score. 
    
    """
    # Instantiate the Coherence model using lda model, corpus and dictionary name
    coherence_model_lda = CoherenceModel(model=lda_model_name, texts=text_name, dictionary=dictionary_name, coherence='c_v')
    
    # Use the relevant method to get the coherence score
    coherence_lda = coherence_model_lda.get_coherence()
    
    # Return the coherence score
    return coherence_lda