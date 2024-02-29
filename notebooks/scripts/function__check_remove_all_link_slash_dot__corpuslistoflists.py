# This first function is used for removing the relevant elements from the list which represent hyperlinks, dots and ampersand (&amp)

def removal_link_slash_dot(corpus):
    
    """
    The function takes a list of lists as a corpus. 
    It looks for elements that start with lettters or symbols that are specific to links ampersands and dots in our corpus and uses the 
    pop method to remove them.
    
    """
    
    # Instantiating a for loop that runs through our corpus list and enumerates each separate Tweet as a sentence
    for ind, sentence in enumerate(corpus):
        
        # Instantiating a for loop that goes through the sentence list and enumerates every word in the sentence as a separate element
        for ind2,word in enumerate(sentence):
            
            # Putting conditions for using pop on an element
            if word.startswith('ht'):
                corpus[ind].pop(ind2)
            elif word.startswith(' ht'):
                corpus[ind].pop(ind2)
            elif word.startswith('  ht'):
                corpus[ind].pop(ind2)
            elif word.startswith(' /'):
                 corpus[ind].pop(ind2)
            elif word.startswith('/'):
                 corpus[ind].pop(ind2)
            elif word.startswith('  /'):
                 corpus[ind].pop(ind2)
            elif word.startswith('amp'):
                 corpus[ind].pop(ind2)
            elif word.startswith(' amp'):
                 corpus[ind].pop(ind2)
            elif word.startswith('..'):
                 corpus[ind].pop(ind2)
            elif word.startswith(' ..'):
                 corpus[ind].pop(ind2)

                    
# This second function is used for checking the Tweets for any remaining hyperlinks, dots and ampersand (&amp) in the corpus and 
# running the first function if there are any present 

def check_remove_all_link_slash_dot(corpus):
    """
    The function takes a list of lists as a corpus. 
    It looks for elements that start with lettters or symbols that are specific to links, ampersands and dots in our corpus and if any are present then
    calls the "removal_link_slash_dot" function to remove them.
    
    """
    
     # Instantiating a for loop that runs through our corpus list and enumerates each seperate Tweet as a sentence
    for ind, sentence in enumerate(corpus):
        
         # Instantiating a for loop that goes through the sentence list and enumerates every word in the sentence as a separate element
        for ind2,word in enumerate(sentence):
            
            # Generating an empty list that will be appended by any element that represents links, ampercents and dots
            should_be_empty = []
            
             # Putting conditions for appending the 'should_be_empty' based on elements that represent links, ampercents and dots
            if word.startswith('ht'):
                should_be_empty.append(word)
            elif word.startswith(' ht'):
                should_be_empty.append(word)
            elif word.startswith('  ht'):
                should_be_empty.append(word)
            elif word.startswith(' /'):
                 should_be_empty.append(word)
            elif word.startswith('/'):
                 should_be_empty.append(word)
            elif word.startswith('  /'):
                 should_be_empty.append(word)
            elif word.startswith('amp'):
                 should_be_empty.append(word)
            elif word.startswith(' amp'):
                 should_be_empty.append(iword)
            elif word.startswith('..'):
                 should_be_empty.append(word)
            elif word.startswith(' ..'):
                 should_be_empty.append(word)
            
            # Setting the while condition to run the "removal_link_slash_dot" function if the 'should_be_empty' list has elements in it
            while len(should_be_empty) > 0:        
                removal_link_slash_dot(corpus)
                
                #After running the "removal_link_slash_dot" function, the 'should_be_empty' list should be emptied in order to 
                # check the corpus (and append) again
                del should_be_empty[:]
                
                # Re-run the current function to check the corpus again for links, ampercents and dots
                check_remove_all_link_slash_dot(corpus)           