# sentinelsys

Sentinelsys is a Simple System Resource Monitor with Real-time Visualization


## Installation

```bash
pip install git+https://github.com/AryaWiratama26/sentinelsys.git
```

## Example
```python
from sentinelsys.monitor import Monitoring
from sentinelsys.visualizer import VisualizerRun

monitor = Monitoring()
print(f"CPU Usage {monitor.get_cpu_usage()}")
print(f"CPU Usage {monitor.get_memory_usage()}")
print(f"CPU Usage {monitor.get_disk_usage()}")

visulisasi = VisualizerRun()
visulisasi.plot_graph()
```

#### Author
- Name : Arya Wiratama <br>
- Email : <a href="mailto:aryawiratama2401@gmail.com">aryawiratama2401@gmail.com</a>