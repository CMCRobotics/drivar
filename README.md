# Drivar
[![IDE Version](https://jitpack.io/v/chibyhq/chiby-ide.svg)](https://jitpack.io/#chibyhq/chiby-ide) 
[![GitHub Actions Status](https://github.com/chibyhq/chiby-ide/workflows/Java%20CI/badge.svg)](https://github.com/chibyhq/chiby-ide/actions)
[![Java 11](https://img.shields.io/badge/Java-11-green "Java 11")](https://java.com)

[<img style="background-color: rgba(0, 0, 0, 0.0470588);"
src="http://cmcrobotics.github.io/raspbuggy/images/rb-banner-147e2ba19ca3551c2b7cc049e823c7bf.png">](http://cmcrobotics.github.io/raspbuggy)

Drivar a **hardware abstraction layer for a collection of wifi programmable RC cars**, such as the [GianoPi holonomic car](http://github.com/stefsaladino/GianoPi) or the [Raspbuggy](http://cmcrobotics.github.io/raspbuggy) and a variety of hardware control adapters (Pimoroni Explorer HAT, Push-pull drivers, Adafruit DC Motor, Lego Mindstorm).

It comes with :

* A low-level Python abstraction library
* Various concrete implementations
  * MQTT Paho (Python + Brython/Javascript)
  * Microbit Kitronic Bitbot
  * Pimoroni Explorer HAT
  * Adafruit DC Motor
  * NXT Lego Mindstorm
* A Jupyter Notebook setup example, showing you how to control cars interactively
* (in preparation) A Webjar package providing Google Blockly block definitions for Python scripts generation.

Drivar is used by :

* The [Raspbuggy project](http://cmcrobotics.github.io/raspbuggy)
* The [GianoPi project](http://github.com/stefsaladino/GianoPi)


## How to build the package

The Drivar package uses Apache Maven to package (using distutils under the cover).
The release is currently done via setup.py and pypi like so :

```
mvn clean package
cd target/py/setup.py
python sdist bdist_egg upload -r pypi
```

