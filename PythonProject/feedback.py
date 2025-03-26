class Feedback:
    """ Represents feedback given by a guest. """

    def __init__(self, guest, rating, comment):
        self.__guest = guest  # Store guest reference
        self.__rating = rating  # Store rating
        self.__comment = comment  # Store comment
        guest.add_feedback(self)  # Link feedback to guest

    def __str__(self): #Returns a string representation of the feedback
        return f"Feedback from {self.__guest}: Rating {self.__rating}/5 - {self.__comment}"
