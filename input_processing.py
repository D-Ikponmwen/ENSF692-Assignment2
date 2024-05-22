# input_processing.py
# Daniel O. Ikponmwen, ENSF 692 P24
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
        

    # Replace these comments with your function commenting
def update_status(sensor): # You may decide how to implement the arguments for this function
    while True:
        try:
            status = input ("Are changes detected in the vision input?\n"
                "Select 1 for traffic light, 2 for pedestrian, 3 for vehicle or 0 to end the program -->")
            if status not in ["0", "1", "2", "3"]:
                        raise ValueError("You must select 1, 2, 3 or 0")
                        continue
            status = int (status)
                     
            if(status == 0 ):
                print("\nExiting the program, Goodbye!\n")
                break
            if (status == 1):
                status_light = input("What change has been identified?\n"
                        "select 'green', 'yellow' or 'red'--> ")
                if status_light not in ["green", "yellow", "red"]:
                    raise ValueError("Invalid vision input")
                    continue
                sensor.traffic_light = status_light
                
                    
            elif (status == 2):
                status_pedestrian = input("What change has been identified?\n"
                        "select 'yes' if there is a pedestrian and 'no' if there is no pedestrian -->").lower()
                if status_pedestrian not in ["yes", "no",]:
                    raise ValueError("Invalid vision input")
                    continue
                sensor.pedestrian = status_pedestrian
                

            elif (status == 3):
                status_vehicle = input("What change has been identified?\n"
                        "select 'yes' if there is a vehicle and 'no' if there is no vehicle --> ").lower()
                if status_vehicle not in ["yes", "no",]:
                    raise ValueError("Invalid vision input")
                    continue
                sensor.vehicle = status_vehicle

            print_message(sensor)
                    
                    #print ("vehicle is {status_vehicle}")
            # else:
            #     if status not in ["1","2","3","0"]:
            #         raise ValueError("Invalid answer. You must select 1, 2, 3 or 0")
            #         continue
            # #         #status_error = print ("you must select 1, 2, 3 or 0")
            # #         break
           
        except ValueError as e:
            print(f"\n {e} \n") 
                 
         


       




# The sensor object should be passed to this function to print the action message and current status
# Replace these comments with your function commenting
def print_message(sensor):
    if sensor.traffic_light == "red" or sensor.pedestrian =="yes" or sensor.vehicle=="yes" :
        print("\nSTOP\n")
        print (f"Light = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian},\
           Vehicle = {sensor.vehicle}\n")
        

    elif sensor.traffic_light == "green" and sensor.pedestrian == "no" and sensor.vehicle =="no":
        print ("\nProceed\n")
        print (f"Light = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian},\
           Vehicle = {sensor.vehicle}\n")
        
        
    elif sensor.traffic_light == "yellow" and sensor.pedestrian == "no" and sensor.vehicle =="no":
        print ("\nCaution\n")
        print (f"Light = {sensor.traffic_light}, Pedestrian = {sensor.pedestrian},\
           Vehicle = {sensor.vehicle}\n") 
       
    


# Complete the main function below
def main():
    print("\n***ENSF 692 Car Vision Detector Processing Program***\n")
    sensor = Sensor()
    update_status(sensor)
 





# Conventional Python code for running main within a larger program
# No additional code should be included below this
if __name__ == '__main__':
    main()

