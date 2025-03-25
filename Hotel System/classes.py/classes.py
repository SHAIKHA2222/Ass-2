from datetime import date

# =============================
# Class: Hotel
# Association: Composition with Room, Aggregation with Guest
# =============================
class Hotel:
    """Represents a hotel that owns rooms and hosts guests."""

    def __init__(self, name: str, location: str, hotel_rating: float, contact_number: str):
        self.__name = name  # Hotel name
        self.__location = location  # Hotel location
        self.__hotel_rating = hotel_rating  # Hotel rating
        self.__contact_number = contact_number  # Hotel contact number
        self.__rooms = []  # Composition: list of Room objects

    def add_room(self, room):  # Adds a room to the hotel
        self.__rooms.append(room)

    def get_available_rooms(self):  # Returns list of available rooms
        return [room for room in self.__rooms if room.is_available()]

    def get_name(self):  # Returns the name of the hotel
        return self.__name

# =============================
# Class: Room
# Composition with Hotel
# =============================
class Room:
    """Represents a hotel room with details like type, price, and availability."""

    def __init__(self, room_number: int, room_type: str, price_per_night: float, amenities: list):
        self.__room_number = room_number  # Room number
        self.__room_type = room_type  # Type (Single, Double, etc.)
        self.__price_per_night = price_per_night  # Nightly price
        self.__availability_status = True  # Available by default
        self.__amenities = amenities  # List of amenities

    def book_room(self):  # Book the room if it's available
        if self.__availability_status:
            self.__availability_status = False
            return True
        return False

    def check_out(self):  # Make the room available again
        self.__availability_status = True

    def is_available(self):  # Return True if available
        return self.__availability_status

    def get_room_type(self):  # Return room type
        return self.__room_type

    def get_price(self):  # Return room price
        return self.__price_per_night

# =============================
# Class: Guest
# Aggregation with Hotel and Booking
# =============================
class Guest:
    """Represents a guest who can book rooms and provide feedback."""

    def __init__(self, guest_id: int, name: str, email: str, nationality: str):
        self.__guest_id = guest_id  # Guest ID
        self.__name = name  # Guest name
        self.__email = email  # Guest email
        self.__nationality = nationality  # Guest nationality
        self.__loyalty_points = 0  # Loyalty points
        self.__bookings = []  # Aggregation: guest can have multiple bookings

    def create_account(self):  # Simulate account creation
        print(f"Account created for {self.__name}")

    def add_booking(self, booking):  # Add booking to guest history
        self.__bookings.append(booking)

    def view_reservation_history(self):  # View past bookings
        print(f"Reservation history for {self.__name}:")
        for b in self.__bookings:
            print(f"Booking {b.get_id()} - {b.get_status()}")

    def get_name(self):  # Get guest name
        return self.__name

    def get_loyalty_points(self):  # Get guest points
        return self.__loyalty_points

# =============================
# Class: PremiumGuest
# Inherits from Guest
# =============================
class PremiumGuest(Guest):
    """Premium guest with membership and rewards."""

    def __init__(self, guest_id: int, name: str, email: str, nationality: str):
        super().__init__(guest_id, name, email, nationality)
        self.__membership = "Silver"  # Membership level
        self.__reward_points = 0  # Reward points

    def upgrade_membership(self):  # Upgrade membership level
        self.__membership = "Gold"

# =============================
# Class: Booking
# Aggregation with Guest
# Unary with Feedback
# Binary with Payment
# =============================
class Booking:
    """Represents a booking with optional feedback and payments."""

    def __init__(self, booking_id: int, guest, room, check_in, check_out):
        self.__booking_id = booking_id  # Booking ID
        self.__guest = guest  # Guest object (Aggregation)
        self.__room = room  # Room object
        self.__check_in = check_in  # Check-in date
        self.__check_out = check_out  # Check-out date
        self.__status = "Pending"  # Booking status
        self.__feedback = None  # Unary association with Feedback
        self.__payments = []  # Binary association with Payment

    def confirm_booking(self):  # Try to book the room
        if self.__room.book_room():
            self.__status = "Confirmed"
            return True
        return False

    def cancel_booking(self):  # Cancel booking
        self.__status = "Cancelled"
        self.__room.check_out()

    def add_feedback(self, feedback):  # Add feedback to booking
        self.__feedback = feedback

    def add_payment(self, payment):  # Add payment to booking
        self.__payments.append(payment)

    def get_status(self):  # Get booking status
        return self.__status

    def get_id(self):  # Get booking ID
        return self.__booking_id

# =============================
# Class: Payment
# Binary Association with Booking (1 booking → many payments)
# =============================
class Payment:
    """Handles a payment made for a booking."""

    def __init__(self, payment_id: int, method: str, amount: float):
        self.__payment_id = payment_id  # Payment ID
        self.__method = method  # Payment method
        self.__amount = amount  # Payment amount
        self.__is_successful = False  # Payment status

    def process(self):  # Mark payment as successful
        self.__is_successful = True if self.__amount > 0 else False

    def generate_invoice(self):  # Return invoice string
        return f"Payment ID: {self.__payment_id} | Amount: ${self.__amount}"

# =============================
# Class: Feedback
# Unary Association with Booking
# =============================
class Feedback:
    """Stores guest feedback after a booking."""

    def __init__(self, feedback_id: int, rating: int, comments: str, guest_name: str):
        self.__feedback_id = feedback_id  # Feedback ID
        self.__rating = rating  # Rating (1–5)
        self.__comments = comments  # Comment text
        self.__guest_name = guest_name  # Guest who submitted

    def submit(self):  # Print feedback to console
        print(f"Feedback from {self.__guest_name}: {self.__comments} (Rating: {self.__rating})")



