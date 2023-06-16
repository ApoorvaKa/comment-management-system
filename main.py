# Comment Management System Technical Challenge
# Author: Apoorva Kaushik

class Comment:
    def __init__(self, text, likes, dislikes, is_flagged):
        self.text = text
        self.likes = likes
        self.dislikes = dislikes
        self.is_flagged = is_flagged
    
    def print_info(self):
        print("Comment: {}".format(self.text))
        print("Likes: {}, Dislikes: {}, Is Flagged: {}".format(self.likes, self.dislikes, self.is_flagged))

class Question(Comment):
    def __init__(self, text, likes, dislikes, is_flagged, answer, topic):
        self.answer = answer
        self.topic = topic
        super().__init__(text, likes, dislikes, is_flagged) # inherit methods and properties from parent class

    def print_info(self):
        print("Comment: {}".format(self.text))
        print("Likes: {}, Dislikes: {}, Is Flagged: {}".format(self.likes, self.dislikes, self.is_flagged))
        print("Topic: {}".format(self.topic))
        print("Answer: {}".format(self.answer))

def print_all(comments):
    for comment_or_question in comments:
        comment_or_question.print_info()
        print()

def print_unflaged(comments):
    for comment_or_question in comments:
        if not comment_or_question.is_flagged:
            comment_or_question.print_info()
            print()

def average_engagement(comments):
    total_engagement = 0
    for comment in comments:
        total_engagement += comment.likes + comment.dislikes
    return total_engagement / len(comments)


def main():
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

main()







