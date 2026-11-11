from ectron1120.driver import Ectron1120

def automation_test():
    calibrator = Ectron1120('GPIB0::14::INSTR')
    
    calibrator.connect()
    calibrator.clear_errors()
    
    # Test 1: Simulate 100 degrees on a Type K thermocouple and store it
    calibrator.set_temperature(100.0, 'K')
    calibrator.store_configuration(1)
    calibrator.execute()
    
    # Test 2: Generate direct voltage
    calibrator.set_millivolts(25.5)
    calibrator.execute()
    
    # Test 3: Recall the configuration saved in Test 1
    calibrator.recall_configuration(1)
    calibrator.execute()
    
    calibrator.disconnect()

if __name__ == "__main__":
    automation_test()