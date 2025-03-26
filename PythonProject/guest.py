class Guest:
    """ Represents a hotel guest. """

    def __init__(self, name, contact):
        self.__name = name  # Store guest name
        self.__contact = contact  # Store guest contact information
        self.__bookings = []  # List to store booking references (Aggregation)
        self.__feedbacks = []  # List to store feedback (Aggregation)

    def add_booking(self, booking):
        self.__bookings.append(booking)  # Append the booking to the list

    def add_feedback(self, feedback):
        self.__feedbacks.append(feedback)  # Append feedback to the list

    def __str__(self): #Returns a string representation of the guest
        return f"Guest: {self.__name}, Contact: {self.__contact}"
