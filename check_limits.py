def minCheck(value, min)
    return value < min
def maxCheck:
    return value > max
def rangeCheck(value,min,max):
    retValmin = 1
    retValmax = 1
    if min != 'NA':
        retValmin = minCheck(value,min)
    if max != 'NA':
        retValmax = minCheck(value,max)
    return retValmin and retValmax
        
def battery_is_ok(temperature, soc, charge_rate):
    tempVal = rangeCheck(temperature,0,45)
    socVal = rangeCheck(soc,20,80)
    chargeVal = rangeCheck(charge_rate,NA,0.8)
    
    print("Temperature out of range") if tempVal == 0 else None
    print("soc out of range") if socVal == 0  else None
    print("charge_rate out of range") if chargeVal == 0 else None
    
    
    return bool(tempVal and socVal and chargeVal)
    

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
