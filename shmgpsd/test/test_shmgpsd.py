import shmgpsd
mygps = shmgpsd.SHM()
for i in range(0, shmgpsd.MAXCHANNELS):
    if mygps.skyview[i].PRN != 0:
        print(f"PRN: {mygps.skyview[i].PRN:4}, " \
              f"SNR: {mygps.skyview[i].ss:4}, "  \
              f"USED: {mygps.skyview[i].used:4}"  )



print(f"Satellites visible: {mygps.satellites_visible:2}")
print(f"Satellites used:    {mygps.satellites_used:2}")
