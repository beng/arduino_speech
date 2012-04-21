import sys, serial, time

port='/dev/tty.usbserial-A1001Neq'

def main(val=5):
    s = serial.SERIAL(port)
    
    time.sleep(1)
    
    w = s.write(val)
    s.close()
    print 'byes written to port:', w
    print 'value written to port:', val

if __name__ == '__main__':
    args = sys.argv
    try:
        main(args[1])
    except IndexError:
        main()