# zeroyuka

Docomoの雑談対話APIとの会話をVOICEROIDに喋らせるためのプログラム

# 詳細

Docomoの雑談対話APIとVOICEROIDを喋らせる。

これを実行するにはモジュールモードで動き、マイク入力が可能なJuliusサーバーが必要。

マイク入力されJuliusの機能でXMLとなった通信内容をソケット経由(ポート番号10500)で取得し、
その内容をdocomoの会話APIに送信すると同時にVOICEROIDへ喋らせる。

その後、docomoの会話APIから返ってきた会話をVOICEROIDへ喋らせる。

喋らせる為に設定ファイル内に民安★Talkをダウンロードし、実行している。

現在Windows上で動作するCUI版のみ作成。

VOICEROIDに関わらない部分に関してはLinuxでも動作可能。ただしその場合当然音声は出力されない。


# 実行に必要なもの

このプログラムを実行させるには、音声入力及び音声認識を行いその結果を送信する装置と、このプログラムが動作しているPCの2台の装置が必要である。
ただし、この2台の装置で用いる環境を両方備えた装置がある場合には、1台でもよい。(両方備えた装置の動作は現在Ubuntu18.04上でのみ確認。)

## このプログラムを動作させるPC

* インターネット環境(Docomoの自然対話APIでのみ使用。)
* 起動状態のVOICEROID(Linux上でテストする場合には不要。)
* Python3の実行環境。現在3.7.1で動作確認している。パスを通す必要がある。使用しているモジュールについてはrequirements.txtを参照。
* Docomoの自然対話API(https://dev.smt.docomo.ne.jp/?p=docs.api.page&api_name=natural_dialogue&p_name=api_reference#tag01)の「雑談対話」が使用可能なAPIキー
* 音声入力及び認識結果を送信する装置へ10500ポートでTCP/IP通信が可能な通信回線

## 音声入力及び認識結果を送信する装置

* モジュールモードで起動してあり、入力機器をマイクとしたJulius。バージョンは4.4.2.1以降であることが必須。
* 接続されたマイク
* このプログラムを動作させるPCと10500ポートでTCP/IP通信が可能な通信回線

# 実行手順

0. 実行に必要なものを用意する。
1. このプロジェクトをcloneする。
2. docomochat/apikey.pyを作成し、以下のようにAPIKEYという名前の文字列型変数としてDocomoの自然対話APIのAPIキーを宣言する。サンプルソースは以下の通り。(このAPIキーは架空のものです。)
```
APIKEY = '1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef123456'
```
3. test.batを実行する。(Linux上でテストする場合にはtest.sh)

# LISCECE

MIT(https://github.com/Hayakuchi0/zeroyuka/blob/master/LICENSE)

# Author

Hayakuchi0
