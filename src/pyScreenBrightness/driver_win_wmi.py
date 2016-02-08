# -*- coding:utf-8 -*-
import wmi
import platform
from UserList import UserList
from collections import OrderedDict
import warnings
from .base import Monitor, Monitors


class WinWMIMonitor(Monitor):
    def __init__(self, wmi, instance_name):
        self.wmi = wmi
        self.instance_name = instance_name

    @property
    def bn(self):
        for res in self.wmi.WmiMonitorBrightness():
            if res.InstanceName == self.instance_name:
                return res

    @property
    def bnm(self):
        for res in self.wmi.WmiMonitorBrightnessMethods():
            if res.InstanceName == self.instance_name:
                return res
        
    def __repr__(self):
        return "<WinMonitor:{!s}>".format(self.bn.InstanceName)

    def current(self):
        return self.bn.CurrentBrightness

    def max(self):
        return self.bnm.WmiSetBrightness(self.bn.level[-1], 0)

    def min(self):
        return self.bnm.WmiSetBrightness(self.bn.level[0], 0)

    def percent(self, range):
        assert 0 <= range <= 100, "out of percent range"
        return self.bnm.WmiSetBrightness(int(round(range)), 0)
    
    def reset(self):
        return self.bnm.WmiRevertToPolicyBrightness()
    

class WinWMIMonitors(Monitors):
    def __init__(self):
        if platform.system() != "Windows": raise OSError("at last is  vista")
        self.wmi = wmi.WMI(namespace="root/wmi")
        self.data = OrderedDict()
        for bn in self.wmi.WmiMonitorBrightness():
            self.data[bn.InstanceName] = WinWMIMonitor(self.wmi, bn.InstanceName)

    def __getitem__(self, k):
        if isinstance(k, int):
            return self.data[self.data.keys()[k]]
        elif isinstance(k, basestr):
            return self.data[k]
        else:
            raise KeyError("int or instance name, got {!r}".format(k))


    def __repr__(self):   
        return "<Monitors{!r}>".format(self.data.keys())

    def max(self):
        for k in self.data:
            self.data[k].max()

    def min(self):
        for k in self.data:
            self.data[k].min()

    def percent(self, percents):
        for k in self.data:
            self.data[k].percents(percents)

    def reset():
        for k in self.data:
            self.data[k].reset()


if __name__ == "__main__":
    monitors = WinWMIMonitors()
    print monitors
    print monitors[0]
    monitors.max()
    import time
    time.sleep(5)
    print monitors.min()
    time.sleep(5)
    print monitors.max()

