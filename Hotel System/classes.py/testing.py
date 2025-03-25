
# =============================
# Testing section
# =============================
def run_tests():
    print("===== TESTING HOTEL SYSTEM =====")

    # Create Hotel and Rooms (Composition)
    hotel = Hotel("Royal Stay", "Dubai", 5, "+971-55-1234567")
    room1 = Room(101, "Single", 200, ["Wi-Fi", "TV"])
    room2 = Room(102, "Double", 300, ["Wi-Fi", "TV", "Mini-bar"])
    hotel.add_room(room1)
    hotel.add_room(room2)

    # Create Guests (Aggregation)
    guest1 = Guest(1, "Alice", "alice@email.com", "UAE")
    guest2 = PremiumGuest(2, "Bob", "bob@email.com", "UK")
    guest1.create_account()
    guest2.create_account()

    # View available rooms before booking
    print("\nAvailable Rooms:")
    for room in hotel.get_available_rooms():
        print(f"Room Type: {room.get_room_type()}, Price: {room.get_price()}")

    # Create Bookings (Aggregation)
    booking1 = Booking(1001, guest1, room1, date(2025, 3, 28), date(2025, 3, 30))
    booking2 = Booking(1002, guest2, room2, date(2025, 3, 28), date(2025, 3, 30))

    # Confirm Bookings
    if booking1.confirm_booking():
        print(f"Booking {booking1.get_id()} confirmed for {guest1.get_name()}")
    if booking2.confirm_booking():
        print(f"Booking {booking2.get_id()} confirmed for {guest2.get_name()}")

    guest1.add_booking(booking1)
    guest2.add_booking(booking2)

    # Add Feedback (Unary)
    fb1 = Feedback(5001, 5, "Excellent stay!", guest1.get_name())
    fb2 = Feedback(5002, 4, "Very clean and comfortable.", guest2.get_name())
    booking1.add_feedback(fb1)
    booking2.add_feedback(fb2)
    fb1.submit()
    fb2.submit()

    # Payments (Binary)
    payment1a = Payment(2001, "Credit Card", 150)
    payment1b = Payment(2002, "Mobile Wallet", 50)
    payment2 = Payment(2003, "Debit Card", 300)

    for p in [payment1a, payment1b, payment2]:
        p.process()

    booking1.add_payment(payment1a)
    booking1.add_payment(payment1b)
    booking2.add_payment(payment2)

    print("\nInvoices:")
    for p in [payment1a, payment1b, payment2]:
        print(p.generate_invoice())

    print("\nReservation History:")
    guest1.view_reservation_history()
    guest2.view_reservation_history()

    booking1.cancel_booking()
    print(f"\nBooking {booking1.get_id()} status after cancellation: {booking1.get_status()}")

# Run test only if this script is run directly
if __name__ == "__main__":
    run_tests()
