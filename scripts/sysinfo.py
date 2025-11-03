import platform, json, psutil, os, subprocess, time

def get_cpu_info():
    with open("/proc/cpuinfo", "r") as f:
        for line in f:
            if line.startswith("model name"):
                return line.split(":")[1].strip()
    return "Unknown"

def seconds_to_human(seconds):
    days = seconds // 86400
    seconds %= 86400
    hours = int(seconds // 3600)
    seconds %= 3600
    minutes = int(seconds // 60)
    seconds = int(seconds % 60)
    
    parts = []
    if days: parts.append(f"{days}d")
    if hours: parts.append(f"{hours}h")
    if minutes: parts.append(f"{minutes}m")
    if seconds or not parts: parts.append(f"{seconds}s")
    
    return " ".join(parts)

def get_network_interface():
    for iface, address in psutil.net_if_addrs().items():
        for addr in address:
            if addr.family == 2 and iface != "lo":  # AF_INET (IPv4) or AF_INET6 (IPv6)
                return iface,addr.address
    return None, None

def main():

    print("Collecting system information...")
    hostname = platform.node()
    cpu_name = get_cpu_info()
    cpu_core = psutil.cpu_count(logical=False)
    memory_gb = (psutil.virtual_memory().total.numerator / 1024**3).__ceil__()
    swap_gb = (psutil.swap_memory().total.numerator / 1024**3).__ceil__()
    disk_total = (psutil.disk_usage('/').total / 1024**3).__ceil__()
    disk_free = (psutil.disk_usage('/').free / 1024**3).__ceil__()
    network_interface_name, network_interface_ip = get_network_interface()
    uptime = seconds_to_human(time.time() - psutil.boot_time())

    merged_data = {}
    merged_data["hostname"] = hostname
    merged_data["cpu_name"] = cpu_name
    merged_data["cpu_core"] = cpu_core
    merged_data["memory"] = str(memory_gb)+"GB"
    merged_data["swap"] = str(swap_gb)+"GB"
    merged_data["disk_total"] = str(disk_total)+"GB"
    merged_data["disk_free"] = str(disk_free)+"GB"
    merged_data["uptime"] = uptime
    merged_data["network_interface_name"] = network_interface_name
    merged_data["network_interface_ip"] = network_interface_ip

    with open("data/system_info.json", "w") as f:
        json.dump(merged_data, f, indent=4)

    with open("data/system_info.ndjson", "a+") as f:
        json.dump({
            "hostname": hostname,
            "cpu_name": cpu_name,
            "cpu_core": cpu_core,
            "memory": str(memory_gb)+"GB",
            "swap": str(swap_gb)+"GB",
            "disk_total": str(disk_total)+"GB",
            "disk_free": str(disk_free)+"GB",
            "uptime": uptime,
            "network_interface_name": network_interface_name,
            "network_interface_ip": network_interface_ip
        }, f)
        f.write("\n")
        print("System information saved to data/system_info.json")


if __name__ == "__main__":
    main()