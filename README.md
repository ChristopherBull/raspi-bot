# Raspberry Pi Robot

[![Continuous Integration](https://github.com/CaffeinatedAndroid/raspi-bot-node/workflows/Continuous%20Integration/badge.svg)](https://github.com/CaffeinatedAndroid/raspi-bot-node/actions?query=workflow%3A%22Continuous+Integration%22)
[![Test Coverage](https://api.codeclimate.com/v1/badges/2a024d6e9d18dc90e064/test_coverage.svg)](https://codeclimate.com/github/CaffeinatedAndroid/raspi-bot-node/test_coverage)
[![Maintainability](https://api.codeclimate.com/v1/badges/2a024d6e9d18dc90e064/maintainability.svg)](https://codeclimate.com/github/CaffeinatedAndroid/raspi-bot-node/maintainability)

This is a NodeJS and Python modular robot for the Raspberry PI.

Various forms of Machine Learning (ML) and Artificial Intelligence (AI) will be utilised in this project.

## Work-in-Progress

The plan is to allow various configurations and features that can be enabled based on the available hardware. Below are some examples of the intended functionality.

_Mobility support:_

- [ ] Differential wheeled robot (2-wheels)
- [ ] Steering motion (RWD, FWD, AWD, etc)
- [ ] Quadcopter (4 rotors) - if I find time, one can dream.

_Sensory support:_

- [x] [Object detection](rpi_bot/vision/) (camera + machine learning)
- [ ] Distance sensing (using HC-SR04)

_Feature support:_

- [ ] Follow/avoid object
- [ ] Auto-navigation

_Connectivity support:_

- [ ] WiFi (TCP & UDP)
- [ ] WiFi Direct
- [ ] Bluetooth
- [ ] Radio

_Control:_

- [ ] [Android app](https://github.com/CaffeinatedAndroid/raspi-bot-app)
