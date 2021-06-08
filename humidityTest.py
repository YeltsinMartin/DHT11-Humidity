import os
import serial
import time
import signal
import sys
import matplotlib.pyplot as plt
import matplotlib.animation as animation

plt.style.use('fivethirtyeight')

x = []
y1 = []
y2 = []

i = 0
arduino = serial.Serial(port='COM5', baudrate=9600, timeout=.1)

def signal_handler(sig, frame):
    print('You pressed Ctrl+C!')
    arduino.close()
    sys.exit(0)

signal.signal(signal.SIGINT, signal_handler)


def animate(i):
    val = arduino.readline()
    if val != "":
        s="{0}.{1}".format(time.localtime().tm_min,
                             time.localtime().tm_sec)
        humidity = val.split(',')[0]
        temp = val.split(',')[1]
        print s,val
        
        x.append(i)
        i +=1
        y1.append(temp)
        y2.append(humidity)
        plt.cla()
        plt.title('Temperature Vs Humidity')    
        plt.plot(x, y2, label = "Temperature")
        plt.plot(x, y1, label = "Humudity")
        # show a legend on the plot
        plt.legend()
    
ani = animation.FuncAnimation(plt.gcf(), animate, interval=1000)
plt.tight_layout()
plt.show()
arduino.close()
