def tempCheck(temperature):
    if temperature < 0 or temperature > 45:
      print('Temperature is out of range!')
      return False

def socCheck(soc):
    if soc < 20 or soc > 80:
      print('State of Charge is out of range!')
      return False

def chargeCheck(charge_rate):
    if charge_rate > 0.8:
      print('Charge rate is out of range!')
      return False

def rangeCheck(value,min,max):
    retValmin = 1
    retValmax = 1
    if min != -1:
        if value < min:
            retValmin = 0
    if max != -1:
        if value > max:
            retValmax = 0
    return retValmin and retValmax
        
def battery_is_ok(temperature, soc, charge_rate):
    not rangeCheck(temperature,0,45) == 0 and print("Temprature out of range")    
    not rangeCheck(soc,20,80) == 0 and print("soc out of range")
    not rangeCheck(charge_rate,-1,0.8) == 0 and print("charge_rate out of range")
    

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
