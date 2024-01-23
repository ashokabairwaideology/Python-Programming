#window version 

import wmi
data = wmi.WMI()
for os_name in data.Win32_operatingSystem():
     print(os_name.Caption)