class Room:
    def __init__(self, room_number, room_type, price):
        self.room_number = room_number
        self.room_type = room_type
        self.price = price
        self.is_available = True
        self.guest_name = None

    def check_in(self, guest_name):
        if self.is_available:
            self.is_available = False
            self.guest_name = guest_name
            print(f"Checked in {guest_name} to room {self.room_number}.")
            return True
        print(f"Room {self.room_number} is not available.")
        return False

    def check_out(self):
        if not self.is_available:
            guest_name = self.guest_name
            self.is_available = True
            self.guest_name = None
            print(f"Checked out {guest_name} from room {self.room_number}.")
            return guest_name
        print(f"Room {self.room_number} is already available.")
        return None

    def __str__(self):
        status = "Available" if self.is_available else f"Occupied by {self.guest_name}"
        return f"Room {self.room_number} ({self.room_type}): INR{self.price}/night - {status}"


class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []
        self.guests = {}  # {guest_name: room_number}

    def add_room(self, room):
        self.rooms.append(room)

    def check_in(self, room_number, guest_name):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.check_in(guest_name):
                    self.guests[guest_name] = room_number
                return
        print(f"Room {room_number} not found.")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                guest_name = room.check_out()
                if guest_name:
                    self.guests.pop(guest_name, None)
                return
        print(f"Room {room_number} not found.")

    def show_guests(self):
        if not self.guests:
            print("No guests currently checked in.")
            return
        
        print("\nCurrent Guest List:")
        print("==================")
        print(f"{'Guest Name':<20} | {'Room No.':<10} | {'Room Type':<15} | {'Price/Night':<12}")
        print("-" * 65)
        
        for guest_name, room_no in self.guests.items():
            room = self.find_room(room_no)
            if room:
                print(f"{guest_name:<20} | {room_no:<10} | {room.room_type:<15} | INR{room.price:<10}")

    def find_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room
        return None

    def get_guest_info(self, guest_name):
        room_number = self.guests.get(guest_name)
        if room_number:
            room = self.find_room(room_number)
            print("\nGuest Information:")
            print(f"Name: {guest_name}")
            print(f"Room Number: {room_number}")
            print(f"Room Type: {room.room_type}")
            print(f"Price: INR{room.price}/night")
        else:
            print(f"No guest found with name: {guest_name}")

    def show_rooms(self):
        print("\nRoom Status:")
        print(f"{'Room No.':<10} | {'Type':<15} | {'Price/Night':<12} | {'Status':<20}")
        print("-" * 60)
        for room in sorted(self.rooms, key=lambda x: x.room_number):
            status = "Available" if room.is_available else f"Occupied by {room.guest_name}"
            print(f"{room.room_number:<10} | {room.room_type:<15} | INR{room.price:<10} | {status:<20}")


def main():
    # Initialize hotel
    hotel = Hotel("MY VILLA GRAND HOTEL;")
    
    # Add sample rooms
    hotel.add_room(Room(1,"SINGLE ROOM", 1300))
    hotel.add_room(Room(2,"DOUBLE ROOM", 1800))
    hotel.add_room(Room(3,"SINGLE ROOM", 1300))
    hotel.add_room(Room(4,"DOUBLE ROOM", 1800)) 
    hotel.add_room(Room(5,"SINGLE ROOM", 1300)) 
    hotel.add_room(Room(6,"DOUBLE ROOM", 1800)) 
    hotel.add_room(Room(7,"SINGLE ROOM", 1300)) 
    hotel.add_room(Room(8,"DOUBLE ROOM", 1800)) 
    hotel.add_room(Room(9,"SINGLE ROOM", 1300)) 
    hotel.add_room(Room(10,"DOUBLE ROOM", 1800))
    hotel.add_room(Room(11, "DELUXE QUEEN", 2500))
    hotel.add_room(Room(12, "DELUXE KING", 2800))
    hotel.add_room(Room(13, "DELUXE COUPLE", 4500))
    hotel.add_room(Room(14, "DELUXE QUEEN", 2500))
    hotel.add_room(Room(15, "DELUXE KING", 2800))
    hotel.add_room(Room(16, "DELUXE COUPLE", 4500))
    hotel.add_room(Room(17, "DELUXE QUEEN", 2500))
    hotel.add_room(Room(18, "DELUXE KING", 2800))
    hotel.add_room(Room(19, "DELUXE COUPLE", 4500))
    hotel.add_room(Room(20, "DELUXE", 2500))
    hotel.add_room(Room(21, "Suite", 4100))
    hotel.add_room(Room(22, "Suite", 4100))
    hotel.add_room(Room(23, "Suite", 4100))
    hotel.add_room(Room(24, "Suite", 4100))
    hotel.add_room(Room(25, "Suite", 4100))
    hotel.add_room(Room(26, "Suite", 4100))
    hotel.add_room(Room(27, "Suite", 4100))
    hotel.add_room(Room(28, "Suite", 4100))
    hotel.add_room(Room(29, "Suite", 4100))
    hotel.add_room(Room(30, "Suite", 4100))
    hotel.add_room(Room(31, "Executive Suite", 5100))
    hotel.add_room(Room(32, "Executive Suite", 5100))
    hotel.add_room(Room(33, "Executive Suite", 5100))
    hotel.add_room(Room(34, "Executive Suite", 5100))
    hotel.add_room(Room(35, "Executive Suite", 5100))
    hotel.add_room(Room(36, "Executive Suite", 5100))
    hotel.add_room(Room(37, "Executive Suite", 5100))
    hotel.add_room(Room(38, "Executive Suite", 5100))
    hotel.add_room(Room(39, "Executive Suite", 5100))
    hotel.add_room(Room(40, "Executive Suite", 5100))

    while True:
        print("\n" + "-" * 39)
        print(f"{hotel.name}- MANAGMENt SYSTEM")
        print("-" * 39)
        print("WELCOME TO HOTEL:-")
        print("-" * 16)
        print("1. SHOW ROOM STATUS")
        print("2. CHECK IN GUEST")
        print("3. SHOW GUEST LIST")
        print("4. GET GUEST INFO")
        print("5. CHECK OUT GUEST")
        print("6. EXIT")
        
        choice = input("\nEnter your choice (1-6): ").strip()
        
        if choice == '1':  # Show Room Status
            hotel.show_rooms()
            try:
                room_number = int(input("\nEnter room number to check in: "))
                guest_name = input("Enter guest name: ").strip()
                hotel.check_in(room_number, guest_name)
            except ValueError:
                print("Invalid input. Please enter a valid room number.")

        elif choice == '2':  # Check In
            print("\nAvailable Rooms:")
            hotel.show_rooms()
            try:
                room_number = int(input("\nEnter room number to check in: "))
                guest_name = input("Enter guest name: ").strip()
                hotel.check_in(room_number, guest_name)
            except ValueError:
                print("Invalid input. Please enter a valid room number.")

        elif choice == '3':  # Show Guest List
            hotel.show_guests()

        elif choice == '4':  # Get Guest Info
            guest_name = input("\nEnter guest name to search: ").strip()
            hotel.get_guest_info(guest_name)

        elif choice == '5':  # Check Out
            hotel.show_guests()
            if hotel.guests:
                try:
                    room_number = int(input("\nEnter room number to check out: "))
                    hotel.check_out(room_number)
                except ValueError:
                    print("Invalid input. Please enter a valid room number.")
                    
        elif choice == '6':  # Exit
            print("\n      --- THANK YOU FOR USING OUR SERVICE ---")
            print("               ---HAVE A GOOD DAY---")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 6.")

        input("\nPress Enter to continue...")


if __name__ == "__main__":
    main()
