
# IT System Information Tool 
import tkinter as tk
import platform
import socket
import os
import time
import importlib

root = tk.Tk()
root.title("System Information")
root.geometry("900x600")
root.configure(bg="#1e1e2f")

def get_gpu_temperature():
    try:
        import clr
        import os

        base_dir = os.path.dirname(os.path.abspath(__file__))
        lhm_dir = os.path.join(base_dir, "LibreHardwareMonitor")
        dll_path = os.path.join(lhm_dir, "LibreHardwareMonitorLib.dll")

        if not os.path.exists(dll_path):
            return "Unavailable - LibreHardwareMonitorLib.dll not found"

        clr.AddReference(str(dll_path))
        from LibreHardwareMonitor.Hardware import Computer, SensorType

        computer = Computer()
        computer.IsGpuEnabled = True
        computer.Open()

        gpu_temp = None

        for hardware in computer.Hardware:
            hardware.Update()

            hardware_name = str(hardware.Name).lower()
            hardware_type = str(hardware.HardwareType).lower()

            for sensor in hardware.Sensors:
                if sensor.SensorType == SensorType.Temperature and sensor.Value is not None:
                    sensor_name = str(sensor.Name).lower()
                    value = float(sensor.Value)

                    if value <= 0:
                        continue

                    if "gpu" in hardware_name or "gpu" in hardware_type:
                        computer.Close()
                        return f"{value:.1f} °C"

                    if gpu_temp is None:
                        gpu_temp = value

            for subhardware in hardware.SubHardware:
                subhardware.Update()

                sub_name = str(subhardware.Name).lower()
                sub_type = str(subhardware.HardwareType).lower()

                for sensor in subhardware.Sensors:
                    if sensor.SensorType == SensorType.Temperature and sensor.Value is not None:
                        sensor_name = str(sensor.Name).lower()
                        value = float(sensor.Value)

                        if value <= 0:
                            continue

                        if "gpu" in sub_name or "gpu" in sub_type:
                            computer.Close()
                            return f"{value:.1f} °C"

                        if gpu_temp is None:
                            gpu_temp = value

        computer.Close()

        if gpu_temp is not None:
            return f"{gpu_temp:.1f} °C"

        return "Unavailable - no GPU temp sensor found"

    except Exception as e:
        return f"Unavailable - error: {e}"


def grab_ip_address():
    try:
        return socket.gethostbyname(socket.gethostname())
    except:
        return "N/A ...... Maybe try and run ADMIN ????"

# system info
def system_info():
    GPU_TEMP = get_gpu_temperature()
    IP_ADDRESS = grab_ip_address()
    info = f"""
    System: {platform.system()}
    System Type: {platform.system()}
    System Model: {platform.machine()}
    OS VERSION: {platform.platform()}

    Registered User: {os.getlogin()}
    Node Name: {platform.node()}

    Release: {platform.release()}
    Version: {platform.version()}
    Machine: {platform.machine()}
    Processor: {platform.processor()}

    IP Address: {IP_ADDRESS}
    Subnet Mask: N/A
    Default Gateway: N/A
    Network Card: N/A
    Hyper-V: N/A
    Time Zone: {time.tzname[0]}

    BIOS: N/A
    Windows Directory: {os.environ.get('WINDIR', 'N/A')}
    System Directory: {os.path.join(os.environ.get('WINDIR', 'C:\\Windows'), 'System32')}

    GPU Temperature: {GPU_TEMP}


"""
 
    info_box.config(state="normal")
    info_box.delete("1.0", tk.END)
    info_box.insert(tk.END, info)
    info_box.config(state="disabled")


title_label = tk.Label(
    root,
    text="System Information",
    font=("Arial", 20, "bold"),
    fg="#ffffff",
    bg="#1e1e2f"
)
title_label.pack(pady=15)

info_box = tk.Text(
    root,
    font=("Courier New", 11),
    bg="#2b2b3c",
    fg="#00ffcc",
    insertbackground="white",
    bd=2,
    relief="groove",
    wrap="word",
    padx=15,
    pady=15
)
info_box.pack(padx=20, pady=10, fill="both", expand=True)
info_box.insert("1.0", "Click the button to show system info")
info_box.config(state="disabled")

show_button = tk.Button(
    root,
    text="Show System Info",
    command=system_info,
    font=("Arial", 12, "bold"),
    bg="#4CAF50",
    fg="white",
    activebackground="#45a049",
    activeforeground="white",
    padx=10,
    pady=8,
    relief="flat",
    cursor="hand2"
)
show_button.pack(pady=15)

root.mainloop()
