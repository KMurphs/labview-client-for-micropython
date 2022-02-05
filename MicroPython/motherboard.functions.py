import machine

version = ""


def read_MON12V():
    ### 12 Primary Voltage measurement
    mon12v = machine.ADC('MON12V')
    
    return mon12v.read_u16()*3.44/65535*(14.3+3.3)/3.3



def read_MON5V():
    ### 5V MB Voltage measurement
    mon5v = machine.ADC('MON5V')
    return mon5v.read_u16()*3.44/65535*2



def read_MON3v3():
    ### 3V3 MB Voltage measurement
    mon3v = machine.ADC('MON3V')
    return mon3v.read_u16()*3.44/65535*(3.3+5.6)/5.6




