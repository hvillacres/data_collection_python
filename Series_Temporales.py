import time
import serial
import numpy as np
import matplotlib.pyplot as plt

Examples = 50
COM = 'COM5'

try:
  arduinoSerial = serial.Serial(COM, 115200)
except:
  print('Cannot conect to the port')

#ACELERÓMETRO + GIROSCOPIO
numFeatures = 18

P =  np.zeros((Examples,numFeatures))

time.sleep(3)

print('Recolectando Datos')

with arduinoSerial:
  for k in range(Examples):
    for n in range(numFeatures):
      P[k,n] = arduinoSerial.readline().strip()
    print(k+1)

print('Datos Recolectados')
np.save('P10',P)

for i in range(numFeatures):
  fig = plt.figure()
  plt.bar(np.arange(0,Examples),P[:,i],label = 'Feature'+str(i+1))
  plt.legend(loc="upper left")
  plt.grid()

plt.show()
