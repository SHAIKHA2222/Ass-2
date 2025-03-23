from datetime import date
from classes import Guest, Room, Booking, Payment

# Test case 1: Guest Account Creation
def test_guest_account_creation():
    guest1 = Guest(1, "John Doe", "john@example.com", 100, "john.doe@email.com", "USA")
    guest1.createAccount()  # Testing account creation for John Doe
    guest1.setEmail("new.john@example.com")  # Changing email as part of profile update
    print(f"Updated Email: {guest1.getEmail()}")  # Verifying if email is updated

    guest2 = Guest(2, "Jane Smith", "jane@example.com", 200, "jane.smith@email.com", "UK")
    guest2.createAccount()  # Testing account creation for Jane Smith

# Test case 2: Searching for Available Rooms
def test_search_available_rooms():
    room1 = Room(101, "Single", 120, True, ["Wi-Fi", "TV"], 2, 1)
    room2 = Room(102, "Double", 180, False, ["Wi-Fi", "TV", "Mini-Bar"], 4, 1)

    rooms = [room1, room2]
    available_rooms = [room for room in rooms if room.isAvailable()]
    
    print(f"Available Rooms: {[room.getRoomType() for room in available_rooms]}")  # Verifying available rooms

# Test case 3: Making a Room Reservation
def test_room_reservation():
    guest = Guest(1, "Emily Johnson", "emily@example.com", 500, "emily.j@example.com", "Canada")
    room = Room(103, "Suite", 250, True, ["Wi-Fi", "Mini-Bar", "Gym"], 3, 2)
    booking = Booking(1, guest, room, date(2025, 3, 10), date(2025, 3, 15), "Pending")
    
    booking.confirmBooking()  # Confirming the booking
    print(f"Booking Status: {booking.__dict__['__status']}")  # Verifying booking status

# Test case 4: Booking Confirmation Notification
def test_booking_confirmation_notification():
    guest = Guest(2, "Michael Brown", "michael@example.com", 200, "michael.b@email.com", "Germany")
    room = Room(104, "Single", 150, True, ["Wi-Fi"], 1, 2)
    booking = Booking(2, guest, room, date(2025, 3, 12), date(2025, 3, 14), "Pending")
    booking.confirmBooking()  # Confirming the booking
    print(f"Booking Status: {booking.__dict__['__status']}")  # Verifying confirmation

# Test case 5: Processing Payment
def test_payment_processing():
    payment = Payment(1, "Credit Card", 250, date.today(), False)
    payment.processPayment()  # Processing the payment
    print(f"Payment Success: {payment.__dict__['__is_successful']}")  # Verifying payment status

# Run test cases
test_guest_account_creation()
test_search_available_rooms()
test_room_reservation()
test_booking_confirmation_notification()
test_payment_processing()

