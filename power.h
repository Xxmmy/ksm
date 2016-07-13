#ifndef __POWER_H
#define __POWER_H

typedef struct _DEV_EXT {
	PVOID CbRegistration;
	PCALLBACK_OBJECT CbObject;
} DEV_EXT, *PDEV_EXT;

extern NTSTATUS register_power_callback(PDEV_EXT ext);
extern void deregister_power_callback(PDEV_EXT ext);

#endif
