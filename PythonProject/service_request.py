class ServiceRequest:
    """ Represents a request for hotel services (e.g., room cleaning, food delivery). """

    def __init__(self, guest, service_type, status="Pending"):
        self.__guest = guest  # Store guest reference
        self.__service_type = service_type  # Store service type
        self.__status = status  # Store request status

    def update_status(self, new_status):
        self.__status = new_status  # Change status to new value

    def __str__(self): #Returns a string representation of the service request
        return f"Service Request: {self.__service_type} for {self.__guest} - Status: {self.__status}"
