import serial
import csv
from datetime import datetime
import time
import firebase_admin
from firebase_admin import credentials, storage

# Initialize Firebase
cred = credentials.Certificate(r'C:\Users\Lekhana\OneDrive\Attachments\Desktop\college\IOT_EL\key.json')  # Use the correct path to your Firebase JSON key file
firebase_admin.initialize_app(cred, {
    'storageBucket': 'power-sense-81863.appspot.com'  # Replace with your Firebase Storage bucket name
})
bucket = storage.bucket()  # Reference to the storage bucket

# Open the serial port
ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with the appropriate serial port

# Open the CSV file for writing
csv_file = open('sensor_data.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

# Write the header to the CSV file
csv_writer.writerow(['Index', 'Date', 'Time', 'Device', 'Current', 'Voltage'])  # Add more headers as needed

index = 0
upload_interval = 60  # Interval in seconds for uploading the CSV file
last_upload_time = time.time()

try:
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
            csv_writer.writerow([
                index,  # Index
                date_str,  # Date
                time_str,  # Time
                *data  # Unpack the data list directly
            ])
            
            print(f"Logged: {index}, {date_str}, {time_str}, {', '.join(data)}")
            
            index += 1
        
        # Check if it's time to upload the CSV file
        current_time = time.time()
        if current_time - last_upload_time >= upload_interval:
            csv_file.flush()  # Ensure all data is written to the file
            blob = bucket.blob('sensor_data.csv')  # Set the file path in the storage bucket
            blob.upload_from_filename('sensor_data.csv')
            print("CSV file uploaded to Firebase Storage.")
            last_upload_time = current_time

except KeyboardInterrupt:
    # Handle script interruption (e.g., Ctrl+C) gracefully
    print("Data logging stopped.")

finally:
    # Ensure resources are cleaned up properly
    csv_file.close()
    ser.close()
    
    # Final upload CSV file to Firebase Storage
    blob = bucket.blob('sensor_data.csv')  # Set the file path in the storage bucket
    blob.upload_from_filename('sensor_data.csv')
    print("CSV file uploaded to Firebase Storage.")



# import serial
# import csv
# from datetime import datetime
# import firebase_admin
# from firebase_admin import credentials, firestore

# # Initialize Firebase
# cred = credentials.Certificate(r'C:\Users\Lekhana\OneDrive\Attachments\Desktop\college\IOT_EL\key.json.json')  # Replace with your Firebase key file
# firebase_admin.initialize_app(cred)
# db = firestore.client()

# ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with the appropriate serial port
# csv_file = open('sensor_data.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)

# index = 0

# while True:
#     line = ser.readline().decode().strip()  # Read a line from serial and decode it
#     if line:
#         # Parse the data from Arduino; adjust the split as needed
#         # Assuming the format from Arduino is: device,current,voltage,...
#         data = line.split(',')
        
#         # Generate date and time
#         now = datetime.now()
#         date_str = now.strftime('%m/%d/%Y')
#         time_str = now.strftime('%H:%M:%S')
        
#         # Write data to CSV in the desired format
#         # Assuming the Arduino sends enough data to fit the columns
#         csv_writer.writerow([
#             *data  # Unpack the data list directly
#         ])
        
#         print(f"Logged: {index}, {date_str}, {time_str}, {', '.join(data)}")
        
#         # Prepare data for Firebase
#         data_dict = {
#             'data': data
#         }
        
#         # Upload to Firebase
#         db.collection('sensor_data').add(data_dict)
        
#         index += 1

# csv_file.close()
# ser.close()




# import serial
# import csv
# from datetime import datetime

# ser = serial.Serial('COM4', 9600)  # Replace 'COM4' with the appropriate serial port
# csv_file = open('sensor_data.csv', 'w', newline='')
# csv_writer = csv.writer(csv_file)

# index = 0

# while True:
#     line = ser.readline().decode().strip()  # Read a line from serial and decode it
#     if line:
#         # Parse the data from Arduino; adjust the split as needed
#         # Assuming the format from Arduino is: device,current,voltage,...
#         data = line.split(',')
        
#         # Generate date and time
#         now = datetime.now()
#         date_str = now.strftime('%m/%d/%Y')
#         time_str = now.strftime('%H:%M:%S')
        
#         # Write data to CSV in the desired format
#         # Assuming the Arduino sends enough data to fit the columns
#         csv_writer.writerow([
#             *data  # Unpack the data list directly
#         ])
        
#         print(f"Logged: {index}, {date_str}, {time_str}, {', '.join(data)}")
        
#         index += 1

# csv_file.close()
# ser.close()
