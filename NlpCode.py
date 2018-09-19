
# import library
    import nltk
    nltk.download('wordnet')
    from nltk.corpus import wordnet
    from nltk.stem import PorterStemmer
    from nltk.stem import WordNetLemmatizer
# start function
def fun(word): 
    
    
    syn=wordnet.synsets(word)
    dif=syn[0].definition()
    exam=syn[0].examples()
        
    synonyms=[]
    antonyms=[]
    for syn2 in wordnet.synsets(word):
        for lema in syn2.lemmas():
              if lema.antonyms():
                 antonyms.append(lema.antonyms()[0].name())  
                 synonyms.append(lema.name())
  
    stemmer=PorterStemmer()
    stemmer=stemmer.stem(word)
    
   
    Lemmatizer=WordNetLemmatizer()
    verb=Lemmatizer.lemmatize(word , pos="v")
    non=Lemmatizer.lemmatize(word , pos="n")
    adjectiv=Lemmatizer.lemmatize(word , pos="a")
    r=Lemmatizer.lemmatize(word , pos="r")
    return [dif, exam , synonyms, antonyms,stemmer,verb,non,adjectiv,r]; 
#end function


# calling function
list = fun('small')  
print(list)

