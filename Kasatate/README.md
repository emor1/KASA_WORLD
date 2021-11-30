# 傘立て

## 概要
天気に応じて傘の動きが変わる傘立てのソースコード。動きの例としては、雨の日であれば傘が喜び、晴れの日や曇りの日であれば退屈そうなゆっくりな動きとなり、風が強い日であれば怯える。使用している天気APIは気象庁のものであり、6時間置きにJSONファイルを取得する。

## 使用する部品
* Raspberry Pi4
* Webカメラ
<!-- * M5Stack(もしくはArduino) -->
<!-- * 赤外線受信モジュール -->
<!-- * 磁気センサ -->
* PCA9685
* サーボモータ (DSSERVO DS3218MG防水20KG高速メタルギア )


## 必要なPythonのライブラリ類
* OpenCV
* RPi.GPIO
* pyserial
* schedule

Adafruitのライブラリはこのファイルと同じディレクトリで以下の操作を行うことで使えるようになる ([参考](https://nyabot.hatenablog.com/entry/2019/04/24/223040))
```

$ git clone https://github.com/adafruit/Adafruit_Python_PCA9685.git
$ git clone https://github.com/adafruit/Adafruit_Python_GPIO.git
$ git clone https://github.com/adafruit/Adafruit_Python_PureIO.git

$ cd Adafruit_Python_PCA9685
$ sudo python setup.py install
$ sudo python3 setup.py install

$ cd ../Adafruit_Python_GPIO
$ sudo python setup.py install
$ sudo python3 setup.py install

$ cd ../Adafruit_Python_PureIO
$ sudo python setup.py install
$ sudo python3 setup.py install
```