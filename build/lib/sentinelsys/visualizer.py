import time
import matplotlib.pyplot as plt
import psutil

class VisualizerRun:
    def __init__(self, interval=1):
        self.interval = interval
        self.cpu_data = []
        self.ram_data = []
        self.disk_data = []
        self.timestamps = []
        
    def update_data(self):
        """Update all of data"""
        self.cpu_data.append(psutil.cpu_percent(interval=0.5))
        self.ram_data.append(psutil.virtual_memory().percent)
        self.disk_data.append(psutil.disk_usage('/').percent)
        self.timestamps.append(time.time())
        
        
        if len(self.cpu_data) > 50:
            self.cpu_data.pop(0)
            self.ram_data.pop(0)
            self.disk_data.pop(0)
            self.timestamps.pop(0)
            
    def plot_graph(self):
        plt.ion()
        fig, ax = plt.subplots(3, 1, figsize=(8, 6))
        
        while True:
            self.update_data()
            
            ax[0].cla()
            ax[0].plot(self.timestamps, self.cpu_data, label="CPU Usage (%)", color='r')
            ax[0].set_title("CPU Usage")
            ax[0].set_ylim(0, 100)
            ax[0].legend()

            ax[1].cla()
            ax[1].plot(self.timestamps, self.ram_data, label="RAM Usage (%)", color='g')
            ax[1].set_title("RAM Usage")
            ax[1].set_ylim(0, 100)
            ax[1].legend()

            ax[2].cla()
            ax[2].plot(self.timestamps, self.disk_data, label="Disk Usage (%)", color='b')
            ax[2].set_title("Disk Usage")
            ax[2].set_ylim(0, 100)
            ax[2].legend()

            plt.pause(self.interval)