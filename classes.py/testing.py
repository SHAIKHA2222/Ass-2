"""
classes.py

Contains all classes from the final UML diagram:
Hotel, Room, Guest, PremiumGuest, Feedback, Booking, and Payment.

Each class:
- Has private attributes with double underscores.
- Uses getters and setters to access or modify data.
- Includes docstrings for clarity.
- Comments every line to explain functionality.
"""

from typing import List  # Used for typing hints like List[Room]


class Hotel:
    """
    Represents a hotel that contains multiple rooms.
    """

    def __init__(self, name: str, location: str, numberOfRooms: int,
                 hotelRating: float, contactNumber: str) -> None:
        """
        Initializes a new Hotel instance.  
        name is the hotel's name.  
        location is where the hotel is located.  
        numberOfRooms is how many rooms the hotel has.  
        hotelRating is the hotel's star or numeric rating.  
        contactNumber is the hotel's phone number.
        """
        self.__name = name  # Private attribute for the hotel's name
        self.__location = location  # Private attribute for the hotel's location
        self.__numberOfRooms = numberOfRooms  # Private attribute for the count of rooms
        self.__hotelRating = hotelRating  # Private attribute for the hotel's rating
        self.__contactNumber = contactNumber  # Private attribute for the hotel's contact number
        self.__rooms: List[Room] = []  # Private list to store Room objects

    def addRoom(self, room: 'Room') -> None:
        """
        Adds a Room object to this hotel's list of rooms.
        room is the Room to add.
        """
        self.__rooms.append(room)  # Appends the Room to the list
        self.__numberOfRooms += 1  # Increments the room count

    def removeRoom(self, room: 'Room') -> None:
        """
        Removes a Room object from this hotel's list of rooms.
        room is the Room to remove.
        """
        if room in self.__rooms:  # Checks if the Room is in the list
            self.__rooms.remove(room)  # Removes the Room from the list
            self.__numberOfRooms -= 1  # Decrements the room count

    def updateHotelRating(self, newRating: float) -> None:
        """
        Updates the hotel's rating with newRating.
        """
        self.__hotelRating = newRating  # Sets the new rating

    def getContactNumber(self) -> str:
        """
        Returns the hotel's contact number as a string.
        """
        return self.__contactNumber  # Returns the private contact number

    def setContactNumber(self, contact: str) -> None:
        """
        Sets the hotel's contact number to contact.
        """
        self.__contactNumber = contact  # Assigns the new contact number

    def getNumberOfRooms(self) -> int:
        """
        Returns how many rooms the hotel has.
        """
        return self.__numberOfRooms  # Returns the private numberOfRooms

    def setNumberOfRooms(self, count: int) -> None:
        """
        Sets the hotel's room count to count.
        """
        self.__numberOfRooms = count  # Assigns the new count

    def __str__(self) -> str:
        """
        Returns a string describing the Hotel.
        """
        # Shows hotel details including name, location, rating, room count, and contact
        return (f"Hotel [Name={self.__name}, Location={self.__location}, "
                f"Rooms={self.__numberOfRooms}, Rating={self.__hotelRating}, "
                f"Contact={self.__contactNumber}]")


