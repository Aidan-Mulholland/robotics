import serial
import time

class MotorsYukon():
    def __init__(self,port="/dev/ttyTHS1", mecanum=False):
       
        self.port=port
        self.baudrate=115200
        self.bytesize=serial.EIGHTBITS
        self.parity=serial.PARITY_NONE
        self.stopbits=serial.STOPBITS_ONE
        self.mecanum=mecanum
        return

    def connect(self):
        # Connect to Yukon via UART 
        self.serial_port = serial.Serial(
            port=self.port,
            baudrate=self.baudrate,
            bytesize=self.bytesize,
            parity=self.parity,
            stopbits=self.stopbits,
        )
        return
    
    def close(self):
        # Connect to Yukon via UART 
        self.serial_port.close()
        return

    def send(self, message):
        self.connect()
        self.serial_port.write(message.encode())
        self.close()
        return

    def forward(self, speed=0.3):
        message=f"m;direction:forward;speed:{speed}\n"
        self.send(message)
        return

    def backward(self, speed=0.3):
        message = f"m;direction:backward;speed:{speed}\n"
        self.send(message)
        return

    def right(self, speed=0.3):
        if self.mecanum:
            message = f"m;direction:right;speed:{speed}\n"
        else:
            message = f"m;direction:spinright;speed:{speed}\n"
        self.send(message)
        return

    def left(self, speed=0.3):
        if self.mecanum:
            message = f"m;direction:left;speed:{speed}\n"
        else: 
            message = f"m;direction:spinleft;speed:{speed}\n" 
        self.send(message)
        return
    
    def spinRight(self, speed=0.3):
        message = f"m;direction:spinright;speed:{speed}\n"
        self.send(message)
        return

    def spinLeft(self, speed=0.3):
        message = f"m;direction:spinleft;speed:{speed}\n"
        self.send(message)
        return
    
    def stop(self, speed=0.0):
        message = f"m;direction:stop;speed:{speed}\n"
        self.send(message)
        return

    #TODO Add individual motor actions eg. left front forward left front back 

if __name__ == "__main__":
    motorTest = MotorsYukon(mecanum=True)
    print("Forward")
    motorTest.left()
    time.sleep(2)
    print("Stop")
    motorTest.stop()
