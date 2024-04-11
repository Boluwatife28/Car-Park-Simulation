import datetime as dt
import csv
import os

#create tables for the records
def Create_tables():
    CarPark_table= 'CarPark_records.csv'
# check if table already exists
    if not os.path.isfile(CarPark_table):
        #create a new csv file
        with open('CarPark_records.csv', mode='w', newline='') as csv_file:
            #create a CSV writer
            writer=csv.writer(csv_file) 

            #write data into the csv file
            writer.writerow(['VehicleRegistrationNumber', 'ParkingSpaceID', 'TicketNumber', 'EntryTime', 'ExitTime', 'ParkingFee'])
            csv_file.close()

    
    ParkingSpots_table= 'ParkingSpots_records.csv'
    # check if table already exists
    if not os.path.isfile(ParkingSpots_table):
         #create a new csv file
        with open('ParkingSpots_records.csv', mode='w', newline='') as csv_file:
            #create a CSV writer
            writer=csv.writer(csv_file) 

            #write data into the csv file
            writer.writerow(['ParkingSpotID', 'isEmpty'])
            #populate the database with parking spot ID
            for i in range(1, 9):
                ParkingSpotID= 'PS' + str(i)
                writer.writerow([ParkingSpotID, 'TRUE'])
            csv_file.close()

    else:
        return
    
#assign parking spot
def assign_parking_spot():
    #open the file in read and write mode
    with open('ParkingSpots_records.csv',mode='r') as csv_file:
        #read the CSV file into a list
        rows = list(csv.reader(csv_file))

        for i, row in enumerate(rows):
            #check if isEmpty is true
            if row[1] == 'TRUE':
                parkingID = row[0]
                #updating isEmpty to false when occupied
                rows[i] = [parkingID] + ["FALSE"]
                break
    #update the csv file 
    with open('ParkingSpots_records.csv',mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)

        
            
        csv_file.close()
    return parkingID
#return pasrking spot when a car exits   
def return_parking_spot(parking_ID):
    with open('ParkingSpots_records.csv',mode='r') as csv_file:
        #read the CSV file into a list
        rows = list(csv.reader(csv_file))
        for i, row in enumerate(rows):
            if row[0]== parking_ID:
                row[1]= 'TRUE'
                rows[i] = [parking_ID] + ['TRUE']
                
                csv_file.close()
                break

    with open('ParkingSpots_records.csv',mode='w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(rows)
    return True
#get available parking spots           
def available_parking_spots():
    #open the file in read mode
    with open('ParkingSpots_records.csv',mode='r') as csv_file:

        reader=csv.reader(csv_file, delimiter=',')
        #get the amount of unoccupied spaces
        count=0
        for row in reader:
            if row[1]== 'TRUE':
                count+=1
        csv_file.close()
    return count
#calculate parking fee
def calculate_parking_fee(entryTime, exitTime):
    #calculate the the time difference
    
    time_diff = exitTime - dt.datetime.strptime(entryTime, '%Y-%m-%d %H:%M:%S.%f')

    #convert time spent to hours
    hours_spent = time_diff.total_seconds()/3600

    #calculate parking fee
    parking_fee = 2 * hours_spent
    return parking_fee
  


#create the class Carpark
class CarPark:
    def __init__(self):
        self.vehicle_regno=None
        self.ticket_no=None
        self.parking_ID=None
        self.parking_spots=8
        self.parking_fee=None

    def Enter_CarPark(self, vehicle_regno):
        self.vehicle_regno=vehicle_regno
        #getting the entry time
        entry_time=dt.datetime.now()
        #generate ticket number
        self.ticket_no='DST' +str(vehicle_regno)
        #assign parking ID
        self.parking_ID= assign_parking_spot()
        #open csv file as append mode
        with open('CarPark_records.csv',mode='a', newline='') as csv_file:
            writer=csv.writer(csv_file, delimiter=',')
            #adding a new record to the csv
            writer.writerow([self.vehicle_regno, self.parking_ID, self.ticket_no, entry_time, '', ''])
            csv_file.close()
        return True 


    def Exit_CarPark(self, vehicle_regno):
        self.vehicle_regno=vehicle_regno
         #open the file in read mode
        with open('CarPark_records.csv',mode='r') as csv_file:
            rows = list(csv.reader(csv_file))
         #search for row that matches vehicle regno
            for i, row in enumerate(rows):
                if row[0] == vehicle_regno:
                    ParkingSpaceId = row[1]
                    ticketNo = row[2]
                    entrytime = row[3]
                    exittime = dt.datetime.now()
                    parkingfee = calculate_parking_fee(entrytime, exittime)
                    self.parking_fee = parkingfee
                    rows[i] = [vehicle_regno, ParkingSpaceId, ticketNo, entrytime, exittime, parkingfee]
                    self.parking_ID = ParkingSpaceId
                    csv_file.close()
            #call the return parking spot function
                    return_parking_spot(ParkingSpaceId)
                else:
                    False
            #update the csv file
            with open('CarPark_records.csv',mode='w', newline='') as csv_file:
                writer=csv.writer(csv_file, delimiter=',')
                writer.writerows(rows)
            return True
    
    def Query_Parkingrecord(self, ticketNumber):
        #open the file in read mode
        with open('CarPark_records.csv',mode='r') as csv_file:
            reader=csv.reader(csv_file, delimiter=',')
            #search for row that matches ticket nummber
            for row in reader:
                if ticketNumber == row[2]:
                    return list(row)
                