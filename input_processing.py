# input_processing.py
# YOUR NAME, ENSF 692 P24
# A terminal-based program for processing computer vision changes detected by a car.
# Detailed specifications are provided via the Assignment 2 README file.
# You must include the code provided below but you may delete the instructional comments.
# You may add your own additional classes, functions, variables, etc. as long as they do not contradict the requirements (i.e. no global variables, etc.). 
# You may import any modules from the standard Python library.
# Remember to include your name and comments.



# No global variables are permitted


# You do not need to provide additional commenting above this class, just the user-defined functions within the class
class Sensor:

    # Must include a constructor that uses default values
    # You do not need to provide commenting above the constructor
    def __init__(self, traffic_light="green", pedestrian= "no", vehicle="no"):
        self.traffic_light = traffic_light
        self.pedestrian = pedestrian
        self. vehicle = vehicle
        
# S1 = Sensor("green", "yes", "yes")
# print (S1.pedestrian)

    # Replace these comments with your function commenting
def update_status(sensor): # You may decide how to implement the arguments for this function
    while True:
        try:
            status = int(input ("Are changes detected in the vision input?\n"
                "Select 1 for traffic light, 2 for pedestrian, 3 for vehicle or 0 to end the program"))
            # if status not in [type(str)]:
            #             raise ValueError("Invalid menu option selected. You must select 1, 2, 3 or 0")
            #             continue          
            while (status != 0 ):
                if (status == 1):
                    status_light = input("What change has been identified?\n"
                        "select 'green', 'yellow' or 'red' ")
                    if status_light not in ["green", "yellow", "red"]:
                        raise ValueError("Invalid traffic light color")
                        continue
                    sensor.traffic_light = status_light
                    return sensor.traffic_light
                    #print ("light is {status_light}")
                    
                elif (status == 2):
                    status_pedestrian = input("What change has been identified?\n"
                        "select 'yes' if there is a pedestrian and 'no' if there is no pedestrian ")
                    if status_pedestrian.lower() not in ["yes", "no",]:
                        raise ValueError("Invalid answer")
                        continue
                    sensor.pedestrian = status_pedestrian
                    return sensor.pedestrian


                    #print ("pedestrian is {status_pedestrian}")

                elif (status == 3):
                    status_vehicle = input("What change has been identified?\n"
                        "select 'yes' if there is a vehicle and 'no' if there is no vehicle ")
                    if status_vehicle.lower() not in ["yes", "no",]:
                        raise ValueError("Invalid answer")
                        continue
                    sensor.vehicle = status_vehicle
                    return sensor.vehicle
                    
                    #print ("vehicle is {status_vehicle}")
                else:
                    if status not in ["1","2","3","0"]:
                        raise ValueError("Invalid answer. You must select 1, 2, 3 or 0")
                        continue
                    #status_error = print ("you must select 1, 2, 3 or 0")
                    break
            print("Exiting the program, Goodbye!")
            break
                
        except ValueError as e:
        #    print(type(e))
           print (f" Error: {e}. Please try again.")
       




# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if sensor.traffic_light == "red" or sensor.pedestrian =="yes" or sensor.vehicle=="yes" :
        return "STOP"
    elif sensor.traffic_light == "green":
        return "Proceed"
    elif sensor.traffic_light == "yellow":
        return "Caution"
    


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    update_status(sensor)
    action_message = print_message(sensor)
    print ("\n")
    print (action_message)
    print (f"Traffic Light color is: {sensor.traffic_light.capitalize()}")
    print (f"Pedestrian present: {sensor.pedestrian.capitalize()}")
    print (f"Vehicle present: {sensor.vehicle.capitalize()}")
   





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