class Room:
    """
    Represents a hotel room with various attributes and amenities.
    """

    def __init__(self, roomNumber: int, roomType: str, pricePerNight: float,
                 availabilityStatus: bool, maxOccupancy: int, floorNumber: int,
                 amenities: List[str]) -> None:
        """
        Initializes a new Room instance.  
        roomNumber is the unique number for the room.  
        roomType is a string describing the type (e.g., 'Deluxe').  
        pricePerNight is the cost per night.  
        availabilityStatus is True if available, False if not.  
        maxOccupancy is how many guests can stay in this room.  
        floorNumber is which floor the room is on.  
        amenities is a list of strings describing included amenities.
        """
        self.__roomNumber = roomNumber  # Private attribute for the room number
        self.__roomType = roomType  # Private attribute for the type of room
        self.__pricePerNight = pricePerNight  # Private attribute for nightly price
        self.__availabilityStatus = availabilityStatus  # Private attribute for availability
        self.__maxOccupancy = maxOccupancy  # Private attribute for max occupancy
        self.__floorNumber = floorNumber  # Private attribute for the floor
        self.__amenities = amenities  # Private attribute for a list of amenities

    def bookRoom(self) -> bool:
        """
        Books this room if it is available.  
        Returns True if successful, False otherwise.
        """
        if self.__availabilityStatus:  # Checks if the room is available
            self.__availabilityStatus = False  # Marks it as occupied
            return True  # Indicates the booking succeeded
        return False  # Indicates the room was already occupied

    def checkOut(self) -> None:
        """
        Checks out of the room, making it available again.
        """
        self.__availabilityStatus = True  # Marks the room as available

    def getRoomDetails(self) -> str:
        """
        Returns a string describing this room in detail.
        """
        # Builds a string with room info and amenities
        amenity_list = ", ".join(self.__amenities)  # Joins amenities with commas
        return (f"Room {self.__roomNumber} on floor {self.__floorNumber}, "
                f"type: {self.__roomType}, price: {self.__pricePerNight}, "
                f"max occupancy: {self.__maxOccupancy}, amenities: [{amenity_list}]")

    def addAmenity(self, amenity: str) -> None:
        """
        Adds an amenity (a string) to this room's list of amenities.
        """
        self.__amenities.append(amenity)  # Appends the new amenity

    def removeAmenity(self, amenity: str) -> None:
        """
        Removes an amenity (a string) from this room's list of amenities if present.
        """
        if amenity in self.__amenities:  # Checks if amenity is in the list
            self.__amenities.remove(amenity)  # Removes it from the list

    def setRoomType(self, roomType: str) -> None:
        """
        Sets the room type to roomType.
        """
        self.__roomType = roomType  # Updates the private roomType

    def setPricePerNight(self, price: float) -> None:
        """
        Sets the nightly price to price.
        """
        self.__pricePerNight = price  # Updates the private pricePerNight

    def isAvailable(self) -> bool:
        """
        Returns True if the room is available, False otherwise.
        """
        return self.__availabilityStatus  # Returns the availability status

    def setAvailability(self, status: bool) -> None:
        """
        Sets the room's availability to status.
        """
        self.__availabilityStatus = status  # Updates the private availabilityStatus

    def __str__(self) -> str:
        """
        Returns a concise string describing the room.
        """
        # Shows the room number, type, price, and availability
        return (f"Room [Number={self.__roomNumber}, Type={self.__roomType}, "
                f"Price={self.__pricePerNight}, Available={self.__availabilityStatus}, "
                f"Floor={self.__floorNumber}]")


