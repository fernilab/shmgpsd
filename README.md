# shmgpsd

Get gpsd data via shared memory. You need to compile gpsd with shm and shared library support. More on that below.

## Compiling gpsd with shared memory and shared library support
```
git clone git://git.savannah.nongnu.org/gpsd.git # or https://gitlab.com/gpsd/gpsd.git
git checkout release-3.18
scons timeservice=yes magic_hat=yes nmea0183=yes ublox=yes mtk3301=yes fixed_port_speed=115200 fixed_stop_bits=1 shm_export=yes shared=yes
sudo scons install
```
## Usage
```Python 3.5.3 (default, Sep 27 2018, 17:25:39)
[GCC 6.3.0 20170516] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import shmgpsd
>>> mygps = shmgpsd.SHM()
>>> mygps.satellites_visible
12
>>> mygps.satellites_used
9
>>> for i in range(0, shmgpsd.MAXCHANNELS):
...   if mygps.skyview[i].PRN != 0:
...     print("PRN: {0}, SNR: {1}, USED: {2}".format(mygps.skyview[i].PRN,
...                                                  mygps.skyview[i].ss,
...                                                  mygps.skyview[i].used))
...
PRN: 16, SNR: 49.0, USED: True
PRN: 26, SNR: 34.0, USED: True
PRN: 23, SNR: 27.0, USED: True
PRN: 3, SNR: 47.0, USED: True
PRN: 31, SNR: 38.0, USED: True
PRN: 22, SNR: 49.0, USED: True
PRN: 48, SNR: 42.0, USED: False
PRN: 9, SNR: 40.0, USED: True
PRN: 14, SNR: 34.0, USED: True
PRN: 27, SNR: 39.0, USED: True
PRN: 29, SNR: 35.0, USED: True
PRN: 7, SNR: 27.0, USED: True
```
