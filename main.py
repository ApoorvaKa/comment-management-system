# Comment Management System Technical Challenge
# Author: Apoorva Kaushik

class Comment:
    def __init__(self, text, likes, dislikes, is_flagged):
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        self.is_flagged = is_flagged
    
    def print_info(self):
        print("Text: " + self.text)
        print("Likes: " + str(self.likes))
        print("Dislikes: " + str(self.dislikes))
        print("Is Flagged: " + str(self.is_flagged))

class Question(Comment):
    def __init__(self, text, likes, dislikes, is_flagged, answer, topic):
        self.answer = answer
        self.topic = topic
        super().__init__(text, likes, dislikes, is_flagged) # inherit methods and properties from parent class

    def print_info(self):
        print("Text: " + self.text)
        print("Likes: " + str(self.likes))
        print("Dislikes: " + str(self.dislikes))
        print("Is Flagged: " + str(self.is_flagged))
        print("Answer: " + self.answer)
        print("Topic: " + self.topic)

def print_all(comments_and_questions):
    for comment_or_question in comments_and_questions:
        comment_or_question.print_info()

def print_unflaged(comments_and_questions):
    for comment_or_question in comments_and_questions:
        if not comment_or_question.is_flagged:
            comment_or_question.print_info()

def average_engagement(comment):
    return (comment.likes + comment.dislikes) / 2


def main():
    comments = []
    comments.append(Comment("pineapple on pizza", 10, 10, True))
    comments.append(Comment("I liked this video", 30, 20, False))
    comments.append(Comment("LOL", 4, 1, False))

    comments.append(Question("Should I dislike Shrek?", 1, 15, True, "No you shouldn't", "Blasphemy"))
    comments.append(Question("Why did the programmer quit their job?", 12, 12, False, "They didn't get arrays", "Coding"))

    print("All comments and questions:")
    print_all(comments)





