import psutil

print("===== SERVER HEALTH REPORT =====")

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent

print(f"CPU Usage: {cpu}%")
print(f"Memory Usage: {memory}%")
print(f"Disk Usage: {disk}%")

if cpu < 80 and memory < 80 and disk < 80:
    print("\nServer Status: HEALTHY")
else:
    print("\nServer Status: WARNING")
