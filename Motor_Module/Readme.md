# Basic Motion of Bot using Jetson Nano and L298N PWM Motor
## Steps:
### - Hardware:
1. Jetson Nano
2. L298N Motor driver
3. 2 BO Motor

  ![Hardware Connection](https://miro.medium.com/max/1400/1*50E_bUkwW4bjzvkRvOb7Lw.jpeg)
### - Software:
1. Open terminal and run following Commands:
```
$ sudo find /opt/nvidia/jetson-io/ -mindepth 1 -maxdepth 1 -type d -exec touch {}/__init__.py \;
$ sudo mkdir /boot/dtb
$ sudo cp -v /boot/tegra210-p3448-0000-p3449-0000-[ab]0[012].dtb /boot/dtb/
$ sudo /opt/nvidia/jetson-io/jetson-io.py
```
2. Follow this for activating PWM pins in Jetson Nano - [Link](https://docs.nvidia.com/jetson/archives/l4t-archived/l4t-3231/index.html#page/Tegra%2520Linux%2520Driver%2520Package%2520Development%2520Guide%2Fhw_setup_jetson_io.html)


# Demo
Run the `robot.py` file in terminal.
