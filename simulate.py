# I'm assuming this is to read the CAN.csv file and then display it for the driver... should do this interms of updating the driver

#Call the main.c as it loops to show the driver as well as checking the temp. in main.c
CANID = CANID()
CANMESSAGE = CANMESSAGE()

print('ID: 0x', CANID)
print('Message: ', CANMESSAGE)
