class Invoice:
    """ Represents an invoice for multiple bookings. """

    def __init__(self, invoice_number, guest):
        self.__invoice_number = invoice_number  # Store invoice number
        self.__guest = guest  # Store guest reference
        self.__bookings = []  # List to store bookings included in invoice

    def add_booking(self, booking):
        self.__bookings.append(booking)  # Append booking to the list

    def get_total_invoice_amount(self):
        return sum(booking.get_total_amount() for booking in self.__bookings)  # Sum booking amounts

    def __str__(self): #Returns a string representation of the invoice
        return f"Invoice {self.__invoice_number}: {self.__guest} - Total: {self.get_total_invoice_amount()} AED"
