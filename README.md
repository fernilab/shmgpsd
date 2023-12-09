# ShmGpsD: Shared Memory GPSD Reader

ShmGpsD reads GPS data from shared memory-enabled GPSD instances, designed for seamless integration with InfluxDB via Telegraf exec inputs (JSON). Ideal for real-time updates and effortless communication with GPSD.

## Key Features:

- Read GPS data efficiently from shared memory
- Perfect for integrating GPS data into InfluxDB via Telegraf
- Streamlined solution for applications requiring precise GPS information

Elevate your applications with ShmGpsD – simplicity meets accuracy.

## Compiling gpsd: Optional (Only if OS distro lacks shared memory support)

```
git clone git://git.savannah.nongnu.org/gpsd.git # or https://gitlab.com/gpsd/gpsd.git
git checkout release-3.18
scons timeservice=yes magic_hat=yes nmea0183=yes ublox=yes mtk3301=yes fixed_port_speed=115200 fixed_stop_bits=1 shm_export=yes shared=yes
sudo scons install
```

## Usage
```
Python 3.11.2 (main, Mar 13 2023, 12:18:29) [GCC 12.2.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> import shmgpsd
>>> mygps = shmgpsd.SHM()
>>> for i in range(0, shmgpsd.MAXCHANNELS):
...     if mygps.skyview[i].PRN != 0:
...         print(f"PRN: {mygps.skyview[i].PRN:4}, " \
...               f"SNR: {mygps.skyview[i].ss:4}, "  \
...               f"USED: {mygps.skyview[i].used:4}"  )
...
PRN:   19, SNR: 18.0, USED:    1
PRN:   22, SNR: 28.0, USED:    1
PRN:   17, SNR: 21.0, USED:    1
PRN:    6, SNR: 31.0, USED:    1
PRN:   14, SNR: 33.0, USED:    1
PRN:   24, SNR: 17.0, USED:    1
PRN:    3, SNR: 15.0, USED:    1
PRN:   46, SNR: 29.0, USED:    0
PRN:   11, SNR: 24.0, USED:    1
PRN:   12, SNR: 20.0, USED:    0
PRN:   30, SNR:  0.0, USED:    0
>>> print(f"Satellites visible: {mygps.satellites_visible:2}")
Satellites visible: 11
>>> print(f"Satellites used:    {mygps.satellites_used:2}")
Satellites used:     8
```
