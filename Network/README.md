# Description

## Files
|name|note|
|----|----|
|udp_GS.py|Simulation of Ground Station|
|udp_RP.py|Simulation of Raspberry Pi zero board for SC-Sat1|
|udp_GS_timeout.py|(under development) Update file for `udp_GS.py`This include timeout function.|
|udp_GS_EOT.py|(under development) Update file for `udp_GS.py` This includes handshake or error detection function|

## How to use

1. Activate `udp_GS/py` on your laptop and `udp_RP.py` on your Raspberry Pi zero.
2. Type `A` to capture. Type `j` to capture `.jpg`, `r` to capture `.raw`, `n` to quit capturing countinuously.
3. Type `B` to get HK data or type `C` to reboot Raspberry Pi Zero (under development)

## Command list
|data|note|C/R/U/D|
|:----:|----|:----:|
|A|Capture .jpg/.raw|C|
|B|Read HK|R|
|C|Reboot|--|
||||

