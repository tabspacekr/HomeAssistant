#참조: https://blog.actorsfit.com/a?ID=01200-258ba477-1fdb-4a28-9d6a-657effd55f10
from pstats import StatsProfile
import serial
import time

address_use = [False,True,False,False,False,False] # 0~5 Address 사용 유무, 테스트시에는 1번만 사용, 실 운영환경에서는 2~5사용
#address_use = [False,False,True,True,True,True] # 1~5 Address 사용 유무, 테스트시에는 1번만 사용, 실 운영환경에서는 2~5사용
print(str(address_use))
ser = serial.Serial("/dev/ttyUSB0", 4800)   #select the serial port, set the baud rate and 
if ser.is_open:
    print("===== Serial Port Open Success!!")
    # https://www.lammertbies.nl/comm/info/crc-calculation?crc=8005&method=hex
    # 위 주소에서 01 03 00 01 00 04 형태로 입력 후, HEX로 Input type 체크 후 Calculate CRC, CRC-16 (Modbus)의 데이터를 역으로처리. 0xC915의 경우, 15 C9 로 마지막에 입력
    
    # Address 1, DataPoint 0 to 6
    send_data_10 = bytes.fromhex('01 03 00 00 00 04 44 09') # SMO, Moisture Content
    send_data_11 = bytes.fromhex('01 03 00 01 00 04 15 C9') # STP, Temperature
    send_data_12 = bytes.fromhex('01 03 00 02 00 04 E5 C9') # SEC, Conductivity
    send_data_13 = bytes.fromhex('01 03 00 03 00 04 B4 09') # PH, PH Value
    send_data_14 = bytes.fromhex('01 03 00 04 00 04 05 C8') # NITROGEN, Nitrogen Content
    send_data_15 = bytes.fromhex('01 03 00 05 00 04 54 08') # PHOSPHORUS, Phosphorus Content
    send_data_16 = bytes.fromhex('01 03 00 06 00 04 A4 08') # POTASSIUM, Potassium Content

    # Address 2, DataPoint 0 to 6
    send_data_20 = bytes.fromhex('02 03 00 00 00 04 44 3A') # SMO, Moisture Content
    send_data_21 = bytes.fromhex('02 03 00 01 00 04 15 FA') # STP, Temperature
    send_data_22 = bytes.fromhex('02 03 00 02 00 04 E5 FA') # SEC, Conductivity
    send_data_23 = bytes.fromhex('02 03 00 03 00 04 B4 3A') # PH, PH Value
    send_data_24 = bytes.fromhex('02 03 00 04 00 04 05 FB') # NITROGEN, Nitrogen Content
    send_data_25 = bytes.fromhex('02 03 00 05 00 04 54 3B') # PHOSPHORUS, Phosphorus Content
    send_data_26 = bytes.fromhex('02 03 00 06 00 04 A4 3B') # POTASSIUM, Potassium Content

    # Address 3, DataPoint 0 to 6
    send_data_30 = bytes.fromhex('03 03 00 00 00 04 45 EB') # SMO, Moisture Content
    send_data_31 = bytes.fromhex('03 03 00 01 00 04 14 EB') # STP, Temperature
    send_data_32 = bytes.fromhex('03 03 00 02 00 04 E4 EB') # SEC, Conductivity
    send_data_33 = bytes.fromhex('03 03 00 03 00 04 B5 EB') # PH, PH Value
    send_data_34 = bytes.fromhex('03 03 00 04 00 04 04 EA') # NITROGEN, Nitrogen Content
    send_data_35 = bytes.fromhex('03 03 00 05 00 04 55 EA') # PHOSPHORUS, Phosphorus Content
    send_data_36 = bytes.fromhex('03 03 00 06 00 04 A5 EA') # POTASSIUM, Potassium Content

    # Address 4, DataPoint 0 to 6
    send_data_40 = bytes.fromhex('04 03 00 00 00 04 44 5C') # SMO, Moisture Content
    send_data_41 = bytes.fromhex('04 03 00 01 00 04 15 9C') # STP, Temperature
    send_data_42 = bytes.fromhex('04 03 00 02 00 04 E5 9C') # SEC, Conductivity
    send_data_43 = bytes.fromhex('04 03 00 03 00 04 B4 5C') # PH, PH Value
    send_data_44 = bytes.fromhex('04 03 00 04 00 04 05 9D') # NITROGEN, Nitrogen Content
    send_data_45 = bytes.fromhex('04 03 00 05 00 04 54 5D') # PHOSPHORUS, Phosphorus Content
    send_data_46 = bytes.fromhex('04 03 00 06 00 04 A4 5D') # POTASSIUM, Potassium Content

    # Address 5, DataPoint 0 to 6
    send_data_50 = bytes.fromhex('05 03 00 00 00 04 45 8D') # SMO, Moisture Content
    send_data_51 = bytes.fromhex('05 03 00 01 00 04 14 4D') # STP, Temperature
    send_data_52 = bytes.fromhex('05 03 00 02 00 04 E4 4D') # SEC, Conductivity
    send_data_53 = bytes.fromhex('05 03 00 03 00 04 B5 8D') # PH, PH Value
    send_data_54 = bytes.fromhex('05 03 00 04 00 04 04 4C') # NITROGEN, Nitrogen Content
    send_data_55 = bytes.fromhex('05 03 00 05 00 04 55 8C') # PHOSPHORUS, Phosphorus Content
    send_data_56 = bytes.fromhex('05 03 00 06 00 04 A5 8C') # POTASSIUM, Potassium Content

    #send_data_xx = 'ff010055000056' # python2.7의 경우에 해당
    #send_data_xx = send_data.decode('hex')    #transmit data to b '/xff/x01/x00U # python2.7의 경우에 해당

    for address_no in range(len(address_use)):
        if address_use[address_no] == False:
            print("# Address No : "+str(address_no)+" is "+str(address_use[address_no]))
            continue
        
        print("# Address No : "+str(address_no)+" START!")

        ser.write(eval('send_data_'+str(address_no)+'0'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            str_return_data = str(return_data.hex())
            print("-ReturnData_0 : "+str_return_data)
            #print(str_return_data[6:10])
            SMO = int(str_return_data[6:10],16) / 10
            print("--SMO : "+str(SMO)+"%")

        ser.write(eval('send_data_'+str(address_no)+'1'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
            str_return_data = str(return_data.hex())
            print("-ReturnData_1 : "+str_return_data)
            #feedback_data = int(str_return_data[-6:-2], 16)
            #feedback_data = str_return_data[6:10]
            #print(str_return_data[6:10])
            STP = int(str_return_data[6:10],16) / 10
            print("--STP : "+str(STP)+"c")

        ser.write(eval('send_data_'+str(address_no)+'2'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
            str_return_data = str(return_data.hex())
            print("-ReturnData_2 : "+str_return_data)
            #feedback_data = int(str_return_data[-6:-2], 16)
            #feedback_data = str_return_data[6:10]
            SEC = int(str_return_data[6:10],16)
            print("--SEC : "+str(SEC))

        ser.write(eval('send_data_'+str(address_no)+'3'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
            str_return_data = str(return_data.hex())
            print("-ReturnData_3 : "+str_return_data)
            #feedback_data = int(str_return_data[-6:-2], 16)
            PH = int(str_return_data[6:10],16) / 10
            print("--PH : "+str(PH))

        ser.write(eval('send_data_'+str(address_no)+'4'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
            str_return_data = str(return_data.hex())
            print("-ReturnData_4 : "+str_return_data)
            #feedback_data = int(str_return_data[-6:-2], 16)
            #feedback_data = str_return_data[6:10]
            NITROGEN = int(str_return_data[6:10],16)
            print("--NITROGEN : "+str(NITROGEN))

        ser.write(eval('send_data_'+str(address_no)+'5'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
            str_return_data = str(return_data.hex())
            print("-ReturnData_5 : "+str_return_data)
            #feedback_data = int(str_return_data[-6:-2], 16)
            #feedback_data = str_return_data[6:10]
            PHOSPHORUS = int(str_return_data[6:10],16)
            print("--PHOSPHORUS : "+str(PHOSPHORUS))

        ser.write(eval('send_data_'+str(address_no)+'6'))   # RS485 Serial Send Data Commands
        time.sleep(0.1)        #delay, otherwise len_return_data will return 0, easily overlooked here! ! ! 
        len_return_data = ser.inWaiting()  #Get buffered data (received data) length 
        if len_return_data:
            return_data = ser.read(len_return_data)  #read buffer data 
            #bytes (binary 2) is converted to hex (16 hex), it is noted here Python3.7 different Python2.7 converted, and the converted character string Intercept the required data field, and then convert it to decimal
            str_return_data = str(return_data.hex())
            print("-ReturnData_6 : "+str_return_data)
            #feedback_data = int(str_return_data[-6:-2], 16)
            #feedback_data = str_return_data[6:10]
            POTASSIUM = int(str_return_data[6:10],16)
            print("--POTASSIUM : "+str(POTASSIUM))
        
        print("# Address No : "+str(address_no)+" END!")

else:
    print("port open failed")


        # feedback_data = str_return_data[11:15]
        # print("Temperature : "+feedback_data)
        # feedback_data = str_return_data[16:20]
        # print("Conduc : "+feedback_data)        


# # This code is ported from modbus CRC16(https://www.modbustools.com/modbus_crc16.htm)

# crcTable=[0x0000,0xC0C1,0xC181,0x0140,0xC301,0x03C0,0x0280,0xC241,0xC601,0x06C0,0x0780,0xC741,0x0500,0xC5C1,0xC481,0x0440,0xCC01,0x0CC0,0x0D80,0xCD41,0x0F00,0xCFC1,0xCE81,0x0E40,0x0A00,0xCAC1,0xCB81,0x0B40,0xC901,0x09C0,0x0880,0xC841,0xD801,0x18C0,0x1980,0xD941,0x1B00,0xDBC1,0xDA81,0x1A40,0x1E00,0xDEC1,0xDF81,0x1F40,0xDD01,0x1DC0,0x1C80,0xDC41,0x1400,0xD4C1,0xD581,0x1540,0xD701,0x17C0,0x1680,0xD641,0xD201,0x12C0,0x1380,0xD341,0x1100,0xD1C1,0xD081,0x1040,0xF001,0x30C0,0x3180,0xF141,0x3300,0xF3C1,0xF281,0x3240,0x3600,0xF6C1,0xF781,0x3740,0xF501,0x35C0,0x3480,0xF441,0x3C00,0xFCC1,0xFD81,0x3D40,0xFF01,0x3FC0,0x3E80,0xFE41,0xFA01,0x3AC0,0x3B80,0xFB41,0x3900,0xF9C1,0xF881,0x3840,0x2800,0xE8C1,0xE981,0x2940,0xEB01,0x2BC0,0x2A80,0xEA41,0xEE01,0x2EC0,0x2F80,0xEF41,0x2D00,0xEDC1,0xEC81,0x2C40,0xE401,0x24C0,0x2580,0xE541,0x2700,0xE7C1,0xE681,0x2640,0x2200,0xE2C1,0xE381,0x2340,0xE101,0x21C0,0x2080,0xE041,0xA001,0x60C0,0x6180,0xA141,0x6300,0xA3C1,0xA281,0x6240,0x6600,0xA6C1,0xA781,0x6740,0xA501,0x65C0,0x6480,0xA441,0x6C00,0xACC1,0xAD81,0x6D40,0xAF01,0x6FC0,0x6E80,0xAE41,0xAA01,0x6AC0,0x6B80,0xAB41,0x6900,0xA9C1,0xA881,0x6840,0x7800,0xB8C1,0xB981,0x7940,0xBB01,0x7BC0,0x7A80,0xBA41,0xBE01,0x7EC0,0x7F80,0xBF41,0x7D00,0xBDC1,0xBC81,0x7C40,0xB401,0x74C0,0x7580,0xB541,0x7700,0xB7C1,0xB681,0x7640,0x7200,0xB2C1,0xB381,0x7340,0xB101,0x71C0,0x7080,0xB041,0x5000,0x90C1,0x9181,0x5140,0x9301,0x53C0,0x5280,0x9241,0x9601,0x56C0,0x5780,0x9741,0x5500,0x95C1,0x9481,0x5440,0x9C01,0x5CC0,0x5D80,0x9D41,0x5F00,0x9FC1,0x9E81,0x5E40,0x5A00,0x9AC1,0x9B81,0x5B40,0x9901,0x59C0,0x5880,0x9841,0x8801,0x48C0,0x4980,0x8941,0x4B00,0x8BC1,0x8A81,0x4A40,0x4E00,0x8EC1,0x8F81,0x4F40,0x8D01,0x4DC0,0x4C80,0x8C41,0x4400,0x84C1,0x8581,0x4540,0x8701,0x47C0,0x4680,0x8641,0x8201,0x42C0,0x4380,0x8341,0x4100,0x81C1,0x8081,0x4040]

# # default returned value is array
# # If second param is True then returning single value
# def crc16(data, byInt = False):
#     crc= [0xff, 0xff];
#     for datum in data:
#         ncrc = crcTable[(crc[0] ^ datum)]
#         crc[0] = (ncrc & 0x00FF) ^ crc[1]
#         crc[1] = ncrc >> 8
#     if(byInt):
#         return crc[0]*256 + crc[1];
#     return crc

# ## USAGE
# res = crc16([0x7E, 0x01, 0x01])
# print ("Returning an array [%s] %2x %2x" %(', '.join(str(x) for x in res), res[0], res[1]))
# res = crc16([0x7E, 0x01, 0x01], True)
# print ("Returning single value %d %2x %2x" %(res, res>>8, res & 0xff))
