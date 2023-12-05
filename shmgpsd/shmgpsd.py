import ctypes as ct
import sys

GPSD_SHM_KEY = 0x47505344
SHM_RDONLY   = 0x010000

MAXCHANNELS  = 140
MAXUSERDEVS  =   4
GPS_PATH_MAX = 128
HEXDATA_MAX  = 512

gpsd    = ct.CDLL( 'libgps.so.28.0.0' )
librt   = ct.CDLL( 'librt.so.1', use_errno=True )

gps_mask_t  = ct.c_uint64
time_t      = ct.c_uint64

class timespec_t( ct.Structure ):
  _fields_ = [ ( "tv_sec",  time_t    ),
               ( "tv_nsec", ct.c_long ) ]

class ecef_t( ct.Structure ):
  _fields_ = [ ( "x",    ct.c_double ),
               ( "y",    ct.c_double ),
               ( "z",    ct.c_double ),
               ( "pAcc", ct.c_double ),
               ( "vx",   ct.c_double ),
               ( "vy",   ct.c_double ),
               ( "vz",   ct.c_double ),
               ( "vAcc", ct.c_double ) ]

class ned_t( ct.Structure ):
  _fields_ = [ ( "relPosN", ct.c_double ),
               ( "relPosE", ct.c_double ),
               ( "relPosD", ct.c_double ),
               ( "relPosL", ct.c_double ),
               ( "relPosH", ct.c_double ),
               ( "velN",    ct.c_double ),
               ( "velE",    ct.c_double ),
               ( "velD",    ct.c_double ) ]

class timedelta_t( ct.Structure ):
  _fields_ = [ ( "real",  timespec_t ),
               ( "clock", timespec_t ) ]

class gps_log_t( ct.Structure ):
  _fields_ = [ ( "lon",           ct.c_double     ),
               ( "lat",           ct.c_double     ),
               ( "altHAE",        ct.c_double     ),
               ( "altMSL",        ct.c_double     ),          
               ( "gSpeed",        ct.c_double     ),
               ( "heading",       ct.c_double     ),
               ( "tAcc",          ct.c_double     ),
               ( "hAcc",          ct.c_double     ),
               ( "vAcc",          ct.c_double     ),
               ( "sAcc",          ct.c_double     ),
               ( "headAcc",       ct.c_double     ),
               ( "velN",          ct.c_double     ),
               ( "velE",          ct.c_double     ),
               ( "velD",          ct.c_double     ),
               ( "pDOP",          ct.c_double     ),
               ( "distance",      ct.c_double     ),
               ( "totalDistance", ct.c_double     ),
               ( "distanceStd",   ct.c_double     ),
               ( "then",          timespec_t      ),
               ( "status",        ct.c_int        ),
               ( "index_cnt",     ct.c_uint32     ),
               ( "fixType",       ct.c_char       ),
               ( "numSV",         ct.c_ubyte      ),
               ( "string",        ct.c_char * 257 ) ]

class gps_fix_t( ct.Structure ):
  _fields_ = [ ( "time",           timespec_t     ),
               ( "mode",           ct.c_int       ),
               ( "status",         ct.c_int       ),
               ( "ept",            ct.c_double    ),      
               ( "latitude",       ct.c_double    ),
               ( "epy",            ct.c_double    ),
               ( "longitude",      ct.c_double    ),
               ( "epx",            ct.c_double    ),
               ( "altitude",       ct.c_double    ),
               ( "altHAE",         ct.c_double    ),
               ( "altMSL",         ct.c_double    ),
               ( "epv",            ct.c_double    ), 
               ( "track",          ct.c_double    ),
               ( "epd",            ct.c_double    ),
               ( "speed",          ct.c_double    ), 
               ( "eps",            ct.c_double    ),
               ( "climb",          ct.c_double    ),
               ( "epc",            ct.c_double    ),
               ( "eph",            ct.c_double    ),
               ( "sep",            ct.c_double    ),
               ( "geoid_sep",      ct.c_double    ),
               ( "magnetic_track", ct.c_double    ),
               ( "magnetic_var",   ct.c_double    ),
               ( "depth",          ct.c_double    ),
               ( "ecef",           ecef_t         ),
               ( "NED",            ned_t          ),
               ( "datum",          ct.c_char * 40 ),
               ( "dpgs_age",       ct.c_double    ),
               ( "dgps_station",   ct.c_int       ),
               ( "wanglem",        ct.c_double    ),
               ( "wangler",        ct.c_double    ),
               ( "wanglet",        ct.c_double    ),
               ( "wspeedr",        ct.c_double    ),
               ( "wspeedt",        ct.c_double    ) ]

class dop_t( ct.Structure ):
  _fields_ = [ ( "xdop", ct.c_double ),
               ( "ydop", ct.c_double ),
               ( "pdop", ct.c_double ),
               ( "hdop", ct.c_double ),
               ( "vdop", ct.c_double ),
               ( "tdop", ct.c_double ),
               ( "gdop", ct.c_double ) ]

