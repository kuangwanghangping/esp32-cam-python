from machine import Pin
import time 
# 设置 D1 引脚为输出模式
#pin_d22 = Pin(0, Pin.IN,Pin.PULL_DOWN)
pin_button = Pin(5,Pin.IN,Pin.PULL_DOWN)#这样是默认是没有低电平
pin_led = Pin(0,Pin.OUT)#led两边一遍接着的是gnd一边接的是pin_0引脚
status = 0
while True :
    if pin_button.value() == 1: #如果通电
        time.sleep_ms(80)#延迟消抖一下
        if pin_button.value() == 1 and status == 0 :
            pin_led.value(not pin_led.value())
            status = 1
        elif pin_button.value() == 0 :
            status = 0
        
    

