# snort-conf

## Description
By default Snort on Windows comes with Linux paths, different library names and relatively bad default configuration. This is a configuration to get Snort 2 (2.9) up and running in no time. This guide assumes that Snort is or will be installed in C:\Snort, if your path is different - please make the necessary adjustment.

## Instructions
Install Snort 2:
https://snort.org/downloads

Install WinPCap:
https://www.winpcap.org/install/default.htm

Download and replace config file located in C:\Snort\etc\snort.conf

Download and replace rules folder located in C:\Snort\ path

You can also get some nice community rules (optional)

Start your terminal as administrator and type:
```cd C:\Snort\bin```

Determine your interface with:
```snort -W```

Start Snort on first (or whatever number yours is) interface:
```snort -i 1 -c C:\Snort\etc\snort.conf -A console```