class Guest:
    """
    Represents a standard guest staying at the hotel.
    """

    def __init__(self, guestID: int, guestName: str, contactInfo: str,
                 loyaltyStatus: bool, email: str, nationality: str) -> None:
        """
        Initializes a new Guest.  
        guestID is a unique identifier for the guest.  
        guestName is the guest's full name.  
        contactInfo is how to reach the guest (phone, etc.).  
        loyaltyStatus is True if the guest has loyalty membership, False otherwise.  
        email is the guest's email address.  
        nationality is the guest's nationality.
        """
        self.__guestID = guestID  # Private attribute for guest ID
        self.__guestName = guestName  # Private attribute for guest name
        self.__contactInfo = contactInfo  # Private attribute for contact info
        self.__loyaltyStatus = loyaltyStatus  # Private attribute for loyalty status
        self.__email = email  # Private attribute for the guest's email
        self.__nationality = nationality  # Private attribute for the guest's nationality

    def createAccount(self) -> None:
        """
        Simulates creating an account for this guest.
        """
        return None  # No actual logic, just a placeholder

    def updateProfile(self) -> None:
        """
        Simulates updating the guest's profile details.
        """
        return None  # No actual logic, just a placeholder

    def viewReservationHistory(self) -> None:
        """
        Simulates viewing this guest's past reservations.
        """
        return None  # No actual logic, just a placeholder

    def getLoyaltyStatus(self) -> bool:
        """
        Returns True if this guest has loyalty membership, False otherwise.
        """
        return self.__loyaltyStatus  # Returns the private loyaltyStatus

    def setLoyaltyStatus(self, status: bool) -> None:
        """
        Sets the loyalty status to status.
        """
        self.__loyaltyStatus = status  # Updates the private loyaltyStatus

    def getContactInfo(self) -> str:
        """
        Returns the contact info for this guest.
        """
        return self.__contactInfo  # Returns the private contactInfo

    def setContactInfo(self, contact: str) -> None:
        """
        Updates the contact info to contact.
        """
        self.__contactInfo = contact  # Updates the private contactInfo

    def __str__(self) -> str:
        """
        Returns a string describing the guest.
        """
        # Shows the guest's ID, name, email, and loyalty status
        return (f"Guest [ID={self.__guestID}, Name={self.__guestName}, "
                f"Email={self.__email}, LoyaltyStatus={self.__loyaltyStatus}]")

class PremiumGuest(Guest):
    """
    Represents a premium guest with additional perks.
    """

    def __init__(self, guestID: int, guestName: str, contactInfo: str,
                 loyaltyStatus: bool, email: str, nationality: str,
                 rewardPoints: int, membershipLevel: str,
                 discountPercentage: float, vipAccess: bool) -> None:
        """
        Initializes a PremiumGuest.  
        guestID, guestName, contactInfo, loyaltyStatus, email, nationality  
        are passed to the base Guest constructor.  
        rewardPoints is an integer tracking extra reward points.  
        membershipLevel is a string describing the membership tier.  
        discountPercentage is a float for discount rates.  
        vipAccess is True if the guest has VIP lounge access.
        """
        super().__init__(guestID, guestName, contactInfo,
                         loyaltyStatus, email, nationality)  # Calls the parent constructor
        self.__rewardPoints = rewardPoints  # Private attribute for extra reward points
        self.__membershipLevel = membershipLevel  # Private attribute for membership level
        self.__discountPercentage = discountPercentage  # Private attribute for discount
        self.__vipAccess = vipAccess  # Private attribute for VIP lounge access

    def earnPoints(self, points: int) -> None:
        """
        Adds points to this premium guest's rewardPoints total.
        """
        self.__rewardPoints += points  # Increments reward points

    def redeemPoints(self) -> bool:
        """
        Redeems all rewardPoints.  
        Returns True if successful, False if there were no points.
        """
        if self.__rewardPoints > 0:  # Checks if there's something to redeem
            self.__rewardPoints = 0  # Resets points
            return True  # Indicates success
        return False  # Indicates no points to redeem

    def upgradeMembership(self) -> None:
        """
        Simulates upgrading the membership level.
        """
        return None  # Placeholder for future logic

    def getMembershipLevel(self) -> str:
        """
        Returns the membership level as a string.
        """
        return self.__membershipLevel  # Returns the private membership level

    def setMembershipLevel(self, level: str) -> None:
        """
        Sets the membership level to level.
        """
        self.__membershipLevel = level  # Updates the private membership level

    def getDiscountPercentage(self) -> float:
        """
        Returns the discount percentage as a float.
        """
        return self.__discountPercentage  # Returns the private discount

    def setDiscountPercentage(self, percentage: float) -> None:
        """
        Sets the discount percentage to percentage.
        """
        self.__discountPercentage = percentage  # Updates the private discount

    def __str__(self) -> str:
        """
        Returns a string describing this premium guest.
        """
        base_str = super().__str__()  # Gets the parent string
        # Appends premium info
        return (f"{base_str} [Premium: Level={self.__membershipLevel}, "
                f"RewardPoints={self.__rewardPoints}, "
                f"Discount={self.__discountPercentage}, VIP={self.__vipAccess}]")


