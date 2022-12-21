import tkinter as tk
import time
import psutil
import wmi

# Connect to the WMI interface
c = wmi.WMI()

# Find the battery device
battery = None
for device in c.Win32_Battery():
    battery = device


def update_time():
    # Pobierz bieżący czas systemowy
    current_time = time.strftime("%I:%M:%S %p")

    # Wyświetl bieżący czas na etykiecie
    time_label.config(text=current_time)

    # Uaktualnij etykietę co sekundę
    time_label.after(1000, update_time)


def update_battery():
    # Pobierz informacje o baterii
    battery_state = psutil.sensors_battery()
    # Sprawdź, czy bateria jest podłączona do źródła zasilania
    if battery_state:
        if battery_state.power_plugged and 20 < battery_state.percent < 80:
            if not battery.Charging:
                change_battery_state(True)
            status = "Podłączona do źródła zasilania i ładuję"
        elif not battery_state.power_plugged:
            status = "Odłączona od źródła zasilania"
        else:
            if battery.Charging:
                change_battery_state(False)
            status = "Podłączona do źródła zasilania i nie ładuję"

        # Wyświetl stan naładowania baterii i informację o podłączeniu do źródła zasilania
        battery_label.config(text="Stan naładowania baterii: {}%\n{}".format(battery_state.percent, status))
    else:
        battery_label.config(text=f"{c.Win32_Battery()}")


def change_battery_state(state):
    battery.Charging = state
    battery.Put()


# Stwórz okno aplikacji
window = tk.Tk()
window.title("System Info")
window.geometry('400x100+100+100')
# Stwórz etykietę do wyświetlania bieżącego czasu
time_label = tk.Label(text="")
time_label.pack()

# Uaktualnij etykietę z bieżącym czasem
update_time()

# Stwórz etykietę do wyświetlania informacji o baterii
battery_label = tk.Label(text="")
battery_label.pack()

# Uaktualnij etykietę z informacjami o baterii
update_battery()

# Uruchom pętlę główną
window.mainloop()
