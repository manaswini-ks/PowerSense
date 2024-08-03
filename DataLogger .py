import serial
import csv
from datetime import datetime

ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with the appropriate serial port
csv_file = open('sensor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

index = 0

while True:
    line = ser.readline().decode().strip()  # Read a line from serial and decode it
    if line:
        # Parse the data from Arduino; adjust the split as needed
        # Assuming the format from Arduino is: device,current,voltage,...
        data = line.split(',')
        
        # Generate date and time
        now = datetime.now()
        date_str = now.strftime('%m/%d/%Y')
        time_str = now.strftime('%H:%M:%S')
        
        # Write data to CSV in the desired format
        # Assuming the Arduino sends enough data to fit the columns
        csv_writer.writerow([
            *data  # Unpack the data list directly
        ])
        
        print(f"Logged: {index}, {date_str}, {time_str}, {', '.join(data)}")
        
        index += 1

csv_file.close()
ser.close()

# import serial
# import csv

# ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate serial port
# csv_file = open('data.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)
# csv_writer.writerow(['Device', 'Current (A)', 'Voltage (V)'])

# while True:
#     line = ser.readline().decode().strip()  # Read a line from serial and decode it
#     if line:
#         device, current, voltage = line.split(',')
#         csv_writer.writerow([device, current, voltage])
#         print(f"Logged: {line}")

# csv_file.close()
# ser.close()
