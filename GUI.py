import tkinter as tk
import Car_Park as cp
import re
current_user=cp.CarPark()

#to clear the previous widgets when another option is chosen
def DestroyWidgets():
    for widget in info_frm.winfo_children():
        widget.destroy()
#function for 'enter car park' button
def EnterCarPark():
    DestroyWidgets()
    #create widget to enter car park
    vrn_lbl1=tk.Label(master=info_frm, text='Enter Car Park.')
    vrn_lbl1.grid(row=2, column=1, sticky='nsew')
    vrn_lbl=tk.Label(master=info_frm, text='Kindly enter your Vehicle Registration Number e.g ABC123DE:')
    vrn_lbl.grid(row=3, column=1, sticky='nsew')
    vrn_ent=tk.Entry(master=info_frm, width=25)
    vrn_ent.grid(row=4, column=1, sticky='nsew')
    def enter_vrn():
        #get the vehicle registration number from the entry widget
        vrn=vrn_ent.get()
        #set a pattern for vehicle registration number
        RegNo_pattern= re.match(r'^[A-Z]{3}\d{3}[A-Z]{2}$', vrn)
        #validate user's entry
        if not RegNo_pattern:
            invalid_lbl=tk.Label(master=info_frm, text='Invalid registration number. Kindly enter a valid registration number.')
            invalid_lbl.grid(row=5, column=1, sticky='nsew')
        else:
            #call Enter_CarPark method from CarPark
            enter_result=current_user.Enter_CarPark(vrn)
            #create labels to show user details
            psi_lbl=tk.Label(master=info_frm, text='Your parking space ID is %s and your Ticket Number is %s' %(current_user.parking_ID, current_user.ticket_no))
            psi_lbl.grid(row=5, column=1, sticky='nsew')
            availableSpots=cp.available_parking_spots()
            availSpots_lbl=tk.Label(master=info_frm, text='Available parking spots: %s ' %(availableSpots))
            availSpots_lbl.grid(row=6, column=1, sticky='nsew')
       
    vrn_btn=tk.Button(master=info_frm, text='Enter', command=enter_vrn)
    vrn_btn.grid(row=4, column=2, sticky='nsew')
#function for 'exit car park' button
def ExitCarPark():
    DestroyWidgets()
    #create widgets to exit car park
    ex_lbl1=tk.Label(master=info_frm, text='Exit Car Park.')
    ex_lbl1.grid(row=2, column=1, sticky='nsew')
    ex_lbl=tk.Label(master=info_frm, text='Kindly enter your Vehicle Registration Number e.g ABC123DE:')
    ex_lbl.grid(row=3, column=1, sticky='nsew')
    ex_ent=tk.Entry(master=info_frm, width=25)
    ex_ent.grid(row=4, column=1, sticky='nsew')
    def exit_vrn():
        #get the vehicle registration number from the entry widget
        ex_vrn=ex_ent.get()
        vehicle_present=current_user.Exit_CarPark(ex_vrn)
        #validate user's entry
        if vehicle_present:
            parkingFee_lbl=tk.Label(master=info_frm, text= 'Your Parking Fee is: £%0.3s' %(current_user.parking_fee))
            parkingFee_lbl.grid(row=5, column=1, sticky='nsew')
            availSpots_lbl=tk.Label(master=info_frm, text= 'Availble Parking Space(s): %s' %(cp.available_parking_spots()))
            availSpots_lbl.grid(row=6, column=1, sticky='nsew')
            freeSpot_lbl=tk.Label(master=info_frm, text= 'Parking space %s previously occupied is free'%(current_user.parking_ID))
            freeSpot_lbl.grid(row=7, column=1, sticky='nsew')
            thanks_lbl=tk.Label(master=info_frm, text= 'Thank you for parking with us!.')
            thanks_lbl.grid(row=8, column=1, sticky='nsew')
        else:
            invalid_lbl=tk.Label(master=info_frm, text= 'No vehicle with vehicle registration number provided! Kindly enter a valid vehicle registration number.')
    ex_btn=tk.Button(master=info_frm, text='Enter', command=exit_vrn)
    ex_btn.grid(row=4, column=2, sticky='nsew')

