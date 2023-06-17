# Comment Management System Technical Challenge for Grand Circus
# Author: Apoorva Kaushiks

import unittest

class Comment:
    def __init__(self, text, likes, dislikes, is_flagged):
        """
        Initializes a Comment object with given parameters
        """
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        self.is_flagged = is_flagged
    
    def print_info(self):
        """
        Prints the comment information
        """
        print("Comment: {}".format(self.text))
        print("Likes: {}, Dislikes: {}, Is Flagged: {}".format(self.likes, self.dislikes, self.is_flagged))

class Question(Comment):
    def __init__(self, text, likes, dislikes, is_flagged, answer, topic):
        """
        Initializes a Question object that inherits from Comment with given parameters
        """
        self.answer = answer
        self.topic = topic
        super().__init__(text, likes, dislikes, is_flagged) # inherit methods and properties from parent class

    def print_info(self):
        """
        Prints the question and answer in addition to the comment information
        """
        super().print_info() # call parent class method
        print("Topic: {}".format(self.topic))
        print("Answer: {}".format(self.answer))

def print_all(comments):
    """
    Prints all comments and questions
    param: comments - list of Comment and Question objects
    return: None
    """
    for comment_or_question in comments:
        comment_or_question.print_info()
        print()

def print_unflaged(comments):
    """
    Prints all comments and questions that are not flagged
    param: comments - list of Comment and Question objects
    return: None
    """
    for comment_or_question in comments:
        if not comment_or_question.is_flagged:
            comment_or_question.print_info()
            print()

def average_engagement(comments):
    """
    Returns the average number of likes and dislikes per comment
    param: comments - list of Comment and Question objects
    return: average number of likes and dislikes per comment
    """
    if len(comments) == 0:
        return 0
    
    total_engagement = 0
    for comment in comments:
        total_engagement += comment.likes + comment.dislikes
    return total_engagement / len(comments)


def main():
    """
    Main function to demo the Comment and Question classes
    """
    comments = []
    comments.append(Comment("pineapple on pizza", 10, 10, True))
    comments.append(Comment("I liked this video", 30, 20, False))
    comments.append(Comment("LOL", 4, 1, False))

    comments.append(Question("Should I dislike Shrek?", 1, 15, True, "No you shouldn't", "Blasphemy"))
    comments.append(Question("Why did the programmer quit their job?", 12, 12, False, "They didn't get arrays", "Coding"))

    print("** ALL COMMENTS & QUESTIONS **")
    print_all(comments)

    print("** UNFLAGGED COMMENTTS & QUESTIONS **")
    print_unflaged(comments)
    
    print("AVERAGE ENGAGEMENT:", average_engagement(comments), "likes and dislikes per comment")


class TestAverageEngagement(unittest.TestCase):
    """
    Unit tests for average_engagement function
    """
    def test_empty(self):
        self.assertEqual(average_engagement([]), 0)

    def test_sample(self):
        comments = []
        comments.append(Comment("pineapple on pizza", 10, 10, True))
        comments.append(Comment("I liked this video", 30, 20, False))
        comments.append(Comment("LOL", 4, 1, False))

        comments.append(Question("Should I dislike Shrek?", 1, 15, True, "No you shouldn't", "Blasphemy"))
        comments.append(Question("Why did the programmer quit their job?", 12, 12, False, "They didn't get arrays", "Coding"))

        self.assertEqual(average_engagement(comments), 23.0)

if __name__ == "__main__":
    main()
    unittest.main()





