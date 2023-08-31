# Data-Structures-and-Algorithms.

Welcome to the Code Functions and Testing project! This repository contains Python implementations of three functions for various data manipulation tasks.

## Functions

1. is_balanced

This function checks if a given expression with parentheses, curly braces, and square brackets is balanced.

Example usage:

```python
expression1 = "([]{})"
expression2 = "([)]"
print(is_balanced(expression1))  
print(is_balanced(expression2))  


2. remove_duplicates

This function removes duplicate elements from a sequence (list or tuple) while preserving their original order.

Example usage:
input_sequence = [2, 3, 2, 4, 5, 3, 6, 7, 5]
result = remove_duplicates(input_sequence)
print(result)  

3. word_frequency

This function calculates the frequency of words in a sentence while ignoring punctuation and being case-insensitive.

Example usage:
sentence = "This is a test sentence. This sentence is a test."
result = word_frequency(sentence)
print(result)

## Getting Started
Clone this repository to your local machine.

Ensure you have Python installed.
            `pipenv install`
            `pipenv shell`

Open a terminal or command prompt and navigate to the project directory.
          

Run the following command to execute the test script:

              `python main.py`



## Contributions

Contributions are welcome! If you find issues or want to enhance the functions, feel free to open a pull request.

# License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.cd lib