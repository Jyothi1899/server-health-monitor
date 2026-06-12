import psutil
import socket
from datetime import datetime
hostname = socket.gethostname()
current_time = datetime.now()


cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent


print("=" * 40)
print("SERVER HEALTH REPORT")
print("=" * 40)

print(f"Hostname      : {hostname}")
print(f"Timestamp     : {current_time}")

print("\nSystem Metrics")
print("-" * 40)

print(f"CPU Usage     : {cpu}%")
print(f"Memory Usage  : {memory}%")
print(f"Disk Usage    : {disk}%")

print("\nHealth Checks")
print("-" * 40)

warning = False

if cpu > 80:
    print("WARNING: High CPU Usage")
    warning = True

if memory > 80:
    print("WARNING: High Memory Usage")
    warning = True

if disk > 80:
    print("WARNING: High Disk Usage")
    warning = True

if not warning:
    print("All system metrics are within safe limits.")

print("\nOverall Status")
print("-" * 40)

if warning:
    print("SERVER STATUS: WARNING")
else:
    print("SERVER STATUS: HEALTHY")

print("=" * 40)
