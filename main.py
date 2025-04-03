from sentinelsys import Monitoring
from sentinelsys import VisualizerRun

monitor = Monitoring()
print(f"CPU Usage {monitor.get_cpu_usage()}")
print(f"CPU Usage {monitor.get_memory_usage()}")
print(f"CPU Usage {monitor.get_disk_usage()}")

visulisasi = VisualizerRun()
visulisasi.plot_graph()
