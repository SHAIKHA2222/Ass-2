
# =============================
# TESTING SECTION – Reflects all associations in UML
# =============================
def run_tests():
    print("===== TESTING HOTEL SYSTEM =====")  # Header for test output

    # Create a hotel and add rooms (Composition)
    hotel = Hotel("Royal Stay", "Dubai", 5, "+971-55-1234567")  # Hotel instance
    room1 = Room(101, "Single", 200, ["Wi-Fi", "TV"])  # Room 101
    room2 = Room(102, "Double", 300, ["Wi-Fi", "TV", "Mini-bar"])  # Room 102
    hotel.add_room(room1)  # Add room1 to hotel
    hotel.add_room(room2)  # Add room2 to hotel

    # Create guest accounts (Aggregation)
    guest1 = Guest(1, "Alice", "alice@email.com", "UAE")  # First guest
    guest2 = PremiumGuest(2, "Bob", "bob@email.com", "UK")  # Premium guest
    guest1.create_account()  # Simulate account creation
    guest2.create_account()

    # Search and display available rooms
    print("\nAvailable Rooms:")
    for room in hotel.get_available_rooms():  # Loop through available rooms
        print(f"Room Type: {room.get_room_type()}, Price: {room.get_price()}")  # Display room info

    # Make bookings (Aggregation)
    booking1 = Booking(1001, guest1, room1, date(2025, 3, 28), date(2025, 3, 30))  # Booking by guest1
    booking2 = Booking(1002, guest2, room2, date(2025, 3, 28), date(2025, 3, 30))  # Booking by guest2

    # Confirm bookings
    if booking1.confirm_booking():
        print(f"Booking {booking1.get_id()} confirmed for {guest1.get_name()}")  # Confirm guest1
    if booking2.confirm_booking():
        print(f"Booking {booking2.get_id()} confirmed for {guest2.get_name()}")  # Confirm guest2

    # Add bookings to guest history
    guest1.add_booking(booking1)  # Add booking1 to guest1
    guest2.add_booking(booking2)  # Add booking2 to guest2

    # Submit feedback (Unary)
    fb1 = Feedback(5001, 5, "Excellent stay!", guest1.get_name())  # Feedback by guest1
    fb2 = Feedback(5002, 4, "Very clean and comfortable.", guest2.get_name())  # Feedback by guest2
    booking1.add_feedback(fb1)  # Attach feedback to booking1
    booking2.add_feedback(fb2)  # Attach feedback to booking2
    fb1.submit()  # Submit feedback1
    fb2.submit()  # Submit feedback2

    # Create and process payments (Binary)
    payment1a = Payment(2001, "Credit Card", 150)  # First part payment by guest1
    payment1b = Payment(2002, "Mobile Wallet", 50)  # Second part payment by guest1
    payment2 = Payment(2003, "Debit Card", 300)  # Full payment by guest2

    for p in [payment1a, payment1b, payment2]:  # Process all payments
        p.process()

    booking1.add_payment(payment1a)  # Link payment1a to booking1
    booking1.add_payment(payment1b)  # Link payment1b to booking1
    booking2.add_payment(payment2)  # Link payment2 to booking2

    # Display invoices
    print("\nInvoices:")
    for p in [payment1a, payment1b, payment2]:
        print(p.generate_invoice())  # Print invoice for each payment

    # View reservation histories
    print("\nReservation History:")
    guest1.view_reservation_history()  # Guest1's bookings
    guest2.view_reservation_history()  # Guest2's bookings

    # Cancel a booking
    booking1.cancel_booking()  # Cancel booking1
    print(f"\nBooking {booking1.get_id()} status after cancellation: {booking1.get_status()}")  # Show status

# Run the test function when this file is executed
if __name__ == "__main__":
    run_tests()

