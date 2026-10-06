import RPi.GPIO as GPIO
import time

# 實體腳位 ？？ (BCM GPIO??)，請依你的接線調整
PIN_LED = 13
PIN_BUZZER = 11
freq = 523      # 頻率 (523Hz，大約是 C5)

# init GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_LED, GPIO.OUT)
GPIO.setup(PIN_BUZZER, GPIO.OUT)

# 建立 PWM 物件，設定頻率 freq
voice = GPIO.PWM(PIN_BUZZER, freq)

def long_sign():
    voice.start(50)   # duty 50%，發聲
    GPIO.output(PIN_LED, GPIO.HIGH)
    time.sleep(1)
    voice.stop()      # 停止發聲
    GPIO.output(PIN_LED, GPIO.LOW)
    time.sleep(0.5)

def short_sign():
    voice.start(50)   # duty 50%，發聲
    GPIO.output(PIN_LED, GPIO.HIGH)
    time.sleep(0.5)
    voice.stop()      # 停止發聲
    GPIO.output(PIN_LED, GPIO.LOW)
    time.sleep(0.5)

try:
    while True:
        for _ in range(3): short_sign()
        for _ in range(3): long_sign()
        for _ in range(3): short_sign()
        time.sleep(1)

except KeyboardInterrupt:
    pass
finally:
    voice.stop()
    GPIO.cleanup()



