# Comment Management System

This is a simple Comment Management System implemented in Python. It includes two classes, `Comment` and `Question`, that allow you to create and manage comments and questions. The system also provides functions to print comments, filter flagged comments, and calculate the average engagement.

## Classes

### Comment

The `Comment` class represents a basic comment and has the following attributes:

- `text`: The text of the comment.
- `likes`: The number of likes the comment has received.
- `dislikes`: The number of dislikes the comment has received.
- `is_flagged`: A boolean value indicating whether the comment has been flagged.

The class provides a method `print_info()` to print the comment's information.

### Question

The `Question` class inherits from the `Comment` class and adds two additional attributes:

- `answer`: The answer to the question.
- `topic`: The topic of the question.

The class overrides the `print_info()` method to include the question's answer and topic in the printed information.

## Functions

The system includes three functions:

### `print_all(comments)`

This function takes a list of `Comment` and `Question` objects as input and prints the information for each comment or question in the list.

### `print_unflagged(comments)`

This function takes a list of `Comment` and `Question` objects as input and prints the information for each comment or question that is not flagged.

### `average_engagement(comments)`

This function takes a list of `Comment` and `Question` objects as input and calculates the average number of likes and dislikes per comment. It returns the calculated average.

## Usage

To use the Comment Management System, you can create instances of the `Comment` and `Question` classes with the desired attributes. Then, you can use the provided functions to perform operations on the comments and questions.

In the provided example code, some comments and questions are created, and the system is demonstrated by printing all comments and questions, printing only the unflagged comments and questions, and calculating the average engagement.

## Unit Tests

The system also includes unit tests for the `average_engagement()` function. The tests cover an empty list case and a sample case with a list of comments and questions. The expected average engagement values are asserted against the calculated values.


**Both the demo code and the unit tests will run when the file is executed.**