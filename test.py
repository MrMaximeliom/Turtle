import uuid
import random
import string
def get_random_string(length):
    numbers = 1234567890
    letters = string.ascii_lowercase
    number_and_letters = str(numbers)+letters
    result_str = ''.join(random.choice(number_and_letters) for i in range(length))
    print("Random string of length", length, "is:", result_str)

if __name__ == "__main__":
    # Printing random id using uuid1()
    # print("The random id using uuid1() is : ", end="")
    # print(uuid.uuid4())
    get_random_string(8)
    get_random_string(16)
