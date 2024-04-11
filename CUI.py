import Car_Park as cp
import re
cp.Create_tables()

#define menu options
def Menu():
    print('''Welcome to KEELE parking space.
            1. Enter Car Park.
            2. Exit Car Park.
            3. View Available Parking Spaces.
            4. Query Parking Record by Ticket Number.
            5. Quit. 
    ''')

while True:
    Menu()
    Menu_option=input('Kindly enter your option: ')
    current_user=cp.CarPark()
    if Menu_option == '1':
        VehicleRegNo=input('Kindly enter Vehicle Registration Number(e.g ABC123DE): ')
        #validate user's vehicle registration number
        RegNo_pattern= re.match(r'^[A-Z]{3}\d{3}[A-Z]{2}$', VehicleRegNo )
        if not RegNo_pattern:
            print('Invalid registration number. Kindly enter a valid registration number.')
        else:
            current_user.Enter_CarPark(VehicleRegNo)
            print('Your parking space ID is %s and your Ticket Number is %s' %(current_user.parking_ID, current_user.ticket_no))
            availableSpots=cp.available_parking_spots()
            print('Available parking spots: %s ' %(availableSpots))
    
        
    elif Menu_option == '2':
        VehicleRegNo=input('Kindly enter Vehicle Registration Number(e.g ABC123DE): ')
        vehicle_present=current_user.Exit_CarPark(VehicleRegNo)
        #validate user's entry
        if vehicle_present:

            print('Your Parking Fee is: £%0.3s' %(current_user.parking_fee))
            print('Availble Parking Space(s): %s' %(cp.available_parking_spots()))
            print('Parking space %s previously occupied is free'%(current_user.parking_ID))
            print('Thank you for parking with us!.')
        else:
            print('No vehicle with vehicle registration number provided! Kindly enter a valid vehicle registration number.')

        
        
    elif Menu_option == '3':
        AvailableSpots=cp.available_parking_spots()
        print('Available parking spot(s): %s' %(AvailableSpots))
        

    elif Menu_option == '4':
        ticketNumber=input('Kindly enter your ticket number: ')
        recordsList=current_user.Query_Parkingrecord(ticketNumber)
        #validate user's entry
        if not recordsList:
            print('No record found for %s. Kindly enter valid ticket number.' %(ticketNumber))
        else:
             print('''Your Vehicle Registration Number is :%s
                 Your Parking Space ID is: %s 
                 Your Ticket Number is : %s
                 Your Entry Time is: %s
                 Your Exit Time is: %s
                 Your Parking Fee is: %s
                 ''' %(recordsList[0], recordsList[1], recordsList[2], recordsList[3], recordsList[4], recordsList[5]))     
             
        
    elif Menu_option == '5':
        print('Thank you for using KEELE car park.')
    else:
        print('Invalid input. Kindly select from available options.')




