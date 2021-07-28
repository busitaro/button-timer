# button-timer
Seleniumで一定時間ごとにボタンを押下するツール

## exeの出力方法
```
pyinstaller main.py --onefile --noconsole
 
出力される .specファイルの# -*- mode: python ; coding: utf-8 -*-の直後に↓を追加
import sys
sys.setrecursionlimit(5000)

pyinstaller main.spec --onefile
```
