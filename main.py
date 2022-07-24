import time, socket, serial, clr
from pathlib import Path


class Observer:

  def __init__(self) -> None:
    clr.AddReference(str(Path(__file__).parent.absolute() / 'LibreHardwareMonitorLib.dll'))
    from LibreHardwareMonitor.Hardware import Computer
    self.computer = Computer()
    self.computer.IsCpuEnabled = True
    self.computer.IsGpuEnabled = True
    self.computer.Open()
    self.observe_types = (
        ('cpu load', 'CPU Total', 'load'),
        ('cpu temp', 'Core (Tctl/Tdie)', 'temperature'),
        ('gpu load', 'GPU Core', 'load'),
        ('gpu temp', 'GPU Core', 'temperature'),
    )
    """ self.observe_types = (
        (
            'cpu占用',
            'cpu温度',
            'gpu占用',
            'gpu温度',
        ),
        (
            'CPU Total',
            'Core (Tctl/Tdie)',
            'GPU Core',
            'GPU Core',
        ),
        ('load', 'temperature', 'load', 'temperature'),
    ) """
    self.sensor_index = [[_[0]] for _ in self.observe_types]
    for hardware in range(0, len(self.computer.Hardware)):
      for sensor in range(0, len(self.computer.Hardware[hardware].Sensors)):
        match_identifier = [
            index for index, (title, _name, _id) in enumerate(self.observe_types)
            if _name in str(self.computer.Hardware[hardware].Sensors[sensor].Name)
            and _id in str(self.computer.Hardware[hardware].Sensors[sensor].Identifier)
        ]
        print(self.computer.Hardware[hardware].Sensors[sensor].Name,
              self.computer.Hardware[hardware].Sensors[sensor].Identifier,
              self.computer.Hardware[hardware].Sensors[sensor].Value)
        if len(match_identifier) > 0:
          self.sensor_index[match_identifier[0]].extend([hardware, sensor])

  def getData(self):
    #更新硬件信息
    for h in set([_[1] for _ in self.sensor_index]):
      self.computer.Hardware[h].Update()
    data = []
    for title, hardware, sensor in self.sensor_index:
      data.append(str(int(self.computer.Hardware[hardware].Sensors[sensor].Value)) + " ")
      # print(title, str(self.computer.Hardware[hardware].Sensors[sensor].Value))
    return ''.join(data)

def wifi_main():
  ob = Observer()
  addr = '192.168.43.206'
  port = 34567
  soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  try:
    print('尝试连接 ', f'{addr}:{port}', end='\r')
    soc.connect((addr, port))
    print('连接成功')
    while True:
      soc.send((ob.getData() + "\0").encode('utf-8'))
      time.sleep(1)
  except ConnectionError as e:
    print(e.strerror)
    print('连接关闭')


# def serial_main

if __name__ == '__main__':
  wifi_main()
