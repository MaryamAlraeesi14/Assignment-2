class Room:
    """ Represents a hotel room. """

    def __init__(self, room_number, room_type, price_per_night):
        self.__room_number = room_number  # Store room number
        self.__room_type = room_type  # Store room type
        self.__price_per_night = price_per_night  # Store price per night
        self.__bookings = []  # List to store bookings related to this room (Aggregation)

    def add_booking(self, booking):
        self.__bookings.append(booking)  # Append the booking to the list

    def get_price_per_night(self):
        return self.__price_per_night  # Return price per night

    def __str__(self): #Returns a string representation of the room.
        return f"Room {self.__room_number} ({self.__room_type}) - {self.__price_per_night} AED/night"
