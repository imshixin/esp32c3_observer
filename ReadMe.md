# esp32c3监控程序，电脑端

# 使用
更改`main.py`中`wifi_main`函数下的`addr`

以管理员权限运行`python main.py`即可，需要电脑和esp32在同一局域网

----

# 其他
`main.py`: 主程序,需要使用管理员程序运行，否则可能获取不到cpu温度

`LibreHardwareMonitorLib.dll`: 运行依赖，用于获取传感器信息
> 来自[LibreHardwareMonitor](https://github.com/LibreHardwareMonitor/LibreHardwareMonitor)

硬件程序在[hardware分支](https://github.com/imshixin/esp32c3_lvgl_observer)


# 部分数据无法读取

在`main.py`中作如下更改以适配自己的电脑


 把这里注释改掉，放if上面去，再运行一下
![yuy_22-07-12_19 15](https://user-images.githubusercontent.com/36874714/180641056-834319d0-042c-48e0-8515-cedf9d646c80.png)

数据有如下对应关系
![yuy_22-07-12_19 20](https://user-images.githubusercontent.com/36874714/180641080-1af0c305-8060-41d2-9871-63f120574e3b.png)

对照自己电脑找找需要的参数把上面的self.observe_types 改改
![yuy_22-07-12_19 17_0](https://user-images.githubusercontent.com/36874714/180641081-9144f436-8aeb-4838-a4ea-1e6cf06b534d.png)

 大概就可以了，我的是AMD的CPU，所以可能会不一样




# 计划：

- [x] tft显示优化或使用lvgl
- [ ] 支持使用数据线连接
> 正在缓慢更新中
