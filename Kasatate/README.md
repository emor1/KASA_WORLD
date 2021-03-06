# 傘立て

## 概要
天気に応じて傘の動きが変わる傘立てのソースコード。動きの例としては、雨の日であれば傘が喜び、晴れの日や曇りの日であれば退屈そうなゆっくりな動きとなり、風が強い日であれば怯える。使用している天気APIは気象庁のものであり、6時間置きにJSONファイルを取得する。

## 動画
クリックすると動画のリンクに飛びます

顔をトラッキングする傘  
<!-- [![](https://img.youtube.com/vi/lEQB60Cla1I/0.jpg)](https://www.youtube.com/watch?v=lEQB60Cla1I) -->


喜ぶ傘  
[![](https://img.youtube.com/vi/JFexx1po1zk/0.jpg)](https://www.youtube.com/watch?v=JFexx1po1zk)


退屈そうな傘  
[![](https://img.youtube.com/vi/GdHj_rmhKHA/0.jpg)](https://www.youtube.com/watch?v=GdHj_rmhKHA)

怯える傘  
[![](https://img.youtube.com/vi/aG2PZIulmO8/0.jpg)](https://www.youtube.com/watch?v=aG2PZIulmO8)

## ソースコード
[傘の検知無し (傘立て単体)](kasatate_1.py)  
[傘の検知有り (傘立てと傘の組み合わせ)](kasatate_2.py)  
## 使用する部品
* Raspberry Pi4
* Webカメラ
* PCA9685
* サーボモータ (DSSERVO DS3218MG防水20KG高速メタルギア )

傘と傘立てとの組み合わせをやるならば追加で以下も必要なる
* M5Stack(もしくはArduino)
* 赤外線受信モジュール
* 磁気センサ

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

<!-- ## ディレクトリExpsについて
[Exps](Exps/)にはそれぞれのコードを単体で検証するために試験的に書いたコードがまとまっている -->