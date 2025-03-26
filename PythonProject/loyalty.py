class LoyaltyProgram:
    """ Represents a loyalty program for frequent guests. """

    def __init__(self):
        self.__guest_points = {}  # Dictionary to store guest points

    def add_points(self, guest, points):
        if guest in self.__guest_points:  # Check if guest already has points
            self.__guest_points[guest] += points  # Add new points
        else:
            self.__guest_points[guest] = points  # Initialize points

    def redeem_points(self, guest, points):
        if guest in self.__guest_points and self.__guest_points[guest] >= points:
            self.__guest_points[guest] -= points  # Deduct points
            return True  # Redemption successful
        return False  # Not enough points

    def get_points(self, guest):
        return self.__guest_points.get(guest, 0)  # Return guest points (default 0)

    def __str__(self): #Returns a string representation of the loyalty program
        return f"Loyalty Program: {self.__guest_points}"
