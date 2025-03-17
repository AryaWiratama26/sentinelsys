import psutil

class Monitoring:
    def __init__(self):
        pass
        
    def get_cpu_usage(self):
        """return : cpu_percent with interval 1"""
        return psutil.cpu_percent(interval=1)
    
    def get_memory_usage(self):
        """return : virtual_memory with GB"""
        ram = psutil.virtual_memory()
        return ram.percent, ram.total / (1024 ** 3)
    
    def get_disk_usage(self):
        """return : disk_usage with percent"""
        return psutil.disk_usage('/').percent

