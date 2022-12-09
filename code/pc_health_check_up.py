#!/usr/bin/env python3

#above line is a shebang

import shutil #in-built library for getting disk/storage details
import psutil #in-built library for getting cpu details

def is_disk_usage_safe(disk):
    du = shutil.disk_usage(disk)
    free = du.free / du.total * 100
    return free > 20

def is_cpu__usage_safe():
    usage = psutil.cpu_percent(1)
    return usage < 75

if  not is_disk_usage_safe("/") or not is_cpu__usage_safe():
    print("Your PC is in danger")
else:
    print("Your PC is safe, Nothing to worry")
