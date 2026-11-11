from ectron1120.driver import Ectron1120

def automatizacion_prueba():
    calibrador = Ectron1120('GPIB0::14::INSTR')
    calibrador.connect()
    calibrador.clear_errors()
    
    # 1. Configuramos 100 grados y lo GUARDAMOS en la memoria 1
    calibrador.set_temperatura(100, 'K')
    calibrador.guardar_configuracion(1)
    calibrador.execute()
    
    # 2. Configuramos otra cosa distinta
    calibrador.set_millivoltios(15.0)
    calibrador.execute()
    
    # 3. LLAMAMOS la configuración que guardamos en el paso 1
    calibrador.cargar_configuracion(1)
    calibrador.execute()
    
    calibrador.disconnect()

if __name__ == "__main__":
    automatizacion_prueba()