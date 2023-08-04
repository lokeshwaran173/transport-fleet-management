import csv
import os

class Vehicle:
    def __init__(self, make, model, driver_name, license_plate, total_students=0, route_name=""):
        self.make = make
        self.model = model
        self.driver_name = driver_name
        self.license_plate = license_plate
        self.total_students = total_students
        self.route_name = route_name

    def __str__(self):
        return f"{self.make} {self.model} ({self.license_plate}) - Driver: {self.driver_name}, Total Students: {self.total_students}, Route: {self.route_name}"


class FleetManager:
    def __init__(self):
        self.fleet = []
        self.load_from_csv("fleet.csv")  # Load fleet data from CSV at the start

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)
        self.save_to_csv("fleet.csv")  # Automatically save after adding a vehicle

    def delete_vehicle(self, vehicle):
        self.fleet.remove(vehicle)
        self.save_to_csv("fleet.csv")  # Automatically save after deleting a vehicle

    def edit_vehicle(self, vehicle, make, model, driver_name, license_plate, total_students, route_name):
        vehicle.make = make
        vehicle.model = model
        vehicle.driver_name = driver_name
        vehicle.license_plate = license_plate
        vehicle.total_students = total_students
        vehicle.route_name = route_name
        self.save_to_csv("fleet.csv")  # Automatically save after editing a vehicle

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
                    make = row.get('Make', '')
                    model = row.get('Model', '')
                    driver_name = row.get('Driver Name', '')
                    license_plate = row.get('License Plate', '')
                    total_students_str = row.get('Total Students', '0')
                    total_students = int(total_students_str) if total_students_str else 0
                    route_name = row.get('Route Name', '')

                    vehicle = Vehicle(make, model, driver_name, license_plate, total_students, route_name)
                    self.add_vehicle(vehicle)
        except FileNotFoundError:
            print("CSV file not found. Starting with an empty fleet.")

    def save_to_csv(self, filename):
        current_directory = os.getcwd()
        file_path = os.path.join(current_directory, filename)

        with open(file_path, 'w', newline='') as csvfile:
            fieldnames = ['Make', 'Model', 'Driver Name', 'License Plate', 'Total Students', 'Route Name']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for vehicle in self.fleet:
                writer.writerow({
                    'Make': vehicle.make,
                    'Model': vehicle.model,
                    'Driver Name': vehicle.driver_name,
                    'License Plate': vehicle.license_plate,
                    'Total Students': vehicle.total_students,
                    'Route Name': vehicle.route_name
                })


def main():
    fleet_manager = FleetManager()

    while True:
        print("\n--- Fleet Management Menu ---")
        print("1. Add Vehicle")
        print("2. View Fleet")
        print("3. Total Vehicles")
        print("4. Edit Vehicle Details")
        print("5. Delete Vehicle")
        print("6. Save to CSV")
        print("7. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == '1':
            print("Enter vehicle details:")
            make = input("Make: ")
            model = input("Model: ")
            driver_name = input("Driver Name: ")
            license_plate = input("License Plate: ")
            total_students = int(input("Total Students in Bus: "))
            route_name = input("Route Name: ")

            vehicle = Vehicle(make, model, driver_name, license_plate, total_students, route_name)
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
                vehicle_index = int(input("Enter the number of the vehicle you want to edit: "))
                if 1 <= vehicle_index <= len(fleet_manager.fleet):
                    vehicle_to_edit = fleet_manager.fleet[vehicle_index - 1]
                    print("\nEnter new vehicle details:")
                    make = input("Make: ")
                    model = input("Model: ")
                    driver_name = input("Driver Name: ")
                    license_plate = input("License Plate: ")
                    total_students = int(input("Total Students in Bus: "))
                    route_name = input("Route Name: ")

                    fleet_manager.edit_vehicle(vehicle_to_edit, make, model, driver_name, license_plate, total_students, route_name)
                    print("Vehicle details edited successfully.")
                else:
                    print("Invalid vehicle number. Please try again.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")

        elif choice == '5':
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

        elif choice == '6':
            fleet_manager.save_to_csv("fleet.csv")
            print("Fleet data saved to CSV.")

        elif choice == '7':
            print("Exiting the Fleet Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
