import pyvisa

class Ectron1120:
    def __init__(self, gpib_address: str):
        self.gpib_address = gpib_address
        self.rm = pyvisa.ResourceManager()
        self.instrument = None

    def connect(self):
        try:
            self.instrument = self.rm.open_resource(self.gpib_address)
            self.instrument.timeout = 2000
            print(f"Successfully connected to Ectron at: {self.gpib_address}")
        except Exception as e:
            print(f"Connection error. Check cable or power: {e}")
            self.instrument = None

    def disconnect(self):
        if self.instrument:
            self.instrument.close()
            print("Connection safely closed.")

    def _send_command(self, command: str):
        if self.instrument:
            self.instrument.write(command)
        else:
            print("Warning: Attempted to send a command without an active connection.")

    def clear_errors(self):
        self._send_command("W")
        print("Memory and errors cleared.")

    def execute(self):
        self._send_command("Z")
        print("Execute command (Z) sent.")

    def set_millivolts(self, mv_value: float):
        command = f"{mv_value}M"
        self._send_command(command)
        print(f"Setting {mv_value} mV (Command sent: {command})")

    def set_temperature(self, degrees: float, tc_type: str):
        tc_letter = tc_type.upper()
        command = f"{degrees}{tc_letter}"
        self._send_command(command)
        print(f"Setting {degrees} C on Type {tc_letter} Thermocouple (Command sent: {command})")

    def store_configuration(self, register: int):
        command = f"X{register}"
        self._send_command(command)
        print(f"Storing state in register {register} (Command sent: {command})")

    def recall_configuration(self, register: int):
        command = f"Y{register}"
        self._send_command(command)
        print(f"Recalling state from register {register} (Command sent: {command})")