import RPi.GPIO as GPIO import time
import tm1637


tm = tm1637.TM1637(clk=23, dio=24) GPIO.setmode(GPIO.BCM) GPIO.setwarnings(False)
 
RED_LED_1 = 2
YELLOW_LED_1 = 3
GREEN_LED_1 = 21
RED_LED_2 = 22
YELLOW_LED_2 = 17
GREEN_LED_2 = 27
RED_LED_3 = 14
YELLOW_LED_3 = 15
GREEN_LED_3 = 18
RED_LED_4 = 13
YELLOW_LED_4 =19
GREEN_LED_4 = 26
GPIO.setup([RED_LED_1, YELLOW_LED_1, GREEN_LED_1, RED_LED_2, YELLOW_LED_2, GREEN_LED_2, RED_LED_3, YELLOW_LED_3, GREEN_LED_3, RED_LED_4, YELLOW_LED_4, GREEN_LED_4], GPIO.OUT)
def light(pin=1,val=1): if pin==1:
GPIO.output(RED_LED_1, GPIO.LOW) GPIO.output(YELLOW_LED_1, GPIO.LOW) GPIO.output(GREEN_LED_1, GPIO.LOW)
if val==1: GPIO.output(RED_LED_1, GPIO.HIGH)
elif val==2:
GPIO.output(YELLOW_LED_1, GPIO.HIGH)
else:
GPIO.output(GREEN_LED_1, GPIO.HIGH)
elif pin==2:
GPIO.output(RED_LED_2, GPIO.LOW) GPIO.output(YELLOW_LED_2, GPIO.LOW) GPIO.output(GREEN_LED_2, GPIO.LOW)
if val==1:
 
GPIO.output(RED_LED_2, GPIO.HIGH)
elif val==2:
GPIO.output(YELLOW_LED_2, GPIO.HIGH)
else:
GPIO.output(GREEN_LED_2, GPIO.HIGH)
elif pin==3:
GPIO.output(RED_LED_3, GPIO.LOW) GPIO.output(YELLOW_LED_3, GPIO.LOW) GPIO.output(GREEN_LED_3, GPIO.LOW)
if val==1: GPIO.output(RED_LED_3, GPIO.HIGH)
elif val==2:
GPIO.output(YELLOW_LED_3, GPIO.HIGH)
else:
GPIO.output(GREEN_LED_3, GPIO.HIGH)
else:
GPIO.output(RED_LED_4, GPIO.LOW) GPIO.output(YELLOW_LED_4, GPIO.LOW) GPIO.output(GREEN_LED_4, GPIO.LOW)
if val==1: GPIO.output(RED_LED_4, GPIO.HIGH)
elif val==2:
GPIO.output(YELLOW_LED_4, GPIO.HIGH)
else:
GPIO.output(GREEN_LED_4, GPIO.HIGH)
def counter(count): tm.show("0000")
while count>=0: tm.show(str(count))
count-=1; time.sleep(1)
def traffic_lights(i,t):
 
count1=t-2; while True: if(i==0):
light(1,3) light(2,1) light(3,1) light(4,1)
counter(count1) light(1,3)
light(2,2) light(3,1) light(4,1) counter(2)
if i==1: light(1,1) light(2,3) light(3,1) light(4,1)
counter(count1) light(1,1)
light(2,3) light(3,2) light(4,1) counter(2) light(1,1) light(2,3) light(3,2) light(4,1) counter(2)
if i==2: light(1,1) light(2,1)
 
light(3,3) light(4,1)
counter(count1) light(1,1)
light(2,1) light(3,3) light(4,2) counter(2)
if i==3: light(1,1) light(2,1) light(3,1) light(4,3)
counter(count1) light(1,2)
light(2,1) light(3,1) light(4,3) counter(2)
