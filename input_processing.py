# input_processing.py
# Daniel O. Ikponmwen, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.


# Sensor class to represent the status of traffic light, pedestrian, and vehicle.
class Sensor:

    # Constructor that uses default values
       def __init__(self, traffic_light="green", pedestrian= "no", vehicle="no"):
        self.traffic_light = traffic_light
        self.pedestrian = pedestrian
        self. vehicle = vehicle
        

    # This function prompts the user for input and continuously updates the sensor status 
    # based on user input until the program is terminated.
    # Parameters: sensor (Sensor): The sensor object to be updated
def update_status(sensor): 
    while True: #While loop to make sure the code continues to run until terminated by entering 0
        try: # This is a try block to catch exceptions, the error mesage is printed wih the except block
            status = input ("Are changes detected in the vision input?\n"
                "Select 1 for traffic light, 2 for pedestrian, 3 for vehicle or 0 to end the program -->")
            if status not in ["0", "1", "2", "3"]: # checks if user entered 1,2,3 or 0
                        raise ValueError("You must select 1, 2, 3 or 0") #raises ValueError if input is not 1,2,3,0
                        continue
            status = int (status) # converts string input to an integer
                     
            if(status == 0 ): #checks if user selected option O, then prints that it is exiting and exits the program
                print("\nExiting the program, Goodbye!\n")
                break
            if (status == 1): #checks if user selected option 1, then prompts for more input
                status_light = input("What change has been identified?\n"
                        "select 'green', 'yellow' or 'red'--> ")
                if status_light not in ["green", "yellow", "red"]:  #checks if input is green, yellow or red
                    raise ValueError("Invalid vision input") #raises ValueError exception is not as specified in previous line
                    continue
                sensor.traffic_light = status_light #updates traffic light status
                
                    
            elif (status == 2):  #checks if user selected option 2, then prompts for more input
                status_pedestrian = input("What change has been identified?\n"
                        "select 'yes' if there is a pedestrian and 'no' if there is no pedestrian -->").lower()
                if status_pedestrian not in ["yes", "no",]:   #checks if input is yes or no
                    raise ValueError("Invalid vision input")  #raises ValueError exception if input is not yes or no
                    continue
                sensor.pedestrian = status_pedestrian #updates pedestrian status
                

            elif (status == 3):  #checks if option 3 for vehicle is selected, then prompts for more input
                status_vehicle = input("What change has been identified?\n"
                        "select 'yes' if there is a vehicle and 'no' if there is no vehicle --> ").lower()
                if status_vehicle not in ["yes", "no",]:  #checks if the input is 'yes' or 'no'
                    raise ValueError("Invalid vision input") #raises an exception error if input is not yes or no
                    continue
                sensor.vehicle = status_vehicle #updates vehicle status

            print_message(sensor)
                             
        except ValueError as e:
            print(f"\n {e} \n") # prints out the ValueError Exception message when there is an invalid input
                 




# Prints an action message based on the sensor's status and also prints the current sensor'status
# Parameters:sensor (Sensor): The sensor object with attributes traffic_light, pedestrian, and vehicle.

def print_message(sensor):
# checks if traffic light is red or pedestrian is yes, vehicle is yes and prints STOP
    if sensor.traffic_light == "red" or sensor.pedestrian =="yes" or sensor.vehicle=="yes" :
        print("\nSTOP\n")
        print (f"Light = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian},\
           Vehicle = {sensor.vehicle}\n")
        
# checks if traffic light is green, no pedestrian, no vehicle and prints "Proceed"
    elif sensor.traffic_light == "green" and sensor.pedestrian == "no" and sensor.vehicle =="no":
        print ("\nProceed\n")
        print (f"Light = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian},\
           Vehicle = {sensor.vehicle}\n")
        
# checks if traffic light is yellow with no pedestrian, no vehicle and prints "Caution"
    elif sensor.traffic_light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle =="no":
        print ("\nCaution\n")
        print (f"Light = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian},\
           Vehicle = {sensor.vehicle}\n") 
       
    


# The main function to run the car vision detector processing program.
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    update_status(sensor)
 





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

