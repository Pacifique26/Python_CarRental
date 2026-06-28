from datetime import datetime

class CarRental:
    def __init__(self, stock=0):
        self.stock = stock

    def display_stock(self):
        print(f"\n[INFO] Available cars: {self.stock}")
        return self.stock

    def rent_hourly(self, n):
        if n <= 0:
            print("[ERROR] Number of cars should be positive.")
            return None
        elif n > self.stock:
            print(f"[ERROR] Only {self.stock} cars available.")
            return None
        else:
            now = datetime.now()
            self.stock -= n
            print(f"[INFO] Rented {n} car(s) on hourly basis at {now.hour}:{now.minute}.")
            return now

    def rent_daily(self, n):
        if n <= 0:
            print("[ERROR] Number of cars should be positive.")
            return None
        elif n > self.stock:
            print(f"[ERROR] Only {self.stock} cars available.")
            return None
        else:
            now = datetime.now()
            self.stock -= n
            print(f"[INFO] Rented {n} car(s) on daily basis at {now.date()}.")
            return now

    def rent_weekly(self, n):
        if n <= 0:
            print("[ERROR] Number of cars should be positive.")
            return None
        elif n > self.stock:
            print(f"[ERROR] Only {self.stock} cars available.")
            return None
        else:
            now = datetime.now()
            self.stock -= n
            print(f"[INFO] Rented {n} car(s) on weekly basis at {now.date()}.")
            return now

    def return_car(self, request):
        rental_time, rental_basis, num_cars = request
        if rental_time and rental_basis and num_cars:
            self.stock += num_cars
            now = datetime.now()
            rental_period = now - rental_time

            if rental_basis == 1:  # hourly
                bill = round(rental_period.total_seconds() / 3600) * 5 * num_cars
            elif rental_basis == 2:  # daily
                bill = rental_period.days * 20 * num_cars
            elif rental_basis == 3:  # weekly
                bill = (rental_period.days // 7) * 60 * num_cars

            print(f"[INFO] Rental bill: ${bill}")
            return bill
        else:
            print("[ERROR] Invalid return request.")
            return None

class Customer:
    def __init__(self):
        self.cars = 0
        self.rental_basis = 0
        self.rental_time = None

    def request_car(self):
        try:
            cars = int(input("How many cars would you like to rent? "))
        except ValueError:
            print("[ERROR] Please enter a valid number.")
            return -1
        if cars < 1:
            print("[ERROR] Number of cars should be greater than zero.")
            return -1
        self.cars = cars
        return self.cars

    def return_car(self):
        if self.rental_time and self.rental_basis and self.cars:
            return self.rental_time, self.rental_basis, self.cars
        else:
            return 0, 0, 0


from car_one import CarRental, Customer

def main():
    shop = CarRental(20)
    customer = Customer()

    while True:
        print("""
        ====== CAR RENTAL SHOP ======
        1. Display available cars
        2. Rent a car on hourly basis ($5/hour)
        3. Rent a car on daily basis ($20/day)
        4. Rent a car on weekly basis ($60/week)
        5. Return a car
        6. Exit
        """)
        choice = input("Enter your choice: ")

        if choice == '1':
            shop.display_stock()

        elif choice == '2':
            customer_request = customer.request_car()
            if customer_request > 0:
                customer.rental_time = shop.rent_hourly(customer_request)
                customer.rental_basis = 1

        elif choice == '3':
            customer_request = customer.request_car()
            if customer_request > 0:
                customer.rental_time = shop.rent_daily(customer_request)
                customer.rental_basis = 2

        elif choice == '4':
            customer_request = customer.request_car()
            if customer_request > 0:
                customer.rental_time = shop.rent_weekly(customer_request)
                customer.rental_basis = 3

        elif choice == '5':
            request = customer.return_car()
            shop.return_car(request)
            # Reset customer data
            customer.rental_basis, customer.rental_time, customer.cars = 0, None, 0

        elif choice == '6':
            print("Thank you for using the Car Rental System. Goodbye!")
            break

        else:
            print("[ERROR] Invalid input. Please choose a valid option.")

if __name__ == "__main__":
    main()
