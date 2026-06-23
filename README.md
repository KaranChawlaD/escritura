# escritura
converting a 3D printer into a handwriter

## project status
beginning stages. first step is local control of my 3D printer.

## setup
- utilizes a virtual environment to prevent any dependency failures.
```bash
python -m venv venv
venv\Scripts\activate # or venv\bin\activate for linux/mac
```
- install the required dependencies in requirements.txt
```bash
pip install -r requirements.txt
```
- figure out your printer's SERIAL_PORT. On a Windows Laptop, this requires tethering to the printer with a data transferrable cable and looking for the serial port in Device Manager -> Ports (ex. "COMX"). Add this in a ".env" file:
```bash
SERIAL_PORT="COMX"
```