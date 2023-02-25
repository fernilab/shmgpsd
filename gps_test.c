#include <stddef.h>
#include <stdio.h>
#include <gps.h>

int main() {
	struct gps_data_t gps_data;
	printf("Devices: %d\n", offsetof(struct gps_data_t, devices));
	printf("Privdata: %d\n", offsetof(struct gps_data_t, privdata));

	printf("%d\n", sizeof(struct rtcm2_t));
        printf("%d\n", sizeof(struct rtcm3_t));
        printf("%d\n", sizeof(struct subframe_t));
        printf("%d\n", sizeof(struct ais_t));
        printf("%d\n", sizeof(struct attitude_t));
        printf("%d\n", sizeof(struct navdata_t));
        printf("%d\n", sizeof(struct rawdata_t));
        printf("%d\n", sizeof(struct gst_t));
        printf("%d\n", sizeof(struct oscillator_t));
        printf("%d\n", sizeof(struct version_t));
        printf("%d\n", sizeof(char) * 256);
        printf("%d\n", sizeof(struct timedelta_t));
        printf("%d\n", sizeof(struct timedelta_t));
}
