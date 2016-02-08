# -*- coding:utf-8 -*-
import abc
import platform
from UserList import UserList

class Monitor(object):
    @abc.abstractmethod
    def current(self):
        pass

    @abc.abstractmethod
    def percent(self, range):
        pass

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def max(self):
        pass

    @abc.abstractmethod
    def min(self):
        pass


class Monitors(UserList):
    @abc.abstractmethod
    def percent(self, range):
        pass

    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def max(self):
        pass

    @abc.abstractmethod
    def min(self):
        pass


def get_monitors():
        if platform.system() == "Windows":
            from .driver_win_wmi import WinWMIMonitors
            return WinWMIMonitors()
        elif platform.system() == "Darwin":
            from .driver_mac import MacMonitors
            return MacMonitors()
        elif platform.system() == "Linux":
            from .driver_linux import LinuxMonitors
            return LinuxMonitors()
        else:
            raise OSError()

