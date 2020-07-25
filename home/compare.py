import gensim
import numpy as np
from nltk.tokenize import word_tokenize , sent_tokenize
from Turtle import settings
import os

def compareTexts(studentAnswer,optimalAnswer):
    student_answer_sentences = sent_tokenize(studentAnswer)
    optimal_answer_sentences = sent_tokenize(optimalAnswer)
    # for word in studentAnswer:
    #     tokens = sent_tokenize(word)
    #     for line in tokens:
    #         student_answer_sentences.append(line)
    # for word in optimalAnswer:
    #     tokens = sent_tokenize(word)
    #     for line in tokens:
    #         optimal_answer_sentences.append(line)

    # print("Number of documents:", len(student_answer_sentences))


    # # making texts lower cased
    lowered_student_answer = [[w.lower() for w in word_tokenize(text)] for text in student_answer_sentences]
    lowered_optimal_answer = [[w.lower() for w in word_tokenize(text)] for text in optimal_answer_sentences]
    # print(lowered_student_answer)
    #
    # # create a dictionary for answers
    dictionary = gensim.corpora.Dictionary(lowered_student_answer)
    # print(dictionary.token2id)
    #
    # #creating courps

    corpus = [dictionary.doc2bow(gen_doc) for gen_doc in lowered_student_answer]
    # print(corpus)
    # Mars is a cold desert world. It is half the size of Earth.
    #
    tf_idf = gensim.models.TfidfModel(corpus)
    # for doc in tf_idf[corpus]:
    #     print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])
    sims = gensim.similarities.Similarity(os.path.join(settings.BASE_DIR, 'Compare'), tf_idf[corpus],
                                          num_features=len(dictionary))

    query_doc_bow = [dictionary.doc2bow(gen_doc) for gen_doc in lowered_optimal_answer]
    # perform a similarity query against the corpus
    query_doc_tf_idf = tf_idf[query_doc_bow]
    # print(document_number, document_similarity)
    print('Comparing Result:', sims[query_doc_tf_idf])

if __name__ == "__main__":
    student_answer = input("enter student answer:\n")
    optimal_answer = input("enter optimal answer:\n")
    compareTexts(student_answer,optimal_answer)

# Mars is the fourth planet in our solar system.It is second-smallest planet in the Solar System after Mercury. Saturn is yellow planet.
#
#