# -*- coding:utf-8 -*-
from .base import Monitor, Monitors
from ctypes import *

class MacMonitor(Monitor):
    def min(self):
        pass

    def max(self):
        pass

    def current(self):
        pass

    def reset(self):
        pass

    def percents(self, range):
        pass


class MacMonitors(Monitors):
    def __init__(self):
        pass

    def max(self):
        pass

    def min(self):
        pass

    def percents(self, range):
        pass

    def reset(self):
        pass


