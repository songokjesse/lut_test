import re
from datetime import datetime, date
from collections import Counter


def available_car_for_rental(registration):
    """
    A function that gets and returns the availability of a car
    :return:
    """
    available_car_registration = get_difference_in_list()
    if registration in available_car_registration:
        return True

    return False


def validate_date(date_input):
    """
    A function that validate the date entered by user
    :param date_input:
    :return:
    """
    try:
        result = bool(datetime.strptime(date_input, '%d/%m/%Y'))
    except ValueError:
        result = False
    return result


def get_age(birthdate):
    """
    A function that calculates the Age from Birthday Provided by User
    :param birthdate:
    :return:
    """
    # Get today's date object
    today = date.today()
    cage = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))

    return cage


def validate_email(email):
    """
    A function that validate email addresses entered by the user
    :param email:
    :return:
    """
    # regex
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    if re.fullmatch(regex, email):
        return True
    return False


def check_if_customer_exist(email):
    """
    A function that checks if a user exists on the Customer.txt file
    :param email:
    :return:
    """
    # Read Customer file
    customer = open('project_files/Customers.txt', 'r')

    # loop and find individual email
    for user in customer:
        if user.split(',')[3] == email:
            return True
    return False


def add_new_customer(customer):
    """
    A function that adds a new customer to Customer.txt file
    :param customer:
    :return:
    """
    customer_file = open("project_files/Customers.txt", "a")
    customer_file.write(customer)
    customer_file.close()


def add_rental_details(customer):
    """
    A function that adds user details to RentedVehicles.txt
    :param customer:
    :return:
    """
    details = customer + "\n"
    f = open("project_files/rentedVehicles.txt", "a")
    f.write(details)
    f.close()


def get_difference_in_list():
    """
    A function that reads two files and find the differences
    :return:
    """

    # Declare emtpy arrays/lists
    cars = get_car_registration_list()
    rented_cars = get_rented_vehicle()

    # get the difference between the cars using the Counter library
    c1 = Counter(cars)
    c2 = Counter(rented_cars)
    diff = list((c1 - c2).elements())
    return diff


def list_available_cars():
    """
    A function that prints to screen a list of cars that are available for renting
    :return:
    """
    # read the vehicles file
    vehicles = open('project_files/Vehicles.txt', 'r')
    # get the list of available cars reg numbers
    reg_cars_available = get_difference_in_list()

    # loop through the vehicles file and
    # compare to the reg numbers of cars available for rent to create
    # the final print statement
    print("The following cars are available: ")
    for car in vehicles:
        for reg in reg_cars_available:
            if reg in car:
                Reg = car.split(',')[0]
                Model = car.split(',')[1]
                Price = car.split(',')[2]
                Properties = car.split(',')[3]

                print(
                    "Reg. nr: {} , Model: {}, Price per day: {}, Properties: {}".format(Reg, Model, Price, Properties))


def get_rented_vehicle():
    """
    A function that returns the registration numbers of cars that have been rented
    :return:
    """
    rented_cars = []
    rented_vehicles = open('project_files/rentedVehicles.txt', 'r')
    for rented_car in rented_vehicles:
        rented_cars.append(rented_car.split(',')[0])

    return rented_cars


def get_car_registration_list():
    cars = []
    # Read the Vehicle.txt file
    vehicles = open('project_files/Vehicles.txt', 'r')

    # loop through the rows and append to the list declared above
    for car in vehicles:
        cars.append(car.split(',')[0])
    return cars


def check_for_rented_car(registration):
    """
    A function that checks if a car has already been rented
    :param registration:
    :return:
    """
    rented_cars = get_rented_vehicle()
    if registration in rented_cars:
        return True
    return False


def calculate_rent_amount(registration):
    # get rental date and price per day
    # Read the Vehicle.txt file
    global start_date
    date_today = datetime.today()
    price = 0
    birthday = ""
    vehicles = open('project_files/Vehicles.txt', 'r')
    rentedVehicle = open('project_files/rentedVehicles.txt', 'r')

    # loop through the rows and append to the list declared above
    for car in vehicles:
        if registration in car:
            price = car.split(',')[2]
    for rent_car in rentedVehicle:
        if registration in rent_car:
            start_date = rent_car.split(',')[2]
            birthday = rent_car.split(',')[1]
    # Get the days from date
    rent_stop_date = date_today.date()
    stop_date = datetime.now()
    rental_start_date = datetime.strptime(start_date.strip(), "%d/%m/%Y %H:%M").date()
    rental_days = (rent_stop_date - rental_start_date).days
    # calculate the amount
    rental_amount = int(rental_days) * int(price)
    return [rental_days, float(rental_amount), start_date.strip(), stop_date.strftime("%d/%m/%Y %H:%M"), birthday]


