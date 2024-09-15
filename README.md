# Create AItuber
このプロジェクトではOpenAI APIを利用して、オリジナルのAItuberを作成します。

## はじめに
このプロジェクト上のコードは[*阿部 由延(@sald_ra)氏*](https://x.com/sald_ra)の著書[『
AITuberを作ってみたら生成AIプログラミングがよくわかった件』](https://bookplus.nikkei.com/atcl/catalog/23/10/31/01079/)から
[github](https://github.com/sr2mg/aituber_python_programing_example)にて公開されているコードを参考に作成したものです。
書籍との主な相違点は下記2点となります。
* Python3.11.5 ⇒ Python3.12.4
* openai0.28.1 ⇒ openai1.43.0

## 環境

言語：Python3.12.4
その他:VOICEVOX/OBS Studio/VB-CABLE

## インストール

Python環境を未構築の方は[こちら](https://www.python.jp/install/windows/install.html)を参考に`Python3.12.4`をインストールください。
*※当プロジェクトはWindows環境の*Python3.12.4*でのみ動作を確認済。*


下記で動作に必要なライブラリを一括でインストール可能です。
```bash
# 未インストールであればsetuptoolsをインストール
pip install setuptools
```

```bash
# setup.pyがあるディレクトリで以下を実施
pip install .
```
*※上記でインストールされるライブラリはrequirements.txtを参照してください。*
## 使い方
1. `.env`ファイルに必要な情報を入力する。
2. `make_sound_device_list.py`を実行し、`sound_device.txt`を作成する。
※事前に[VB-AUDIO](https://vb-audio.com/Cable/)にてVB-CABLEのインストールをしておく。
3. 必要があれば`example_system.py`, `play_sound.py`, `test_voicevox.py`にて`output_device_name`に`sound_device.txt`から任意のデバイスを指定する。
4. `run_system.py`を起動する。

## 機能
* OpenAI APIを利用した生成AIとの会話
* YoutubeLiveで送信されたコメントの取得
* OBS Studioに接続し、プログラムからテキストを変更
* VOICEVOXに接続しサンプリングレートの取得および取得した音声データの再生
* PC上に接続されている音声デバイスの取得

## FAQ
#### .envに入力する情報がわからない
OpenAIのAPIキーについては[倉田 美咲](https://github.com/kurata04)氏の[こちらの記事](https://qiita.com/kurata04/items/a10bdc44cc0d1e62dad3)を参照ください。
OBSに関する情報は[YGPuzzleGTANT](https://x.com/roiyaruRIZ)氏の[こちらの記事](https://note.com/213414)を参照ください。
`VIDEO_ID`についてはYoutubeLiveの配信URLにおける"watch?v="の後の文字列が該当します。*(例、https://www.youtube.com/watch?v=hoge のhoge部分)*

#### test_voicevoxで入力した音声が再生されない
VOICEVOXは起動していますか？
インストールがまだならまずは[こちら](https://voicevox.hiroshiba.jp/)からVOICEVOXをインストールし、*VOICEVOXを起動した状態で*実行してみてください。
それでも再生されない場合はPlaySoundの引数に適切なデバイス名を指定できていない可能性があるので再度確認してください。

#### connect_obsを実行してもテキストに変化がない
`connect_obs.py`実行時にはOBS Studioを起動しておいてください。
また、画面上に「test」というテキストソースを配置する必要があります。
公開しているコードは直接実行すると「test」というテキストソースのテキストが「This is a test.」に変わるというプログラムのためです。

#### connect_openaiで出力結果が返ってこない
APIキーは正しく`.env`に記載されていますか？
もし誤ったAPIキーを入力してしまっている場合はAPIキーの再発行が必要です。
また、Open APIのUsageからCredit Grantsに空きがあることを確認してください。空きがない場合はクレジットの追加が必要です。

#### run_systemがうまく動作しない

`VIDEO_ID`は`.env`に正しく記載されていますか？
もしも自身でライブ配信を行いその動作の確認が取れない場合は、現行のYoutubeLiveから活発にコメントが行われている配信の`VIDEO＿ID`を入れてみてテストしてみてください。

##### その他
上記でも解決できない、または上記にはない問題が発生した際にはお手数ですが[*Issues*](https://github.com/t4ned4/create-aituber/issues)を残していただくか、taneda.bp@gmail.comまでご連絡ください。

## 製作者
名前: t4ned4
GitHub: @t4ned4
X: @tane_programing

*このREADMEは2024年9月12日時点での内容です。*
