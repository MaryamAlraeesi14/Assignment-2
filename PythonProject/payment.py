class Payment:
    """ Represents a payment transaction. """

    def __init__(self, amount, method, booking):
        self.__amount = amount  # Store amount
        self.__method = method  # Store payment method
        self.__booking = booking  # Store booking reference

    def __str__(self): #Returns a string representation of the payment
        return f"Payment: {self.__amount} AED via {self.__method}"
