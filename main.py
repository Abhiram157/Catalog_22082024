class ChargingStation:
    def __init__(self, name, location, station_type, slots):
        self.name = name
        self.location = location
        self.type = station_type
        # Create a copy of slots to ensure each station has its own slots
        self.slots = [ChargingSlot(slot.time) for slot in slots]

    def __str__(self):
        return f"{self.name} ({self.type}) - {self.location}"


class ChargingSlot:
    def __init__(self, time):
        self.time = time
        self.is_booked = False

    def __str__(self):
        status = "Booked" if self.is_booked else "Available"
        return f"{self.time} - {status}"


def create_stations():
    # Define the time slots
    slots = [ChargingSlot(f"{hour}:00 AM") for hour in range(8, 12)] + \
            [ChargingSlot(f"{hour}:00 PM") for hour in range(12, 6)]

    stations = [
        ChargingStation(
            name="Station 1",
            location="123 Main St",
            station_type="Fast",
            slots=slots
        ),
        ChargingStation(
            name="Station 2",
            location="456 Elm St",
            station_type="Standard",
            slots=slots
        ),
        ChargingStation(
            name="Station 3",
            location="789 Oak St",
            station_type="Fast",
            slots=slots
        ),
        ChargingStation(
            name="Station 4",
            location="321 Pine St",
            station_type="Super Fast",
            slots=slots
        ),
        ChargingStation(
            name="Station 5",
            location="654 Cedar St",
            station_type="Standard",
            slots=slots
        ),
    ]
    return stations


def find_stations(stations, station_type=None):
    if station_type:
        return [station for station in stations if station.type == station_type]
    return stations


def book_slot(station, slot_time):
    for slot in station.slots:
        if slot.time == slot_time and not slot.is_booked:
            slot.is_booked = True
            return f"Slot at {slot_time} has been successfully booked at {station.name}."
    return "Slot not available."


def main():
    stations = create_stations()
    print("\n--- EV Charging Station Finder ---")
    while True:
        print("1. Find Charging Stations")
        print("2. Book a Slot")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            station_type = input("Enter station type (Fast/Standard/Super Fast) or press Enter to skip: ")
            available_stations = find_stations(stations, station_type if station_type else None)
            if available_stations:
                print("\nAvailable Charging Stations:")
                for i, station in enumerate(available_stations):
                    print(f"{i + 1}. {station}")
            else:
                print("No stations found.")

        elif choice == '2':
            station_index = int(input("Enter station number to book a slot: ")) - 1
            if 0 <= station_index < len(stations):
                station = stations[station_index]
                print(f"\nAvailable Slots at {station.name}:")
                for slot in station.slots:
                    print(slot)

                slot_time = input("Enter the time of the slot you want to book: ")
                result = book_slot(station, slot_time)
                print(result)
            else:
                print("Invalid station number.")

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
