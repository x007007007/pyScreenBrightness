#pyScreenBrightness#

`
import pyScreenBrightness
monitors = pyScreenBrightness.get_monitors()  # get screen brightness controller handle, return monitors object
monitors.percent(10)
monitors.reset()
monitors.max()
monitors.min()

for monitor in monitors:
    print monior.current()
`

##Moonitors Object##

Monitors object is a subclass of UserList and have methods to batch action of monitor objects


##Monitor Object##

