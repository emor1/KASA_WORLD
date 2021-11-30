import cv2
import RPi.GPIO as GPIO
import Adafruit_PCA9685
import serial
import math
import schedule
import get_json as get_json


# set up freq
set_freq = 50
ang = 90
t = 0
# Set up OpenCV
faceCascade = cv2.CascadeClassifier('cascad/frontal_face.xml')

# read cascade
cap = cv2.VideoCapture(0)
cap.set(3, 320)
cap.set(4, 240)

ser = serial.Serial('/dev/ttyUSB0', 115200)

weather = "hare"
# weather = "ame"
# weather = "taihu"


def convert_deg(deg, freq):
    step = 4096
    deg = deg - 90
    max_pulse = 2.4
    min_pulse = 0.5

    center_pulse = (max_pulse - min_pulse) / 2 + min_pulse

    one_pulse = round((max_pulse - min_pulse) / 180, 2)

    deg_pulse = center_pulse + deg * one_pulse
    deg_num = int(deg_pulse / (1.0 / freq * 1000 / step))
    return deg_num


def happyMode(t_1):
    frqHappy = 0.5
    A = 30
    y = math.sin(2 * frqHappy * t_1 * math.pi) * A
    return y


def ScareMode(t_1):
    frqSad = 4
    A = 2
    y = math.sin(2 * frqSad * t_1 * math.pi) * A
    return y


def SadMode(t_1):
    f = 0.03
    A = 50
    y = math.sin(2 * f * t_1 * math.pi) * A
    return y


def update_wether_info():
    get_json.get_weather_data()
    print("Get JSON")
    global weather
    weather = get_json.update_weather()
    print("Update")
    print("Mode: %s" % weather)


if __name__ == "__main__":
    schedule.every(10).seconds.do(update_wether_info)
    pwm = Adafruit_PCA9685.PCA9685()
    pwm.set_pwm_freq(set_freq)
    # state = Fals
    state = True

    try:
        while True:
            schedule.run_pending()
            # Serial Communication for detecting umbrella
            data = ser.readline()
            data_clean = data.strip().decode('utf-8')
            ret, frame = cap.read()
            if data_clean == "16":
                print(data_clean)
                state = True
            elif data_clean == "IRtrue":
                state = True
            else:
                state = False

            if state:
                ret, frame = cap.read()
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                faces = faceCascade.detectMultiScale(
                    gray, scaleFactor=1.2, minNeighbors=5, minSize=(20, 20))

                for(x, y, w, h) in faces:
                    cv2.rectangle(frame, (x, y), (x + w, y + h),
                                  (255, 0, 0), 2)
                    roi_gray = gray[y:y + h, x:x + w]
                    roi_color = frame[y:y + h, x:x + w]
                    x_Pos = x + w / 2
                    ang1 = 180 * x_Pos / 360
                    ang = int(ang1)
                    if weather == "ame":
                        ang += happyMode(t)
                    elif weather == "hare":
                        ang += SadMode(t)
                    elif weather == "taihu":
                        ang += ScareMode(t)
            else:
                ang = 90
            cv2.imshow('video', frame)
            k = cv2.waitKey(30) & 0xff
            if k == 27:
                break
            pwm.set_pwm(0, 0, convert_deg(ang, set_freq))
            t += 0.1
    except KeyboardInterrupt:
        GPIO.cleanup()
        print("CleanUp")
        pwm.set_pwm(0, 0, 0)
        ser.close()
        pass

    pwm.set_pwm(0, 0, 0)
    GPIO.cleanup()
    print("CleanUp")
    cap.release()
    cv2.destroyAllWindows()
    ser.close()
