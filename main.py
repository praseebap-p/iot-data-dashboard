import random
import time
import matplotlib.pyplot as plt

data = []

plt.ion()

for i in range(20):
    value = random.randint(20, 50)
    data.append(value)

    plt.clf()
    plt.plot(data)
    plt.title("Real-Time IoT Data")
    plt.pause(0.5)

    print("Sensor:", value)
