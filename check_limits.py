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
    tempVal = rangeCheck(temperature,0,45)
    socVal = rangeCheck(soc,20,80)
    chargeVal = rangeCheck(charge_rate,-1,0.8)
    
    print("Temperature out of range") if tempVal == 0 else None
    print("soc out of range") if socVal == 0  else None
    print("charge_rate out of range") if chargeVal == 0 else None
    
    
    return bool(tempVal and socVal and chargeVal)
    

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
