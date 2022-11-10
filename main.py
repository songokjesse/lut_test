def list_available_cars():
    # variable declaration
    available_vehicles_list = []
    # Read the Vehicle.txt file
    vehicles = open('project_files/Vehicles.txt', 'r')
    rented_vehicles = open('project_files/rentedVehicles.txt', 'r')

    # loop through the rows and check if the car is not already rented
    print('---------------------------------------------------------------------------')
    print("Available Cars for Rental")
    print('---------------------------------------------------------------------------')
    for car in vehicles:
        for rented_car in rented_vehicles:
            if car.split(',')[0] != rented_car.split(',')[0]:
                print(car)
    print('---------------------------------------------------------------------------')


if __name__ == "__main__":

    selection_prompt = None

    # always run until user exits loop using 0
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
            list_available_cars()
            continue
        elif selection_prompt == 2:
            print(selection_prompt)
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