class satellite_t( ct.Structure ):
  _fields_ = [ ( "ss",        ct.c_double ),
               ( "used",      ct.c_bool   ),
               ( "PRN",       ct.c_short  ),
               ( "elevation", ct.c_double ),
               ( "azimuth",   ct.c_double ),
               ( "gnssid",    ct.c_ubyte  ),
               ( "svid",      ct.c_ubyte  ),
               ( "sigid",     ct.c_ubyte  ),
               ( "freqid",    ct.c_char   ),
               ( "health",    ct.c_ubyte  ) ]

class devconfig_t( ct.Structure ):
  _fields_ = [ ( "path",        ct.c_char * GPS_PATH_MAX ),
               ( "flags",       ct.c_int                 ),
               ( "driver",      ct.c_char * 64           ),
               ( "subtype",     ct.c_char * 128          ),
               ( "subtype1",    ct.c_char * 128          ),
               ( "hexdata",     ct.c_char * HEXDATA_MAX  ),
               ( "activated",   timespec_t               ),
               ( "baudrate",    ct.c_uint                ),
               ( "stopbits",    ct.c_uint                ),
               ( "parity",      ct.c_char                ),
               ( "cycle",       timespec_t               ),
               ( "minicycle",   timespec_t               ),
               ( "driver_mode", ct.c_int                 ) ]

class gps_policy_t( ct.Structure ):
  _fields_ = [ ( "watcher",  ct.c_bool                ),
               ( "json",     ct.c_bool                ),
               ( "nmea",     ct.c_bool                ),
               ( "raw",      ct.c_int                 ),
               ( "scaled",   ct.c_bool                ),
               ( "timing",   ct.c_bool                ),
               ( "split24",  ct.c_bool                ),
               ( "pps",      ct.c_bool                ),
               ( "loglevel", ct.c_int                 ),
               ( "devpath",  ct.c_char * GPS_PATH_MAX ),
               ( "remote",   ct.c_char * GPS_PATH_MAX ) ]

class devices_t( ct.Structure ):
  _fields_ = [ ( "time",     timespec_t                ),
               ( "ndevices", ct.c_int                  ),
               ( "list",     devconfig_t * MAXUSERDEVS ) ]

class gps_data_t( ct.Structure ):
  _fields_ = [ ( "set",                gps_mask_t                ),
               ( "online",             timespec_t                ), 
               ( "gps_fd",             ct.c_int                  ),
               ( "fix",                gps_fix_t                 ),
               ( "log",                gps_log_t                 ),
               ( "leap_seconds",       ct.c_int                  ),
               ( "satellites_used",    ct.c_int                  ),
               ( "dop",                dop_t                     ),
               #( "epe",                ct.c_double               ),
               ( "skyview_time",       timespec_t                ),
               ( "satellites_visible", ct.c_int                  ),
               ( "skyview",            satellite_t * MAXCHANNELS ),
               ( "dev",                devconfig_t               ),
               ( "policy",             gps_policy_t              ),
               ( "devices",            devices_t                 ),
               ( "gps_data_union",     ct.c_byte * 6240          ), 
               ( "toff",               timedelta_t               ), 
               ( "pps",                timedelta_t               ), 
               ( "qErr",               ct.c_long                 ),
               ( "qErr_time",          timespec_t                ), 
               ( "privdata",           ct.c_void_p               ) ]

class shmexport_t( ct.Structure ):
  _fields_ = [ ( "bookend1", ct.c_int   ),
               ( "gpsdata",  gps_data_t ), 
               ( "bookend2", ct.c_int   ) ]

def SHM():
  librt.shmget.restype  = ct.c_int
  librt.shmget.argtypes = [ ct.c_int, ct.c_size_t, ct.c_int ]
  librt.shmat.restype  = ct.c_void_p
  librt.shmat.argtypes = [ ct.c_int, ct.c_void_p, ct.c_int ]

  shmexport_p = ct.POINTER( shmexport_t )

  # We just need to read so no permissions needed.
  shmid = librt.shmget( GPSD_SHM_KEY, 0, 0 )
  if shmid == -1:
    c_errno = ct.get_errno()
    print( "shmget failed with errno: {0}".format( c_errno ) )
    sys.exit( c_errno )
  shm = librt.shmat( shmid, 0, SHM_RDONLY )
  if shm == -1:
    c_errno = ct.get_errno()
    print( "shmat failed with errno: {0}".format( c_errno ) )
    sys.exit( c_errno )

  # Both shared memory functions worked, so let's cast it.
  cast_p = ct.cast( shm, shmexport_p )

  # Return this so we don't have to type the whole struct down
  # to get information.
  return cast_p.contents.gpsdata
