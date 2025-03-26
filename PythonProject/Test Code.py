#This just to check that the submitted code error-free and have well-formatted output

from room import Room
from guest import Guest
from booking import Booking
from payment import Payment
from invoice import Invoice
from feedback import Feedback
from service_request import ServiceRequest
from loyalty import LoyaltyProgram


# Create guests
guest1 = Guest("Maryam", "0501234567")
guest2 = Guest("Mohammed", "0551234567")

# Create rooms
room1 = Room(100, "Single", 150)
room2 = Room(101, "Double", 100)

# Make bookings
booking1 = Booking(guest1, room1, 3)  # 3-night stay in Deluxe Room
booking2 = Booking(guest2, room2, 2)  # 2-night stay in Suite Room

# Process payments
booking1.make_payment(900, "Credit Card")
booking2.make_payment(1000, "Cash")

# Create an invoice
invoice1 = Invoice("INV-001", guest1)
invoice1.add_booking(booking1)

# Guest leaves feedback
feedback1 = Feedback(guest1, 5, "Amazing experience!")
feedback2 = Feedback(guest2, 4, "Great service but room was small.")

# Service request (room cleaning)
service1 = ServiceRequest(guest1, "Room Cleaning")
service1.update_status("Completed")

# Loyalty program
loyalty = LoyaltyProgram()
loyalty.add_points(guest1, 100)  # Add 100 points to guest1
loyalty.add_points(guest2, 50)  # Add 50 points to guest2

# Print details
print(guest1)
print(guest2)
print(room1)
print(room2)
print(booking1)
print(booking2)
print(invoice1)
print(feedback1)
print(feedback2)
print(service1)
print(f"Loyalty Points for {guest1}: {loyalty.get_points(guest1)}")
print(f"Loyalty Points for {guest2}: {loyalty.get_points(guest2)}")
