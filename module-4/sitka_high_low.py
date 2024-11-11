#Amanda New
#CSD325-A311
#Module 4.2 Assignment
#High/Low Temperatures

#Introduction, instructions, and user input
def userInput():

    print("Welcome to the Sitka Temperature Data!")
    print("Select an option:")
    print("  (H)ighs")
    print("  (L)ows")
    print("  (E)xit")
    return input("Enter your choice (H/L/E): ") 

#main function
def main ():

    import csv
    from datetime import datetime

    from matplotlib import pyplot as plt


    filename = 'sitka_weather_2018_simple.csv'
    with open(filename) as f:
        reader = csv.reader(f)

        # Get dates and high temperatures from this file.
        #*** Edited to include lows***
        dates, highs, lows = [], [], []
        for row in reader:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            dates.append(current_date)
            high = int(row[5])
            highs.append(high)
            low = int(row[6])
            lows.append(low)

        #elif H/L/E to print and plot Highs and Lows, and exit system if user selects 'E'
        while True:
            choice = userInput()
            
            if choice == "H":

            # Plot the high temperatures.
            #plt.style.use('seaborn')
                fig, ax = plt.subplots()
                ax.plot(dates, highs, c='red')

                # Format plot.
                plt.title("Daily high temperatures - 2018", fontsize=24)
                plt.xlabel('', fontsize=16)
                fig.autofmt_xdate()
                plt.ylabel("Temperature (F)", fontsize=16)
                plt.tick_params(axis='both', which='major', labelsize=16)

                plt.show()

            elif choice == "L":

                #Plot the low temperature
                #plt.style.use('seaborn')
                fig, ax = plt.subplots()
                ax.plot(dates, lows, c='blue')

                # Format plot.
                plt.title("Daily low temperatures - 2018", fontsize=24)
                plt.xlabel('', fontsize=16)
                fig.autofmt_xdate()
                plt.ylabel("Temperature (F)", fontsize=16)
                plt.tick_params(axis='both', which='major', labelsize=16)

                plt.show()

            elif choice == "E":
                print("Exiting program...")
                break

            else:
                print(choice)
                print(len(choice))
                print("Invalid choice. Please refer to instructions and select H, L, or E. Try again!")

main()