import random
import time
import matplotlib.pyplot as plt

data = []

for i in range(10):
    value = random.randint(20, 50)  # simulate sensor data
    data.append(value)
    
    print("Sensor Value:", value)
    time.sleep(1)

plt.plot(data)
plt.title("IoT Sensor Data")
plt.xlabel("Time")
plt.ylabel("Value")
plt.show()
