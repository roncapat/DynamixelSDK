#!/usr/bin/env python
#coding: UTF-8

import dynamixel_functions as df
from ctypes import c_char_p

COMM_SUCCESS       = 0
COMM_PORT_BUSY     = -1000
COMM_TX_FAIL       = -1001
COMM_RX_FAIL       = -1002
COMM_TX_ERROR      = -2000
COMM_RX_WAITING    = -3000
COMM_RX_TIMEOUT    = -3001
COMM_RX_CORRUPT    = -3002
COMM_NOT_AVAILABLE = -9000

class PortHandler:
  def __init__(self, port_name):
    self._handler = df.portHandler(port_name)
  
  def openPort(self):
    return int(df.openPort(self._handler))
   
  def closePort(self):
    df.closePort(self._handler)
  
  def clearPort(self):
    df.clearPort(self._handler)
    
  def setPortName(self, port_name):
    df.setPortName(self._handler, port_name)
    
  def getPortName(self):
    return c_char_p((df.getPortName(self._handler))).value
    
  def setBaudRate(self, baud_rate):
    return bool(int(df.setBaudRate(self._handler, baudrate)))
    
  def getBaudRate(self):
    return int(df.getBaudRate(self._handler))
    
  def readPort(self, length):
    packet = create_string_buffer(length)
    ret = int(df.readPort(self._handler, packet, length))
    return int(ret), [ord(i) for i in packet]
     
  def writePort(self, length):
    packet = create_string_buffer(length)
    ret = int(df.writePort(self._handler, packet, length))
    return int(ret), [ord(i) for i in packet]

  def setPacketTimeout(self, packet_length):
    df.setPacketTimeout(self._handler, packet_length)

  def setPacketTimeoutMSec(self, msec):
    df.setPacketTimeoutMSec(self._handler, msec)
  
  def isPacketTimeout(self):
    return bool(int(df.isPacketTimeout(self._handler)))
      

class PacketHandler:
  __initiated = False
  __init__(self, protocol_version = 1):
    self._v = protocol_version
    if not initiated:
      df.packetHandler()
      PacketHandler.__initiated = True
  
  def getTxRxResult(result): 
    return c_char_p(df.getTxRxResult(result)).value

  def getRxPacketError(error):
    return c_char_p(df.getRxPacketError(error)).value

  def getLastTxRxResult(self, port_num):
    return int(df.getLastTxRxResult(port_num))
  
  def getLastRxPacketError(self, port_num):
    return int(df.getLastRxPacketError(port_num))
  
  #def setDataWrite(self, port_num, data_length, data_pos, data):
  #  df.setDataWrite(port_num, self._v, data_length, data_pos, data)
    
  #def getDataRead(self, port_num, data_length, data_pos):
  #  return int(df.getDataRead(port_num, self._v, data_length, data_pos))

  def txPacket(self, port_num, packet):
    df._txPacket(port_num, self._v, c_char_p(packet))
    
  def rxPacket(self, port_num):
    df.rxPacket(port_num, self._v)

  def txRxPacket(self, port_num):
    df.txRxPacket(port_num, self._v)

  def ping(self, port_num, id):
    df.ping(port_num, self._v, id)
    
  def pingGetModelNum(self, port_num, id):
    return int(df.pingGetModelNum(port_num, self._v, id))

  def broadcastPing(self, port_num):
    df.broadcastPing(port_num, self._v)

  def reboot(self, port_num, id):
    df.reboot(port_num, self._v, id)

  def factoryReset(self, port_num, id):
    df.factoryReset(port_num, self._v, id)

  def readTx(self, port_num, id, address, length):
    df.readTx(port_num, self._v, id, address, length)
  
  def readRx(self, port_num, length):
    df.readRx(port_num, self._v, length)

  def readTxRx(self, port_num, id, address, length):
    df.readTxRx(port_num, self._v, id, address, length)

  def read1ByteTx(self, port_num, id, address):
    df.read1ByteTx(port_num, self._v, id, address)
  
  def read1ByteRx(self, port_num):
    return int(df.read1ByteRx(port_num))

  def read1ByteTxRx(self, port_num, id, address):
    return int(df.read1ByteTxRx(port_num, self._v, id, address))
    
  def read2ByteTx(self, port_num, id, address):
    df.read2ByteTx(port_num, self._v, id, address)
  
  def read2ByteRx(self, port_num):
    return int(df.read2ByteRx(port_num))

  def read2ByteTxRx(self, port_num, id, address):
    return int(df.read2ByteTxRx(port_num, self._v, id, address))
    
  def read4ByteTx(self, port_num, id, address):
    df.read4ByteTx(port_num, self._v, id, address)
  
  def read4ByteRx(self, port_num):
    return int(df.read4ByteRx(port_num))

  def read4ByteTxRx(self, port_num, id, address):
    return int(df.read4ByteTxRx(port_num, self._v, id, address))

  def writeTxOnly(self, port_num, id, address, length):
    df.writeTxOnly(port_num, self._v, id, address, length)
  
  def writeTxRx(self, port_num, id, address, length):
    df.writeTxOnly(port_num, self._v, id, address, length)
  
  def write1ByteTxOnly(self, port_num, id, address, data):
    df.write1ByteTxOnly(port_num, self._v, id, address, data)
    
  def write1ByteTxRx(self, port_num, id, address, data):
    df.write1ByteTxOnly(port_num, self._v, id, address, data)

  def write2ByteTxOnly(self, port_num, id, address, data):
    df.write2ByteTxOnly(port_num, self._v, id, address, data)
  
  def write2ByteTxRx(self, port_num, id, address, data):
    df.write2ByteTxOnly(port_num, self._v, id, address, data)
  
  def write4ByteTxOnly(self, port_num, id, address, data):
    df.write4ByteTxOnly(port_num, self._v, id, address, data)
    
  def write4ByteTxRx(self, port_num, id, address, data):
    df.write4ByteTxOnly(port_num, self._v, id, address, data)

  def regWriteTxOnly(self, port_num, id, address, length):
    df.regWriteTxOnly(port_num, self._v, id, address, length)

  def regWriteTxRx(self, port_num, id, address, length):
    df.regWriteTxRx(port_num, self._v, id, address, length)
    
  def syncReadTx(self, port_num, start_address, data_length, param_length):
    df.syncReadTx(port_num, self._v, start_address, data_length, param_length)    
  
  # syncReadRx   -> GroupSyncRead
  # syncReadTxRx -> GroupSyncRead

  def syncWriteTxOnly(self, port_num, start_address, data_length, param_length):
    df.syncWriteTxOnly(port_num, self._v, start_address, data_length, param_length)
  
  def bulkReadTx(self, port_num, param_length):
    df.bulkReadTx(port_num, self._v, param_length)

  # bulkReadRx   -> GroupBulkRead
  # bulkReadTxRx -> GroupBulkRead

  def bulkWriteTxOnly(self, port_num, param_length):
    df.bulkWriteTxOnly(port_num, self._v, param_length)


