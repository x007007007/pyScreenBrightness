# -*- coding:utf-8 -*-
import win32api
from ctypes import *
from ctypes.wintypes import BOOL, HMONITOR, HDC, RECT, LPARAM, DWORD, BYTE, WCHAR, HANDLE
from collections import OrderedDict
import warnings


_MONITOR_ENUM_PROC = WINFUNCTYPE(BOOL, HMONITOR, HDC, POINTER(RECT), LPARAM)
class _PHYSICAL_MONITOR(Structure):
    _fields_ = [
        ('handle', HANDLE), 
        ('description', WCHAR * 128)
    ]


monitors = []
def callback(hmonitor, hdc, lprect, lparam):
    print hmonitor, hdc, lprect, lparam
    monitors.append(hmonitor)
    count = DWORD()
    if not windll.dxva2.GetNumberOfPhysicalMonitorsFromHMONITOR(hmonitor, byref(count)):
        print("Err {}".format(windll.kernel32.GetLastError()))
        raise WinError("GetNumberOfPhysicalMonitorsFromHMONITOR failed")
    print count.value
    physical_array = (_PHYSICAL_MONITOR * count.value)()
    if not windll.dxva2.GetPhysicalMonitorsFromHMONITOR(hmonitor, count.value, physical_array):
        print("Err {}".format(windll.kernel32.GetLastError()))
        raise WinError("GetPhysicalMonitorsFormHMONITOR failed")

    for physical in physical_array:
        pdwMC = DWORD(0)
        pdwSC = DWORD(0)
        if windll.dxva2.GetMonitorCapabilities(physical.handle, byref(pdwMC), byref(pdwSC)):
            print pdwMC, pdwSC
            max_bn = DWORD(0)
            min_bn = DWORD(0)
            cur_bn = DWORD(0)
            print physical, physical.handle
            if not windll.dxva2.SetMonitorBrightness(physical.handle, c_int(6)):
                print("Err {}".format(windll.kernel32.GetLastError()))
                raise WinError("SetMonitorBrightness failed")
            if not windll.dxva2.GetMonitorBrightness(hmonitor, byref(max_bn), byref(cur_bn), byref(min_bn)):
                raise WinError("GetMonitorBrightness failed")
            
            if not windll.dxva2.DestroyPhysicalMonitor(hmonitor):
                raise WinError("DestroyPhysicalMonitor failed")
        else:
            pass
            
    return True


#if not windll.user32.EnumDisplayMonitors(None, None, _MONITOR_ENUM_PROC(callback), None):
#    raise WinError("EnumDisplayMonitors failed")


