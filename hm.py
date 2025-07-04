class Hotel:
    def __init__(self, rooms):
        self.rooms = rooms
        self.booked_rooms = []

    def display_available_rooms(self):
        print("Available Rooms:")
        for room in self.rooms:
            if room not in self.booked_rooms:
                print(room)

    def book_room(self, room_number):
        if room_number in self.rooms and room_number not in self.booked_rooms:
            self.booked_rooms.append(room_number)
            print("Room booked successfully!")
        else:
            print("Room not available or already booked.")

    def cancel_booking(self, room_number):
        if room_number in self.booked_rooms:
            self.booked_rooms.remove(room_number)
            print("Booking cancelled successfully!")
        else:
            print("Room not booked.")

# Example usage:
hotel = Hotel([101, 102, 103, 104, 105])

while True:
    print("\nHotel Management System")
    print("1. Display Available Rooms")
    print("2. Book a Room")
    print("3. Cancel a Booking")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        hotel.display_available_rooms()
    elif choice == 2:
        room_number = int(input("Enter room number to book: "))
        hotel.book_room(room_number)
    elif choice == 3:
        room_number = int(input("Enter room number to cancel: "))
        hotel.cancel_booking(room_number)
    elif choice == 4:
        break
    else:
        print("Invalid choice.")