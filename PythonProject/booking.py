from room import Room
from guest import Guest
from payment import Payment

class Booking:
    """ Represents a booking made by a guest. """

    def __init__(self, guest, room, num_nights):
        self.__guest = guest  # Store guest reference
        self.__room = room  # Store room reference
        self.__num_nights = num_nights  # Store number of nights
        self.__payment = None  # Store payment object (Aggregation)
        self.__total_amount = num_nights * room.get_price_per_night()  # Calculate total amount

        guest.add_booking(self)  # Add booking reference to guest
        room.add_booking(self)  # Add booking reference to room

    def make_payment(self, amount, method):
        self.__payment = Payment(amount, method, self)  # Create a payment object

    def get_total_amount(self):
        return self.__total_amount  # Return total amount

    def __str__(self): #Returns a string representation of the booking.
        return f"Booking: {self.__guest} - {self.__room} for {self.__num_nights} nights"
