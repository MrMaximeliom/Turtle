import math
import string
import sys


translation_table = str.maketrans(string.punctuation+string.ascii_uppercase,
                                     " "*len(string.punctuation)+string.ascii_lowercase)


# counts frequency of each word
# returns a dictionary which maps
# the words to  their frequency.
def count_frequency(word_list):
    D = {}

    for new_word in word_list:

        if new_word in D:
            D[new_word] = D[new_word] + 1

        else:
            D[new_word] = 1

    return D


# returns dictionary of (word, frequency)
# pairs from the previous dictionary.
def word_frequencies_for_answer(answer):
    text = answer.translate(translation_table)
    word_list = text.split()
    freq_mapping = count_frequency(word_list)
    print(len(word_list), "words, ", )
    print(len(freq_mapping), "distinct words")

    return freq_mapping


# returns the dot product of two documents
def dotProduct(D1, D2):
    Sum = 0.0

    for key in D1:

        if key in D2:
            Sum += (D1[key] * D2[key])

    return Sum


# returns the angle in radians
# between document vectors
def vector_angle(D1, D2):
    numerator = dotProduct(D1, D2)
    denominator = math.sqrt(dotProduct(D1, D1) * dotProduct(D2, D2))

    return math.acos(numerator / denominator)


def documentSimilarity(answer_1, answer_2):
    sorted_word_list_1 = word_frequencies_for_answer(answer_1)
    sorted_word_list_2 = word_frequencies_for_answer(answer_2)
    distance = vector_angle(sorted_word_list_1, sorted_word_list_2)

    print("The distance between the documents is: % 0.6f (radians)" % distance)

if __name__ == "__main__":
    student_answer = input("enter student answer:\n")
    optimal_answer = input("enter optimal answer:\n")
    documentSimilarity(student_answer,optimal_answer)