#function for 'view available spots' buuton
def AvailableSpots():
    DestroyWidgets()
    AvailableSpots=cp.available_parking_spots()
    availSpots_lbl=tk.Label(master=info_frm, text= 'Available parking spot(s): %s' %(AvailableSpots))
    availSpots_lbl.grid(row=2, column=1, sticky='nsew')
#function for 'query car park' button
def QueryParking():
    DestroyWidgets()
    #create widgets to query car park
    query_lbl1=tk.Label(master=info_frm, text='Query Parking Record')
    query_lbl1.grid(row=2, column=1, sticky='nsew')
    query_lbl=tk.Label(master=info_frm, text='Kindly enter your ticket number')
    query_lbl.grid(row=3, column=1, sticky='nsew')
    query_ent=tk.Entry(master=info_frm, width=25)
    query_ent.grid(row=4, column=1, sticky='nsew')
    def query_ticketno():
        ticketno=query_ent.get()
        recordsList=current_user.Query_Parkingrecord(ticketno)
        #validate user's entry
        if not recordsList:
            invalind_lbl=tk.Label(master=info_frm, text= 'No record found for %s. Kindly enter valid ticket number.' %(ticketno))
            invalind_lbl.grid(row=5, column=1, sticky='nsew')
        else:
            userDetails_lbl=tk.Label(master=info_frm, text= '''Your Vehicle Registration Number is :%s
                 Your Parking Space ID is: %s 
                 Your Ticket Number is : %s
                 Your Entry Time is: %s
                 Your Exit Time is: %s
                 Your Parking Fee is: %s
                 ''' %(recordsList[0], recordsList[1], recordsList[2], recordsList[3], recordsList[4], recordsList[5]))
            userDetails_lbl.grid(row=5, column=1, sticky='nsew')
    query_btn=tk.Button(master=info_frm, text='Enter', command=query_ticketno)
    query_btn.grid(row=4, column=2, sticky='nsew')
#function for 'quit' button
def Quit():
    window.destroy()


#create window
window=tk.Tk()
#name the window
window.title('KEELE CARPARK SYSTEM')
#create frame to contain the button widgets
btn_frm=tk.Frame(master=window, relief=tk.SUNKEN, borderwidth=2)
btn_frm.grid(row=0, column=0)
#create and position buttons
enter_btn=tk.Button(master=btn_frm, text='Enter Car Park',width=20, height=3, command=EnterCarPark)
enter_btn.grid(row=0, column=0, sticky='e', padx=5, pady=5)

exit_btn=tk.Button(master=btn_frm, text='Exit Car Park', width=20, height=3, command=ExitCarPark) 
exit_btn.grid(row=0, column=1, sticky='e', padx=5, pady=5)

availablespace_btn=tk.Button(master=btn_frm, text='View Available Parking Spaces', width=25, height=3, command= AvailableSpots)
availablespace_btn.grid(row=0, column=2, sticky='e', padx=5, pady=5)

queryrecord_btn=tk.Button(master=btn_frm, text='Query Parking Record', width=20, height=3, command= QueryParking) 
queryrecord_btn.grid(row=0, column=3, sticky='e', padx=5, pady=5)

quit_btn=tk.Button(master=btn_frm, text='Quit', width=20, height=3, command=Quit)
quit_btn.grid(row=0, column=4, sticky='e', pady=5)

#create frame to display information
info_frm= tk.Frame(master=window, relief=tk.RAISED, borderwidth=2)
info_frm.grid(row=1, column=0, sticky='nsew')

#create the welcome label
greeting_lbl=tk.Label(master=info_frm, text='Welcome to Keele Car Park!')
greeting_lbl.grid(row=1,column=3, columnspan=4, padx=10, pady=10, sticky='nsew')


window.mainloop()