class Payment:
    """
    Represents a payment made for a booking.
    """

    def __init__(self, paymentID: int, paymentMethod: str, amount: float,
                 transactionDate: str, isSuccessful: bool) -> None:
        """
        Initializes a Payment.  
        paymentID is the unique payment identifier.  
        paymentMethod is how the guest paid (e.g., 'Credit Card').  
        amount is the total paid.  
        transactionDate is when the payment occurred.  
        isSuccessful is True if payment succeeded, False otherwise.
        """
        self.__paymentID = paymentID  # Private attribute for payment ID
        self.__paymentMethod = paymentMethod  # Private attribute for method
        self.__amount = amount  # Private attribute for amount
        self.__transactionDate = transactionDate  # Private attribute for date
        self.__isSuccessful = isSuccessful  # Private attribute for success flag

    def processPayment(self) -> bool:
        """
        Processes this payment.  
        Returns True if successful, False otherwise.
        """
        return self.__isSuccessful  # Returns the success flag

    def generateInvoice(self) -> str:
        """
        Generates and returns an invoice string for this payment.
        """
        # Builds an invoice string
        return (f"Invoice -> PaymentID: {self.__paymentID}, "
                f"Amount: {self.__amount}, Method: {self.__paymentMethod}")

    def getPaymentMethod(self) -> str:
        """
        Returns the payment method as a string.
        """
        return self.__paymentMethod  # Returns the private paymentMethod

    def setPaymentMethod(self, method: str) -> None:
        """
        Sets the payment method to method.
        """
        self.__paymentMethod = method  # Updates the private paymentMethod

    def getAmount(self) -> float:
        """
        Returns the amount as a float.
        """
        return self.__amount  # Returns the private amount

    def setAmount(self, amount: float) -> None:
        """
        Sets the amount to amount.
        """
        self.__amount = amount  # Updates the private amount

    def __str__(self) -> str:
        """
        Returns a string describing this payment.
        """
        # Shows payment details
        return (f"Payment [ID={self.__paymentID}, Method={self.__paymentMethod}, "
                f"Amount={self.__amount}, Date={self.__transactionDate}, "
                f"Success={self.__isSuccessful}]")


class Feedback:
    """
    Represents feedback provided by a guest about their stay.
    """

    def __init__(self, feedbackID: int, rating: int, comments: str,
                 submissionDate: str, guestName: str) -> None:
        """
        Initializes Feedback.  
        feedbackID is a unique identifier for this feedback.  
        rating is an integer rating (e.g., 1-5).  
        comments is a string of remarks from the guest.  
        submissionDate is when this feedback was submitted.  
        guestName is who provided the feedback.
        """
        self.__feedbackID = feedbackID  # Private attribute for feedback ID
        self.__rating = rating  # Private attribute for rating
        self.__comments = comments  # Private attribute for comments
        self.__submissionDate = submissionDate  # Private attribute for date
        self.__guestName = guestName  # Private attribute for guest name

    def submitFeedback(self) -> None:
        """
        Simulates submitting this feedback.
        """
        return None  # Placeholder for future logic

    def getFeedbackDetails(self) -> str:
        """
        Returns a string containing detailed feedback info.
        """
        # Builds a feedback summary
        return (f"Feedback ID: {self.__feedbackID}, Rating: {self.__rating}, "
                f"Comments: {self.__comments}, Date: {self.__submissionDate}, "
                f"Guest: {self.__guestName}")

    def setRating(self, rating: int) -> None:
        """
        Sets the rating to rating.
        """
        self.__rating = rating  # Updates the private rating

    def setComments(self, comments: str) -> None:
        """
        Sets the comments to comments.
        """
        self.__comments = comments  # Updates the private comments

    def __str__(self) -> str:
        """
        Returns a concise string describing the feedback.
        """
        # Calls getFeedbackDetails to produce a summary
        return self.getFeedbackDetails()


