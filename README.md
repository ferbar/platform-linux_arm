# Linux - arduino: development platform for [PlatformIO](http://platformio.org)

This fork of [linux_arm](http://platformio.org/platforms/linux_arm) intends to get arduino projects running (localy) on Linux with the help of RasPiArduino.

# Usage

1. [Install PlatformIO](http://platformio.org)
2. Create PlatformIO project and configure a platform option in [platformio.ini](http://docs.platformio.org/page/projectconf.html) file:

## Stable version

```ini
[env:linux_test]
board = generic_linux
build_flags =
    -DESPHOME_LOG_LEVEL=ESPHOME_LOG_LEVEL_DEBUG
    -DUSE_ARDUINO
    -DSERIAL_TO_CONSOLE
    -Wno-sign-compare
    -Wno-unused-but-set-variable
    -Wno-unused-variable
    -fno-exceptions
extra_scripts =
    post:post_build.py
framework = raspiarduino
lib_deps =
#   https://github.com/ferbar/RasPiArduino.git
lib_ldf_mode = off
platform = https://github.com/ferbar/platform-linux_arm.git#raspiarduino
...
```


