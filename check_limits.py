def rangeCheck(value, minv, maxv):
    if minv != 'NA' and value < minv:
        return False
    if maxv != 'NA' and value > maxv:
        return False
    return True
        
def battery_is_ok(temperature, soc, charge_rate):
    tempVal = rangeCheck(temperature,0,45)
    socVal = rangeCheck(soc,20,80)
    chargeVal = rangeCheck(charge_rate,'NA',0.8)
    
    print("Temperature out of range") if tempVal == True else None
    print("soc out of range") if socVal == True  else None
    print("charge_rate out of range") if chargeVal == True else None
    
    
    return bool(tempVal and socVal and chargeVal)

if __name__ == '__main__':
  assert(battery_is_ok(25, 70, 0.7) is True)
  assert(battery_is_ok(50, 85, 0) is False)
