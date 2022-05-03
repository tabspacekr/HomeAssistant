#참조: https://blog.actorsfit.com/a?ID=01200-258ba477-1fdb-4a28-9d6a-657effd55f10
from pstats import StatsProfile
import serial
import time

ser = serial.Serial("/dev/ttyUSB0", 4800)   #select the serial port, set the baud rate and 
if ser.is_open:
    print("port open success")
    #hex (hex 16) is converted to bytes (2 hex), It should be noted here Python3.7 conversion with different Python2.7
    # https://www.lammertbies.nl/comm/info/crc-calculation?crc=8005&method=hex
    # 위 주소에서 01 03 00 01 00 04 형태로 입력 후, HEX로 Input type 체크 후 Calculate CRC, CRC-16 (Modbus)의 데이터를 역으로처리. 0xC915의 경우, 15 C9 로 마지막에 입력
    send_data_0 = bytes.fromhex('01 03 00 00 00 04 44 09') # SMO, Moisture Content
    send_data_1 = bytes.fromhex('01 03 00 01 00 04 15 C9') # STP, Temperature
    send_data_2 = bytes.fromhex('01 03 00 02 00 04 E5 C9') # SEC, Conductivity
    send_data_3 = bytes.fromhex('01 03 00 03 00 04 B4 09') # PH, PH Value
    send_data_4 = bytes.fromhex('01 03 00 04 00 04 05 C8') # NITROGEN, Nitrogen Content
    send_data_5 = bytes.fromhex('01 03 00 05 00 04 54 08') # PHOSPHORUS, Phosphorus Content
    send_data_6 = bytes.fromhex('01 03 00 06 00 04 A4 08') # POTASSIUM, Potassium Content

    #send_data = 'ff010055000056' #python2.7용
    #send_data = send_data.decode('hex')    #transmit data to b '/xff/x01/x00U #python2.7용
    ser.write(send_data_0)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_0 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        ##feedback_data = int(str_return_data[6:10],16)
        print(str_return_data[6:10])
        SMO = int(str_return_data[6:10],16) / 10
        #print("SMO : "+str(int(str_return_data[0:6],16))+"."+str(int(str_return_data[7:10],16))+"%")
        print("SMO : "+str(SMO)+"%")

    ser.write(send_data_1)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_1 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        #feedback_data = str_return_data[6:10]
        print(str_return_data[6:10])
        STP = int(str_return_data[6:10],16) / 10
        print("STP : "+str(STP)+"c")

    ser.write(send_data_2)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_2 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        #feedback_data = str_return_data[6:10]
        SEC = int(str_return_data[6:10],16)
        print("SEC : "+str(SEC))

    ser.write(send_data_3)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_3 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        PH = int(str_return_data[6:10],16) / 10
        print("PH : "+str(PH))

    ser.write(send_data_4)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_4 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        #feedback_data = str_return_data[6:10]
        NITROGEN = int(str_return_data[6:10],16)
        print("NITROGEN : "+str(NITROGEN))

    ser.write(send_data_5)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_5 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        #feedback_data = str_return_data[6:10]
        PHOSPHORUS = int(str_return_data[6:10],16)
        print("PHOSPHORUS : "+str(PHOSPHORUS))

    ser.write(send_data_6)   #send commands
    time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
    len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
    if len_return_data:
        return_data = ser.read(len_return_data)  #read buffer data 
        #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
        str_return_data = str(return_data.hex())
        print("send_data_6 : "+str_return_data)
        #feedback_data = int(str_return_data[-6:-2], 16)
        #feedback_data = str_return_data[6:10]
        POTASSIUM = int(str_return_data[6:10],16)
        print("POTASSIUM : "+str(POTASSIUM))


else:
    print("port open failed")


        # feedback_data = str_return_data[11:15]
        # print("Temperature : "+feedback_data)
        # feedback_data = str_return_data[16:20]
        # print("Conduc : "+feedback_data)        
