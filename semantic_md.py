import spacy

nlp = spacy.load('en_core_web_md')

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

#After running the code, you will find that the similarity between cat and monkey is relatively higher 
# than the similarity between cat and banana. This observation is interesting because it aligns with the 
# fact that cat and monkey are both mammals, while a banana is a fruit. As a result, 
# there may be more shared semantic characteristics between cat and monkey, such as their shared classification as animals.
#monkey and banana have a higher similarity than cat and
#banana. So we can assume that the model already puts together that
#monkeys eat bananas and that is why there is a significant similarity