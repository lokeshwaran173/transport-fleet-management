import csv

class Vehicle:
    def __init__(self, make, model, year, license_plate):
        self.make = make
        self.model = model
        self.year = year
        self.license_plate = license_plate

    def __str__(self):
        return f"{self.year} {self.make} {self.model} ({self.license_plate})"


class FleetManager:
    def __init__(self):
        self.fleet = []
        self.load_from_csv("C:\Users\ZF-7\Downloads\scm-biz-suite-master\scm-biz-suite-master\.vscode\fleet.csv")  # Load fleet data from CSV at the start

    def add_vehicle(self, vehicle):
        self.fleet.append(vehicle)
        self.save_to_csv("C:\Users\ZF-7\Downloads\scm-biz-suite-master\scm-biz-suite-master\.vscode\fleet.csv")  # Automatically save after adding a vehicle

    def delete_vehicle(self, vehicle):
        self.fleet.remove(vehicle)
        self.save_to_csv("C:\Users\ZF-7\Downloads\scm-biz-suite-master\scm-biz-suite-master\.vscode\fleet.csv1")  # Automatically save after deleting a vehicle

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
                    vehicle = Vehicle(row['Make'], row['Model'], int(row['Year']), row['License Plate'])
                    self.add_vehicle(vehicle)
        except FileNotFoundError:
            print("CSV file not found. Starting with an empty fleet.")

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            fieldnames = ['Make', 'Model', 'Year', 'License Plate']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()

            for vehicle in self.fleet:
                writer.writerow({
                    'Make': vehicle.make,
                    'Model': vehicle.model,
                    'Year': vehicle.year,
                    'License Plate': vehicle.license_plate
                })


def main():
    fleet_manager = FleetManager()

    while True:
        print("\n--- Fleet Management Menu ---")
        print("1. Add Vehicle")
        print("2. View Fleet")
        print("3. Total Vehicles")
        print("4. Delete Vehicle")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            # ... (Add Vehicle functionality remains the same)

        elif choice == '2':
            # ... (View Fleet functionality remains the same)

        elif choice == '3':
            # ... (Total Vehicles functionality remains the same)

        elif choice == '4':
            # ... (Delete Vehicle functionality remains the same)

        elif choice == '5':
            print("Exiting the Fleet Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()