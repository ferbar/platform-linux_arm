# Copyright 2021-present PlatformIO <contact@platformio.org>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
RasPiArduino
Arduino Framework for RaspberryPI 

https://github.com/me-no-dev/RasPiArduino
"""

from os.path import join, isdir

from SCons.Script import DefaultEnvironment, SConscript


env = DefaultEnvironment()
board = env.BoardConfig()

FRAMEWORK_DIR = env.PioPlatform().get_package_dir("framework-raspiarduino")
assert isdir(FRAMEWORK_DIR)

#print("=================")
#print(board)
# build_core = board.get("build.core", "").lower()
#variant= board.get("build.variant", "").lower()

#print(env)
#print("10=================")
#print(env.Dump())
#print("20=================")

env.Replace(
    CPPFLAGS=[
#        "-O2",
        "-O0",
        "-g",
        "-rdynamic",
        "-Wformat=2",
        "-Wall",
        "-Winline",
        "-pipe",
        "-fPIC"
    ],

    LIBS=["pthread"]
)

env.Append(
    CPPDEFINES=[
        "_GNU_SOURCE"
    ],

    CPPPATH=[
        join(env.PioPlatform().get_package_dir(
             "framework-raspiarduino"), "cores/piduino")
    ]
)


#
# Target: Build Core Library
#

libs = []
libs.append(env.BuildLibrary(
    join("$BUILD_DIR", "FrameworkRasPiArduino"),
    join(env.PioPlatform().get_package_dir("framework-raspiarduino"), "cores/piduino")
))

# from framework-arduinoespressif32/tools/platformio-build.py
variants_dir = join(FRAMEWORK_DIR, "variants")
if "build.variants_dir" in env.BoardConfig():
    variants_dir = join("$PROJECT_DIR", env.BoardConfig().get("build.variants_dir"))

if "build.variant" in env.BoardConfig():
    env.Append(
        CPPPATH=[
            join(variants_dir, env.BoardConfig().get("build.variant"))
        ]
    )
    libs.append(env.BuildLibrary(
        join("$BUILD_DIR", "FrameworkRasPiArduinoVariant"),
        join(variants_dir, env.BoardConfig().get("build.variant"))
))

env.Append(LIBS=libs)