def remove_transaction_from_line(registration):
    """
    A function that deletes a line with a specific registration number
    :param registration:
    :return:
    """
    with open("project_files/rentedVehicles.txt", 'r') as file:
        lines = file.readlines()

    # delete matching content
    with open("project_files/rentedVehicles.txt", 'w') as file:
        for line in lines:
            # find() returns -1 if no match is found
            if line.find(registration) != -1:
                pass
            else:
                file.write(line)


def write_to_transaction_file(rent_amount, registration):
    f = open("project_files/transActions.txt", "a")
    # stop_date =
    details = registration + "," + str(rent_amount[4]) + "," + str(rent_amount[2]) + "," + str(
        rent_amount[3]) + "," + str(rent_amount[0]) + "," + format(amount[1], ".2f") + "\n"
    f.write(details)
    f.close()


def calculate_total_transactions():
    total_rental_amount = 0
    transactions = open('project_files/transActions.txt', 'r')
    for cost in transactions:
        total_rental_amount = total_rental_amount + float(cost.split(',')[5])

    return total_rental_amount


if __name__ == "__main__":

    selection_prompt = None

    # always run until user exits using 0
    while selection_prompt != 0:
        selection_prompt = int(input(
            '''
            You may select one of the following
             1) List available cars
             2) Rent a car
             3) Return a car
             4) Count the money
             0) Exit
             What is your selection?: 
            '''))
        if selection_prompt == 1:
            # get the list of cars that are available for rent
            list_available_cars()
            # continue running the program
            continue
        elif selection_prompt == 2:
            # Prompt user to enter car registration
            car_registration = input("Enter Registration Number for the car you want to Rent: ")
            # Check if car exist for rental
            car_is_available = available_car_for_rental(car_registration)
            if car_is_available:
                customers_birthday = input("What is your Birthday? (DD/MM/YYYY) : ")
                if validate_date(customers_birthday):

                    # calculate the customers age
                    age = get_age(datetime.strptime(customers_birthday, '%d/%m/%Y'))

                    # Check if the customer is allowed to rent a car by age
                    if 100 > age >= 18:

                        # Prompt the user for User Details (Firstname, Lastname, Email)
                        customer_first_name = input("What is your First Name: ")
                        customer_last_name = input("What is your Last Name: ")
                        customer_email = input("What is your Email Address: ")

                        # Check if the customer provided a valid email
                        if validate_email(customer_email):
                            # Check if user exist
                            if check_if_customer_exist(customer_email):
                                # if it exists do nothing
                                pass
                            else:
                                # Insert Customer Details
                                customer_details = customers_birthday + "," + customer_first_name + "," + customer_last_name + "," + customer_email
                                add_new_customer(customer_details)
                        else:
                            print("Invalid Email")
                        now = datetime.now()  # current date and time
                        # Add Details to Rented Vehicles
                        rental_details = car_registration + "," + customers_birthday + "," + now.strftime(
                            "%d/%m/%Y %H:%M")
                        add_rental_details(rental_details)

                        print("Hi {} You rented the car {}".format(customer_first_name, car_registration))

                    else:
                        print("Your Age Limit is not Authorised to Rent")
                else:
                    print("Invalid Birthday Date")
            else:
                print("Invalid Registration or Car is not Available for Rental")
            continue
        elif selection_prompt == 3:
            # Prompt user to enter car registration
            rented_car_registration = input("Enter Registration Number for the Rented Car: ")
            if check_for_rented_car(rented_car_registration):
                # calculate the rental days & amount and return their values in an array
                amount = calculate_rent_amount(rented_car_registration)
                # Add the rental details to the transaction file
                write_to_transaction_file(amount, rented_car_registration)
                # remove the rental details after car has been returned
                remove_transaction_from_line(rented_car_registration)
                # display message
                print("The rent lasted {} days and the cost is {} euros".format(amount[0], format(amount[1], ".2f")))

            else:
                print("Car has not been rented Out")
            continue
        elif selection_prompt == 4:
            total_amount = calculate_total_transactions()
            print("The total amount of money is {} euros".format(total_amount))
            continue
        elif selection_prompt == 0:
            break
        else:
            print("Invalid Entry: Kindly choose any options number between 1 to 4 ")
            continue
