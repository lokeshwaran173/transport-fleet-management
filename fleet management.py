import csv

class Vehicle:
    def __init__(self, make, model, license_plate, total_students=0):
        self.make = make
        self.model = model
        
        self.license_plate = license_plate
        self.total_students = total_students

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate}) - Total Students: {self.total_students}"


class FleetManager:
    def __init__(self):
        self.fleet = []
        self.load_from_csv("fleet.csv")  # Load fleet data from CSV at the start

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)

    def delete_vehicle(self, vehicle):
        self.fleet.remove(vehicle)

    def view_fleet(self):
        if not self.fleet:
            print("No vehicles in the fleet.")
        else:
            for index, vehicle in enumerate(self.fleet, 1):
                print(f"{index}. {vehicle}")

    def total_vehicles(self):
        return len(self.fleet)

    def load_from_csv(self, filename):
        try:
            with open(filename, 'r', newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    vehicle = Vehicle(row['Make'], row['Model'],
                                      row['License Plate'], int(row['Total Students']))
                    self.add_vehicle(vehicle)
        except FileNotFoundError:
            print("CSV file not found. Starting with an empty fleet.")

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Make', 'Model', 'License Plate', 'Total Students']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for vehicle in self.fleet:
                writer.writerow({
                    'Make': vehicle.make,
                    'Model': vehicle.model,
                   
                    'License Plate': vehicle.license_plate,
                    'Total Students': vehicle.total_students
                })


def main():
    fleet_manager = FleetManager()

    while True:
        print("\n--- Fleet Management Menu ---")
        print("1. Add Vehicle")
        print("2. View Fleet")
        print("3. Total Vehicles")
        print("4. Delete Vehicle")
        print("5. Save to CSV")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            print("Enter vehicle details:")
            make = input("Make: ")
            model = input("Model: ")
            license_plate = input("License Plate: ")
            total_students = int(input("Total Students in Bus: "))

            vehicle = Vehicle(make, model, license_plate, total_students)
            fleet_manager.add_vehicle(vehicle)
            print("Vehicle added to the fleet successfully.")

        elif choice == '2':
            print("\n--- Fleet List ---")
            fleet_manager.view_fleet()

        elif choice == '3':
            total_vehicles = fleet_manager.total_vehicles()
            print(f"Total number of vehicles in the fleet: {total_vehicles}")

        elif choice == '4':
            print("\n--- Fleet List ---")
            fleet_manager.view_fleet()
            try:
                vehicle_index = int(input("Enter the number of the vehicle you want to delete: "))
                if 1 <= vehicle_index <= len(fleet_manager.fleet):
                    vehicle_to_delete = fleet_manager.fleet[vehicle_index - 1]
                    fleet_manager.delete_vehicle(vehicle_to_delete)
                    print("Vehicle deleted from the fleet.")
                else:
                    print("Invalid vehicle number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '5':
            fleet_manager.save_to_csv("fleet.csv")
            print("Fleet data saved to CSV.")

        elif choice == '6':
            print("Exiting the Fleet Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
