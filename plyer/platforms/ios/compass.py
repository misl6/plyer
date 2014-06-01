'''
iOS Compass
---------------------
'''

from plyer.facades import Compass
from jnius import autoclass

Hardware = autoclass('org.renpy.Ios.Hardware')

class IosCompass(Compass):

    def __init__(self):
        super(IosAccelerometer, self).__init__()
        self.bridge = autoclass('bridge').alloc().init()
        self.bridge.motionManager.magnetometerUpdateInterval_(0.1)

    def _enable(self):
        self.bridge.startMagnetometerUpdates()

    def _disable(self):
        self.bridge.stopMagnetometerUpdates()

    def _get_orientation(self):
        return ( 
            self.bridge.mg_x,
            self.bridge.mg_y,
            self.bridge.mg_z)

def instance():
    return IosCompass()
