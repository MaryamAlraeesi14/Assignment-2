# test_hotel_management
from room import Room
from guest import Guest
from booking import Booking
from payment import Payment
from invoice import Invoice
from feedback import Feedback
from service_request import ServiceRequest
from loyalty import LoyaltyProgram


# Test Guest Account Creation
def test_guest_account_creation():
    """Test the process of creating a guest account."""
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    guest = Guest(name, email)
    print("Guest account created successfully!")
    print(guest)
    print("-" * 50)


# Test Room Availability Search
def test_room_availability():
    """Test searching for available rooms."""
    room_type = input("Enter room type (Single/Double): ")
    if room_type == "Single":
        room = Room(101, "Single", 100)
    elif room_type == "Double":
        room = Room(102, "Double", 150)
    else:
        print("Invalid room type entered.")
        return
    print("Available room found:", room)
    print("-" * 50)


# Test Room Reservation
def test_room_reservation():
    """Test making a room reservation."""
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    guest = Guest(name, email)

    room_type = input("Enter room type (Single/Double): ")
    room = Room(101, room_type, 100 if room_type == "Single" else 150)

    nights = int(input("Enter number of nights: "))
    booking = Booking(guest, room, nights)

    print("Room booked successfully!")
    print(booking)
    print("-" * 50)


# Test Booking Confirmation
def test_booking_confirmation():
    """Test booking confirmation notification."""
    print("Booking confirmation email sent to the guest.")
    print("-" * 50)


# Test Invoice Generation
def test_invoice_generation():
    """Test generating an invoice."""
    name = input("Enter guest name: ")
    email = input("Enter guest email: ")
    guest = Guest(name, email)

    room_type = input("Enter room type (Single/Double): ")
    room = Room(101, room_type, 100 if room_type == "Single" else 150)

    nights = int(input("Enter number of nights: "))
    booking = Booking(guest, room, nights)

    invoice = Invoice(1, guest)
    invoice.add_booking(booking)

    print("Invoice generated successfully!")
    print(invoice)
    print("-" * 50)


# Test Payment Processing
def test_payment_processing():
    """Test processing different payment methods."""
    amount = float(input("Enter payment amount: "))
    method = input("Enter payment method (Credit Card/Other): ")
    payment = Payment(amount, method, None)

    print("Payment processed successfully!")
    print(payment)
    print("-" * 50)


# Test Reservation History
def test_reservation_history():
    """Test displaying reservation history."""
    print("Displaying reservation history...")
    print("-" * 50)


# Test Reservation Cancellation
def test_reservation_cancellation():
    """Test canceling a reservation."""
    print("Reservation canceled successfully!")
    print("-" * 50)


# Test Guest Feedback Submission
def test_guest_feedback():
    """Test submitting guest feedback."""
    guest_name = input("Enter your name: ")
    guest_contact = input("Enter your contact information: ")

    # Create a Guest object
    guest = Guest(guest_name, guest_contact)

    feedback_text = input("Enter your feedback: ")
    rating = int(input("Enter your rating (1-5): "))

    # Create a Feedback object with the Guest instance
    feedback = Feedback(guest, rating, feedback_text)

    print("\nFeedback submitted successfully!")
    print(feedback)
    print("-" * 50)




# Test Service Request
def test_service_request():
    """Test making a service request."""
    guest_name = input("Enter your name: ")
    service_type = input("Enter service request (Cleaning, Towels, etc.): ")
    request = ServiceRequest(guest_name, service_type)
    print("Service request submitted successfully!")
    print(request)
    print("-" * 50)


# Test Loyalty Program
def test_loyalty_program():
    """Test adding and redeeming loyalty points."""
    guest_name = input("Enter your name: ")
    guest_contact = input("Enter your contact information: ")

    # Create a Guest object
    guest = Guest(guest_name, guest_contact)

    # Create a LoyaltyProgram instance (no guest argument needed)
    loyalty = LoyaltyProgram()

    # Add points to the guest
    points_to_add = int(input("Enter loyalty points to add: "))
    loyalty.add_points(guest, points_to_add)

    print(f"\nLoyalty points updated for {guest_name}. Current points: {loyalty.get_points(guest)}")

    # Redeem points
    points_to_redeem = int(input("Enter loyalty points to redeem: "))
    if loyalty.redeem_points(guest, points_to_redeem):
        print(f"Redeemed {points_to_redeem} points successfully.")
    else:
        print(f"Not enough points to redeem {points_to_redeem}. Current balance: {loyalty.get_points(guest)}")

    print("\nLoyalty Program Details:")
    print(loyalty)
    print("-" * 50)



# Main menu for testing
def main():
    while True:
        print("\nHotel Management System - Test Menu")
        print("1. Guest Account Creation")
        print("2. Room Availability Search")
        print("3. Room Reservation")
        print("4. Booking Confirmation")
        print("5. Invoice Generation")
        print("6. Payment Processing")
        print("7. Reservation History")
        print("8. Reservation Cancellation")
        print("9. Guest Feedback")
        print("10. Service Request")
        print("11. Loyalty Program")
        print("12. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            test_guest_account_creation()
        elif choice == "2":
            test_room_availability()
        elif choice == "3":
            test_room_reservation()
        elif choice == "4":
            test_booking_confirmation()
        elif choice == "5":
            test_invoice_generation()
        elif choice == "6":
            test_payment_processing()
        elif choice == "7":
            test_reservation_history()
        elif choice == "8":
            test_reservation_cancellation()
        elif choice == "9":
            test_guest_feedback()
        elif choice == "10":
            test_service_request()
        elif choice == "11":
            test_loyalty_program()
        elif choice == "12":
            print("Exiting test script. Goodbye!")
            break
        else:
            print("Invalid choice, please try again.")


# Run the test script
if __name__ == "__main__":
    main()
