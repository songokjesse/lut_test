from datetime import datetime, date


def available_car_for_rental(registration):
    """
    A function that gets and returns the availability of a car
    :return:
    """

    # Read the  Vehicle.txt file
    vehicles = open('project_files/Vehicles.txt', 'r')
    # Read the  RentedVehicle.txt file
    rented_vehicles = open('project_files/rentedVehicles.txt', 'r')
    # Loop through both files and find and append cars that have not been rented
    for car in vehicles:
        for rented_car in rented_vehicles:
            if car.split(',')[0] != rented_car.split(',')[0] and car.split(',')[0] == registration:
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
    today = date.today()
    return today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))



def list_available_cars():
    """
    A function that prints to screen a list of cars that are available for renting
    :return:
    """
    # Read the Vehicle.txt file
    vehicles = open('project_files/Vehicles.txt', 'r')
    rented_vehicles = open('project_files/rentedVehicles.txt', 'r')

    # loop through the rows and check if the car is not already rented and print on screen
    print("The following cars are available:")
    for car in vehicles:
        for rented_car in rented_vehicles:
            if car.split(',')[0] != rented_car.split(',')[0]:
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
            # Prompt user to enter car car_registration
            car_registration = input("Enter Registration Number for the car you want to Rent: ")
            # Check if car exist for rental
            car_is_available = available_car_for_rental(car_registration)
            if car_is_available:
                customers_birthday = input("What is your Birthday? (DD/MM/YYYY) : ")
                if validate_date(customers_birthday):
                    age = get_age(customers_birthday)
                    # if age < 100 and age >=18
                else:
                    print("Invalid Birthday Date")
            else:
                print("Car is not Available for Rental")
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
