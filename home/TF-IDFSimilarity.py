from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import linear_kernel
from nltk import word_tokenize
from nltk.stem import WordNetLemmatizer
import nltk
from nltk.corpus import stopwords

# Download stopwords list
#nltk.download('punkt')
stop_words = set(stopwords.words('english'))

# Interface lemma tokenizer from nltk with sklearn
class LemmaTokenizer:
    ignore_tokens = [',', '.', ';', ':', '"', '``', "''", '`']
    def __init__(self):
        self.wnl = WordNetLemmatizer()
    def __call__(self, doc):
        return [self.wnl.lemmatize(t) for t in word_tokenize(doc) if t not in self.ignore_tokens]

def calculateSimilarityUsingTFIDF(search_terms,documents):
    #Lemmatize the stop words
    tokenizer=LemmaTokenizer()
    token_stop = tokenizer(' '.join(stop_words))

    #search_terms = 'red tomato'
    #documents = ['cars drive on the road', 'tomatoes are actually fruit']
    #cars drive on the road, tomatoes are actually fruit.

    # Create TF-idf model
    vectorizer = TfidfVectorizer(stop_words=token_stop,
                              tokenizer=tokenizer)
    #doc_vectors = vectorizer.fit_transform([search_terms] + documents)
    doc_vectors = vectorizer.fit_transform([search_terms] + documents)

    # Calculate similarity
    cosine_similarities = linear_kernel(doc_vectors[0:1], doc_vectors).flatten()
    document_scores = [item.item() for item in cosine_similarities[1:]]
    print(document_scores)
    # [0.0, 0.287]
if __name__ == "__main__":
    teacher_answer = input("enter optimal answer:")
    num = int(input("Enter number of answers: "))
    student_answers = []
    for _ in range(num):
        student_answer = input("Enter answer: ")
        student_answers.append(student_answer)

    calculateSimilarityUsingTFIDF(teacher_answer,student_answers)

"""
dev:
[0.11641413 0.10281226 0.56890744]
mine:
[0.085376984254077, 0.085376984254077, 0.3818316938440054]

"""