import time
import serial
import os
from dotenv import load_dotenv

load_dotenv()

# ------------------------------------------

SERIAL_PORT = os.getenv("SERIAL_PORT")
BAUD_RATE = 115200 # communication speed -> change to 250000 if script hangs

# ------------------------------------------

def send_gcode_cmd(ser, cmd):
    """send gcode cmd and output response"""
    print(f"\nsending {cmd}")

    ser.write((cmd + '\n').encode('utf-8'))
    time.sleep(0.5)

    while ser.in_waiting > 0:
        resp = ser.readline().decode('utf-8', errors='ignore').strip()
        print(f"printer: {resp}")

# ------------------------------------------

if __name__ == "__main__":
    try:
        print("connecting to printer...")
        printer = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)

        time.sleep(3) # reboot/wakeup
        print("\nconnected!")

        send_gcode_cmd(printer, "G28") #autohome

    except serial.SerialException as e:
        print(f"error: could not connect to printer: {e}")
    except KeyboardInterrupt:
        print("script cancelled by you")
    finally:
        if 'printer' in locals() and printer.is_open:
            printer.close()
            print("\nconnection closed")