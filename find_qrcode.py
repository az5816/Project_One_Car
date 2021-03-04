
import image
import sensor
import time
from fpioa_manager import fm
from machine import UART,Timer

fm.register(33,fm.fpioa.UART1_TX,force = True)
fm.register(35,fm.fpioa.UART1_RX,force = True)

uart = UART(UART.UART1,115200,8,None,1,timeout = 1000,read_buf_len = 4096)

# clock = time.clock()

sensor.reset()                                         #初始化摄像头模块
sensor.set_pixformat(sensor.RGB565)    #设置彩色模式
sensor.set_framesize(sensor.QVGA)        #设置帧大小(320x240)
# 人眼模式
sensor.set_vflip(1)                          # 垂直方向翻转
sensor.set_hmirror(1)                     # 水平方向翻转

sensor.skip_frames(30)                  # 跳过30帧

def scan_qrcode():
    """二维码扫描函数"""
    img = sensor.snapshot()
    res  = img.find_qrcodes()
    if len(res)>0:
        print(res[0].payload())
        # uart.write('i am fine !')
        uart.write('Task:'+res[0].payload())
        # uart.write(res[0].payload())

while True:
    scan_qrcode()

'''
while (True):
    img = sensor.snapshot()            # 拍照
    res = img.find_qrcodes()           # 创建对象,res为列表
    # print(len(res))                       # 确定res列表长度

    if len(res) > 0:
        # img.draw_string(2,2, res[0].payload(), color=(255,0,0), scale=4)
        # 写字 draw_string(x,y, text,color=(r,g,b),scale）
        # (_字符坐标,_字符内容,_字符颜色,_字符大小)
        # print()
        print(res[0].payload())
        # 打印二维码读取信息
        # 串口发送至lcd/数码管显示
'''
'''
import image,sensor,time

from fpioa_manager import fm
from machine import UART

#引脚映射
fm.register(33,fm.fpioa.UART1_TX,force=True)
fm.register(35,fm.fpioa.UART1_RX,force=True)

clock = time.clock()

#指定的参数新建一个 UART 对象
#格式参考：uart = machine.UART(uart,baudrate,bits,parity,stop,timeout, read_buf_len)

uart = UART(UART.UART1, 115200, 8, None, 1, timeout=1000, read_buf_len=4096)

sensor.reset()                         #初始化摄像头模块
sensor.set_pixformat(sensor.RGB565)    #设置彩色模式
sensor.set_framesize(sensor.QVGA)      #设置帧大小(320x240)
sensor.set_vflip(1)                        #垂直方向翻转   （二维码读取时该语句需添加）
sensor.set_hmirror(1)                   # 水平方向翻转
sensor.skip_frames(10)                 #跳过10帧

while True:
    clock.tick()
    img = sensor.snapshot()             #开始拍照
    task = img.find_qrcodes()           #寻找二维码
    fps =clock.fps()
    if len(task) > 0:
        uart.write('Task:'+task[0].payload())  #K210串口发送数据
        print(task[0].payload())                      #K210_IDE打印，用于调试和验证发送数据的正确性
'''
