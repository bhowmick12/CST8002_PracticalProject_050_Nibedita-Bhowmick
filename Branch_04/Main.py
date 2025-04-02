import pandas as pd
import matplotlib.pyplot as plt
import os



# Main Program Execution
if __name__ == "__main__":


    # file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test01.csv"
    file_path = "C:\\Licensed_Early_Learning_and_Childcare_Facilities.csv"
    # file_path = "C:\\Users\\Nibedita\\OneDrive - Algonquin College\\Documents\\Test_03.csv"
    try:
        model = CSVModel(file_path)
        view = CSVView()
        controller = CSVController(model, view)
        controller.run()
    except FileNotFoundError as e:
        print(e)
