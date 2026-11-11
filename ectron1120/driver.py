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
            print(f"Conectado exitosamente al Ectron en: {self.gpib_address}")
        except Exception as e:
            print(f"Error de conexion. Revisa el cable o encendido: {e}")
            self.instrument = None

    def disconnect(self):
        if self.instrument:
            self.instrument.close()
            print("Conexion cerrada de forma segura.")

    def _send_command(self, command: str):
        if self.instrument:
            self.instrument.write(command)
        else:
            print("Cuidado: Intentaste enviar un comando sin estar conectado.")

    def clear_errors(self):
        self._send_command("W")
        print("Memoria y errores limpiados.")

    def execute(self):
        self._send_command("Z")
        print("Comando de ejecucion (Z) enviado.")

    def set_millivoltios(self, valor_mv: float):
        comando = f"{valor_mv}M"
        self._send_command(comando)
        print(f"Configurando {valor_mv} mV (Codigo enviado: {comando})")

    def set_temperatura(self, grados: float, tipo_termopar: str):
        tipo = tipo_termopar.upper()
        comando = f"{grados}{tipo}"
        self._send_command(comando)
        print(f"Configurando {grados} C en Termopar Tipo {tipo} (Codigo enviado: {comando})")

    def guardar_configuracion(self, registro: int):
        comando = f"X{registro}"
        self._send_command(comando)
        print(f"Guardando estado en registro {registro} (Codigo enviado: {comando})")

    def cargar_configuracion(self, registro: int):
        comando = f"Y{registro}"
        self._send_command(comando)
        print(f"Cargando estado de registro {registro} (Codigo enviado: {comando})")