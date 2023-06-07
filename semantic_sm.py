import spacy

nlp = spacy.load('en_core_web_sm')

# Perform semantic similarity
cat = nlp('cat')
monkey = nlp('monkey')
banana = nlp('banana')

similarity_cat_monkey = cat.similarity(monkey)
similarity_cat_banana = cat.similarity(banana)
similarity_monkey_banana= monkey.similarity(banana)


print(f'Similarity between cat and monkey: {similarity_cat_monkey}')
print(f'Similarity between cat and banana: {similarity_cat_banana}')
print(f'Similarity between monkey and banana: {similarity_monkey_banana}')

#simpler language model 'en_core_web_sm', you may notice a difference in the quality and depth of the semantic analysis.
# The 'en_core_web_sm' model is a smaller and simpler version of the spaCy language model, 
# which means it has fewer features and a smaller vocabulary compared to 'en_core_web_md'. 
# As a result, it may not perform as well in capturing the nuanced relationships between words 
# and understanding the context in a sentence. The similarity scores and the accuracy of finding similar words might be 
# slightly lower compared to the larger model. 