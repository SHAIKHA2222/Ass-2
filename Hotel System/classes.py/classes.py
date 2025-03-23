# Importing necessary libraries for handling dates
from datetime import date

# Class: Hotel
# Describes a hotel with multiple rooms, and provides functions to manage room listings and hotel details
class Hotel:
    """Represents a hotel with rooms and basic information."""
    
    def __init__(self, name, location, number_of_rooms, hotel_rating, contact_number):
        self.__name = name  # Hotel name
        self.__location = location  # Location of the hotel
        self.__number_of_rooms = number_of_rooms  # Total number of rooms in the hotel
        self.__hotel_rating = hotel_rating  # Rating of the hotel
        self.__contact_number = contact_number  # Contact information of the hotel
        self.__rooms = []  # List to store room objects
    
    def addRoom(self, room):
        """Adds a room to the hotel."""
        self.__rooms.append(room)  # Adds a room to the list of rooms
    
    def removeRoom(self, room):
        """Removes a room from the hotel."""
        if room in self.__rooms:
            self.__rooms.remove(room)  # Removes the specified room from the list
    
    def updateHotelRating(self, new_rating):
        """Updates the hotel's rating."""
        self.__hotel_rating = new_rating  # Sets a new rating for the hotel
    
    def getContactNumber(self):
        """Returns the contact number of the hotel."""
        return self.__contact_number  # Returns the contact number
    
    def setContactNumber(self, contact):
        """Sets a new contact number for the hotel."""
        self.__contact_number = contact  # Updates the contact number
    
    def getNumberOfRooms(self):
        """Returns the number of rooms in the hotel."""
        return len(self.__rooms)  # Returns the total count of rooms
    
    def setNumberOfRooms(self, count):
        """Sets the number of rooms in the hotel."""
        self.__number_of_rooms = count  # Updates the number of rooms

# Class: Room
# Represents an individual room with specific attributes like room type, availability, and price
class Room:
    """Represents a hotel room."""
    
    def __init__(self, room_number, room_type, price_per_night, availability_status, amenities, max_occupancy, floor_number):
        self.__room_number = room_number  # Room number (unique identifier)
        self.__room_type = room_type  # Type of room (e.g., single, double)
        self.__price_per_night = price_per_night  # Price per night for the room
        self.__availability_status = availability_status  # Room availability status (True/False)
        self.__amenities = amenities  # List of amenities available in the room
        self.__max_occupancy = max_occupancy  # Maximum number of people allowed in the room
        self.__floor_number = floor_number  # Floor number where the room is located
    
    def bookRoom(self):
        """Books the room if available."""
        if self.__availability_status:
            self.__availability_status = False  # Marks room as unavailable
            return True  # Room is successfully booked
        return False  # Room is not available
    
    def checkOut(self):
        """Checks out the guest and makes the room available again."""
        self.__availability_status = True  # Marks the room as available for booking
    
    def getRoomType(self):
        """Returns the room type."""
        return self.__room_type  # Returns room type
    
    def setRoomType(self, room_type):
        """Sets the room type."""
        self.__room_type = room_type  # Updates the room type
    
    def getPricePerNight(self):
        """Returns the price per night."""
        return self.__price_per_night  # Returns price per night
    
    def setPricePerNight(self, price):
        """Sets the price per night."""
        self.__price_per_night = price  # Updates the price per night
    
    def isAvailable(self):
        """Returns whether the room is available."""
        return self.__availability_status  # Returns room availability status
    
    def setAvailability(self, status):
        """Sets the room availability status."""
        self.__availability_status = status  # Updates room availability status

# Class: Guest
# Represents a guest, including their personal details and booking history
class Guest:
    """Represents a hotel guest."""
    
    def __init__(self, guest_id, guest_name, contact_info, loyalty_points, email, nationality):
        self.__guest_id = guest_id  # Unique guest ID
        self.__guest_name = guest_name  # Guest's name
        self.__contact_info = contact_info  # Guest's contact info (phone/email)
        self.__loyalty_points = loyalty_points  # Points earned by the guest
        self.__email = email  # Guest's email address
        self.__nationality = nationality  # Guest's nationality
    
    def createAccount(self):
        """Creates a new guest account."""
        print(f"Account created for {self.__guest_name}")  # Confirmation message
    
    def updateProfile(self):
        """Updates the guest profile."""
        print(f"Profile updated for {self.__guest_name}")  # Confirmation message
    
    def viewReservationHistory(self):
        """Views the guest's reservation history."""
        print(f"Reservation history for {self.__guest_name}")  # Placeholder message
    
    def getLoyaltyPoints(self):
        """Returns the guest's loyalty points."""
        return self.__loyalty_points  # Returns loyalty points
    
    def setLoyaltyPoints(self, points):
        """Sets the guest's loyalty points."""
        self.__loyalty_points = points  # Updates loyalty points
    
    def getEmail(self):
        """Returns the guest's email."""
        return self.__email  # Returns email
    
    def setEmail(self, email):
        """Sets the guest's email."""
        self.__email = email  # Updates email

