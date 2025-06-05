import platform
try:
    import psutil
except ImportError:
    print("The 'psutil' module is not installed. Please install it using 'pip install psutil'.")
    exit(1)

class SystemInfo:
    def get_platform_info(self):
        return {
            "system": platform.system(),
            "release": platform.release(),
            "version": platform.version(),
            "processor": platform.processor(),
            "cores": psutil.cpu_count(logical=False),
            "logical_cores": psutil.cpu_count(logical=True),
        }

    def get_memory_info(self):
        mem = psutil.virtual_memory()
        return {
            "total_gb": mem.total / (1024 ** 3),
            "available_gb": mem.available / (1024 ** 3),
            "used_gb": mem.used / (1024 ** 3),
        }

    def get_disk_info(self):
        disk = psutil.disk_usage('/')
        return {
            "total_gb": disk.total / (1024 ** 3),
            "used_gb": disk.used / (1024 ** 3),
            "free_gb": disk.free / (1024 ** 3),
        }

def print_info():
    info = SystemInfo()

    print("== Platform Info ==")
    for key, value in info.get_platform_info().items():
        print(f"{key.capitalize().replace('_', ' ')}: {value}")

    print("\n== Memory Info ==")
    for key, value in info.get_memory_info().items():
        print(f"{key.capitalize().replace('_', ' ')}: {value:.2f} GB")

    print("\n== Disk Info ==")
    for key, value in info.get_disk_info().items():
        print(f"{key.capitalize().replace('_', ' ')}: {value:.2f} GB")

if __name__ == "__main__":
    print_info()