class Booking:
    """
    Represents a reservation made by a guest for a specific room.
    """

    def __init__(self, bookingID: int, guest: Guest, room: Room,
                 checkInDate: str, checkOutDate: str, status: str,
                 feedback: Feedback = None) -> None:
        """
        Initializes a Booking.  
        bookingID is the unique booking identifier.  
        guest is the Guest who made this booking.  
        room is the Room that is booked.  
        checkInDate is the date of arrival.  
        checkOutDate is the date of departure.  
        status could be 'Pending', 'Confirmed', or 'Cancelled'.  
        feedback is optional Feedback about this booking.
        """
        self.__bookingID = bookingID  # Private attribute for booking ID
        self.__guest = guest  # Private attribute referencing the Guest
        self.__room = room  # Private attribute referencing the Room
        self.__checkInDate = checkInDate  # Private attribute for check-in
        self.__checkOutDate = checkOutDate  # Private attribute for check-out
        self.__status = status  # Private attribute for booking status
        self.__feedback = feedback  # Private attribute for optional Feedback

    def confirmBooking(self) -> bool:
        """
        Confirms the booking if the room is available.  
        Returns True if confirmed, False otherwise.
        """
        if self.__room.isAvailable():  # Checks if the room is free
            self.__room.bookRoom()  # Books the room
            self.__status = "Confirmed"  # Changes status to Confirmed
            return True  # Indicates success
        return False  # Indicates failure if room wasn't available

    def cancelBooking(self) -> bool:
        """
        Cancels the booking if not already cancelled.  
        Returns True if cancellation succeeds, False otherwise.
        """
        if self.__status != "Cancelled":  # Checks if it's not already cancelled
            self.__status = "Cancelled"  # Marks it as cancelled
            self.__room.setAvailability(True)  # Frees up the room
            return True  # Indicates a successful cancellation
        return False  # Indicates it was already cancelled

    def modifyBooking(self, newDates: str) -> bool:
        """
        Modifies the booking's check-in and check-out dates if confirmed.  
        newDates is a string with new check-in/out info.  
        Returns True if modification succeeds, False otherwise.
        """
        if self.__status == "Confirmed":  # Only allow if booking is confirmed
            # In a real system, parse newDates for separate check-in and check-out
            # For simplicity, just store the string
            # This is not exactly how the diagram does it, but we can mimic
            self.__checkInDate = newDates  # Overwrites with newDates
            self.__checkOutDate = newDates  # Overwrites with newDates
            return True  # Indicates success
        return False  # Indicates not confirmed

    def getCheckInDate(self) -> str:
        """
        Returns the check-in date as a string.
        """
        return self.__checkInDate  # Returns the private checkInDate

    def setCheckInDate(self, date: str) -> None:
        """
        Sets the check-in date to date.
        """
        self.__checkInDate = date  # Updates the private checkInDate

    def getCheckOutDate(self) -> str:
        """
        Returns the check-out date as a string.
        """
        return self.__checkOutDate  # Returns the private checkOutDate

    def setCheckOutDate(self, date: str) -> None:
        """
        Sets the check-out date to date.
        """
        self.__checkOutDate = date  # Updates the private checkOutDate

    def __str__(self) -> str:
        """
        Returns a string describing this booking.
        """
        feedback_str = str(self.__feedback) if self.__feedback else "No Feedback"  # String for feedback
        return (f"Booking [ID={self.__bookingID}, Guest={self.__guest}, "
                f"Room={self.__room}, CheckIn={self.__checkInDate}, "
                f"CheckOut={self.__checkOutDate}, Status={self.__status}, "
                f"Feedback={feedback_str}]")
