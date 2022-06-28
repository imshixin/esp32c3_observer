# esp32c3监控程序，电脑端

> 这是个简易版本，还有待改进

`main.py`: 主程序,需要使用管理员程序允许，否则可能获取不到cpu温度

`tray.py`: 托盘程序，目前还没实现

`LibreHardwareMonitorLib.dll`: 运行依赖，用于获取传感器信息
> 来自[github](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor)

硬件程序在[hardware分支](https://github.com/imshixin/esp32c3_observer/tree/hardware)

计划：

- [ ] 电脑端托盘程序
- [ ] tft显示优化或使用lvgl
- [ ] 支持使用数据线连接
> 正在持续更新中