# Class: PremiumGuest
# Inherits from Guest and adds premium-level features such as reward points and membership benefits
class PremiumGuest(Guest):
    """Represents a premium guest."""
    
    def __init__(self, guest_id, guest_name, contact_info, loyalty_points, email, nationality,
                 reward_points, membership_level, discount_percentage, vip_access):
        super().__init__(guest_id, guest_name, contact_info, loyalty_points, email, nationality)
        self.__reward_points = reward_points  # Reward points for premium guests
        self.__membership_level = membership_level  # Membership level (e.g., Gold, Silver)
        self.__discount_percentage = discount_percentage  # Discount percentage for premium guests
        self.__vip_access = vip_access  # VIP access status
    
    def earnPoints(self, points):
        """Earn points for premium guests."""
        self.__reward_points += points  # Adds points to reward points
    
    def redeemPoints(self):
        """Redeem reward points for premium guests."""
        self.__reward_points = 0  # Resets reward points after redemption
    
    def upgradeMembership(self):
        """Upgrades the membership level."""
        self.__membership_level = "Gold"  # Upgrades to Gold level
    
    def getMembershipLevel(self):
        """Returns the membership level."""
        return self.__membership_level  # Returns membership level
    
    def setMembershipLevel(self, level):
        """Sets a new membership level."""
        self.__membership_level = level  # Updates membership level
    
    def getDiscountPercentage(self):
        """Returns the discount percentage."""
        return self.__discount_percentage  # Returns discount percentage
    
    def setDiscountPercentage(self, percentage):
        """Sets the discount percentage."""
        self.__discount_percentage = percentage  # Updates discount percentage

# Class: Booking
# Represents a booking made by a guest, linking the guest, room, and other booking details
class Booking:
    """Represents a room booking."""
    
    def __init__(self, booking_id, guest, room, check_in_date, check_out_date, status, feedback=None):
        self.__booking_id = booking_id  # Booking ID
        self.__guest = guest  # Guest object
        self.__room = room  # Room object
        self.__check_in_date = check_in_date  # Check-in date
        self.__check_out_date = check_out_date  # Check-out date
        self.__status = status  # Booking status (e.g., confirmed, canceled)
        self.__feedback = feedback  # Feedback object (optional)
    
    def confirmBooking(self):
        """Confirms the booking."""
        self.__status = "Confirmed"  # Sets status to confirmed
    
    def cancelBooking(self):
        """Cancels the booking."""
        self.__status = "Canceled"  # Sets status to canceled
    
    def modifyBooking(self, new_dates):
        """Modifies the booking with new dates."""
        self.__check_in_date, self.__check_out_date = new_dates  # Updates the check-in and check-out dates
    
    def getCheckInDate(self):
        """Returns the check-in date."""
        return self.__check_in_date  # Returns check-in date
    
    def setCheckInDate(self, date):
        """Sets the check-in date."""
        self.__check_in_date = date  # Sets the check-in date
    
    def getCheckOutDate(self):
        """Returns the check-out date."""
        return self.__check_out_date  # Returns check-out date
    
    def setCheckOutDate(self, date):
        """Sets the check-out date."""
        self.__check_out_date = date  # Sets the check-out date

# Class: Payment
# Handles payment processing and details related to booking payments
class Payment:
    """Handles booking payment details."""
    
    def __init__(self, payment_id, payment_method, amount, transaction_date, is_successful):
        self.__payment_id = payment_id  # Payment ID
        self.__payment_method = payment_method  # Payment method (credit card, etc.)
        self.__amount = amount  # Payment amount
        self.__transaction_date = transaction_date  # Transaction date
        self.__is_successful = is_successful  # Whether the payment was successful
    
    def processPayment(self):
        """Processes the payment."""
        self.__is_successful = self.__amount > 0  # Payment succeeds if the amount is positive
    
    def generateInvoice(self):
        """Generates an invoice for the payment."""
        return f"Invoice for Payment ID: {self.__payment_id}, Amount: ${self.__amount}"  # Returns formatted invoice

    def getPaymentMethod(self):
        """Returns the payment method."""
        return self.__payment_method  # Returns payment method
    
    def setPaymentMethod(self, method):
        """Sets the payment method."""
        self.__payment_method = method  # Sets the payment method
    
    def getAmount(self):
        """Returns the payment amount."""
        return self.__amount  # Returns the amount paid
    
    def setAmount(self, amount):
        """Sets the payment amount."""
        self.__amount = amount  # Sets the payment amount

# Class: Feedback
# Stores feedback provided by guests after booking
class Feedback:
    """Stores guest feedback after booking."""
    
    def __init__(self, feedback_id, rating, comments, submission_date, guest_name):
        self.__feedback_id = feedback_id  # Feedback ID
        self.__rating = rating  # Rating given by the guest
        self.__comments = comments  # Feedback comments
        self.__submission_date = submission_date  # Date the feedback was submitted
        self.__guest_name = guest_name  # Guest's name who provided feedback
    
    def submitFeedback(self):
        """Submits feedback from the guest."""
        print(f"Feedback submitted by {self.__guest_name}: Rating {self.__rating}, Comments: {self.__comments}")
    
    def getFeedbackDetails(self):
        """Returns feedback details as a string."""
        return f"Rating: {self.__rating}, Comments: {self.__comments}"  # Returns feedback details
    
    def getRating(self):
        """Returns the rating given by the guest."""
        return self.__rating  # Returns rating
    
    def setRating(self, rating):
        """Sets the rating."""
        self.__rating = rating  # Updates the rating
    
    def getComments(self):
        """Returns the comments given by the guest."""
        return self.__comments  # Returns comments
    
    def setComments(self, comments):
        """Sets the comments."""
        self.__comments = comments  # Updates comments


