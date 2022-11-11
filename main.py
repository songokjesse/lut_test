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
    pass


def get_difference_in_list():
    """
    A function that reads two files and find the differences
    :return:
    """

    # Declare emtpy arrays/lists
    cars = []
    rented_cars = []
    # Read the Vehicle.txt file
    vehicles = open('project_files/Vehicles.txt', 'r')
    rented_vehicles = open('project_files/rentedVehicles.txt', 'r')

    # loop through the rows and append to the list declared above
    for car in vehicles:
        cars.append(car.split(',')[0])
    for rented_car in rented_vehicles:
        rented_cars.append(rented_car.split(',')[0])

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
    for car in vehicles:
        for reg in reg_cars_available:
            if reg in car:
                Reg = car.split(',')[0]
                Model = car.split(',')[1]
                Price = car.split(',')[2]
                Properties = car.split(',')[3]
                print(
                    "Reg. nr: {} , Model: {}, Price per day: {}, Properties: {}".format(Reg, Model, Price, Properties))


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

                        # Add Details to Rented Vehicles
                        rental_details = car_registration + "," + customers_birthday + "," + str(datetime.now(tz=None))
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
            print(selection_prompt)
            continue
        elif selection_prompt == 4:
            print(selection_prompt)
            continue
        elif selection_prompt == 0:
            break
        else:
            print("Invalid Entry: Kindly choose any options number between 1 to 4 ")
            continue
