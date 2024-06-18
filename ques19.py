# Python Programming Assignment-1
# 19. Write a python program that removes all punctuation from a given string. 
import string
def remove_punctuation(input_string):
    translator = str.maketrans('', '', string.punctuation)
    no_punctuation_string = input_string.translate(translator)
    return no_punctuation_string
input_string = "Hello, world! This is a test... Are you ready?"
result = remove_punctuation(input_string)
print(result)  
