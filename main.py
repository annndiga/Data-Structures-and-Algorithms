import string
from stacks import is_balanced
from sequences import remove_duplicates
from dictionaries import word_frequency

def main():
    
    expression1 = "([]{})"
    expression2 = "([)]"
    print(is_balanced(expression1))  
    print(is_balanced(expression2))  
    
    
    input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
    result = remove_duplicates(input_sequence)
    print(result) 
    
    
    sentence = "This is a test sentence. This sentence is a test."
    result = word_frequency(sentence)
    print(result)

if __name__ == "__main__":
    main()