class GroupBulkRead:  
  def __init__(self, port_num, packet_handler):
    self._b = int(df.groupBulkRead(port_num, packet_handler._v))

  def groupBulkReadAddParam(self, id, start_address, data_length):
    return int(df.groupBulkReadAddParam(self._b, id, start_address, data_length))
  
  def groupBulkReadRemoveParam(self, id):
    df.groupBulkReadRemoveParam(self._b, id)

  def groupBulkReadClearParam(self):
    df.groupBulkReadClearParam(self._b)
    
  def groupBulkReadTxPacket(self):
    df.groupBulkReadTxPacket(self._b)

  def groupBulkReadRxPacket(self):
    df.groupBulkReadRxPacket(self._b)    
    
  def groupBulkReadTxRxPacket(self):
    df.groupBulkReadTxRxPacket(self._b)    
    
  def groupBulkReadIsAvailable(self, id, address, data_length):
    return int(df.groupBulkReadIsAvailable(self._b, id, address, data_length))
  
  def groupBulkReadGetData(self, id, address, data_length):
    return int(df.groupBulkReadGetData(self._b, id, address, data_length))
    

class GroupBulkWrite:
  def __init__(self, port_num, packet_handler):
    self._b = int(df.groupBulkWrite(port_num, packet_handler._v))

  def groupBulkWriteAddParam(self, id, start_address, data_length, data, input_length):
    return int(df.groupBulkWriteAddParam(self._b, id, start_address, data_length, data, input_length))
    
  def groupBulkWriteChangeParam(self, id, start_address, data_length, data, input_length, data_pos):
    return bool(int(df.groupBulkWriteChangeParam(self._b, id, start_address, data_length, data, input_length, data_pos)))
  
  def groupBulkWriteRemoveParam(self, id):
    df.groupBulkWriteRemoveParam(self._b, id)

  def groupBulkWriteClearParam(self):
    df.groupBulkWriteClearParam(self._b)
    
  def groupBulkWriteTxPacket(self):
    df.groupBulkWriteTxPacket(self._b)



class GroupSyncRead:
  def __init__(self, port_num, packet_handler, start_address, data_length):
    self._g = int(df.groupSyncRead(port_num, packet_handler._v, start_address, data_length))

  def groupSyncReadAddParam(id):
    return int(df.groupSyncReadAddParam(self._g, id))
    
  def groupSyncReadRemoveParam(id):
    df.groupSyncReadRemoveParam(self._g, id)
    
  def groupSyncReadCleareParam():
    df.groupSyncReadClearParam(self._g)
    
  def groupSyncReadTxPacket():
    df.groupSyncReadTxPacket(self._g)
    
  def groupSyncReadRxPacket():
    df.groupSyncReadRxPacket(self._g)
    
  def groupSyncReadTxRxPacket():
    df.groupSyncReadTxRxPacket(self._g)

  def groupSyncReadIsAvailable(id, address, data_length):
    return int(df.groupSyncReadIsAvailable(self._g, id, address, data_length))

  def groupSyncReadGetData(id, address, data_length):
    return int(df.groupSyncReadGetData(self._g, id, address, data_length))


class GroupSyncWrite:
  def __init__(self, port_num, packet_handler, start_address, data_length):
    self._g = int(df.groupSyncWrite(port_num, packet_handler._v, start_address, data_length))

  def groupSyncWriteAddParam(self, id, data, data_length):
    return int(df.groupSyncWriteAddParam(self._g, id, data, data_length))
    
  def groupSyncWriteChangeParam(self, id, data, data_length, data_pos):
    return bool(int(df.groupSyncWriteChangeParam(self._g, id, data, data_length, data_pos)))
  
  def groupSyncWriteRemoveParam(self, id):
    df.groupSyncWriteRemoveParam(self._g, id)

  def groupSyncWriteClearParam(self):
    df.groupSyncWriteClearParam(self._g)
    
  def groupSyncWriteTxPacket(self):
    df.groupSyncWriteTxPacket(self._g)
