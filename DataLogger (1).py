import serial
import csv

ser = serial.Serial('COM3', 9600)  # Replace 'COM3' with the appropriate serial port
csv_file = open('data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(['Device', 'Current (A)', 'Voltage (V)'])

while True:
    line = ser.readline().decode().strip()  # Read a line from serial and decode it
    if line:
        device, current, voltage = line.split(',')
        csv_writer.writerow([device, current, voltage])
        print(f"Logged: {line}")

csv_file.close()
ser.close()
