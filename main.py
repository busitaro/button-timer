from os import path
from time import sleep
from threading import Thread
import subprocess

import PySimpleGUI as sg

from control import push_btn
from config import Config


class Execution():
    def __init__(self):
        self.loop = False
        self.interval = 0

    def exec(self):
        while self.loop:
            push_btn(self.interval)
            sleep(5)

    def start(self):
        self.thread = Thread(target=self.exec)
        self.thread.start()

execution = Execution()


def start_event(interval):
    execution.interval = interval
    execution.loop = True
    print('開始')
    execution.start()


def end_event():
    execution.loop = False
    print('終了')


def launch_browser():
    def launch():
        # ブラウザのデータアウトプットパスを作成
        config = Config()
        data_output_path = path.abspath(config.data_output_path)

        # ブラウザのパス
        brower_path = config.browser_path

        # ブラウザの起動
        subprocess.run([brower_path, '-remote-debugging-port=9222', '--user-data-dir={}'.format(data_output_path)])
    # 別スレッドとしてブラウザ起動
    thread = Thread(target=launch)
    thread.start()


def show_gui():
    sg.theme('DarkAmber') 
    label_launch = "ブラウザ起動"
    label_start = 'スタート'
    label_stop = 'ストップ'
    label_interval = '待機時間 (分)'
    is_start = False

    # ウィンドウに配置するコンポーネント
    layout = [
            [sg.Text(label_interval , size=(25, 1)), sg.InputText('', size=(5, 1), key='interval')],
            [sg.Button(label_launch, key='launch_btn')],
            [sg.Button(label_start, key='s_btn')],
            [sg.Output(size=(80,20))]
    ]

    # ウィンドウの生成
    window = sg.Window('WEBクリックツール', layout)

    # イベントループ
    while True:
        try:
            event, values = window.read()
            if event == sg.WIN_CLOSED:
                # ウィンドウの×ボタン
                print('closed')
                break
            elif event == 'launch_btn':
                launch_browser()
            elif event == 's_btn':
                if not is_start:
                    # スタート
                    # intervalのvalidation
                    interval = values['interval']
                    if not interval.isdigit():
                        print('{}には数値を入力してください。'.format(label_interval))
                    else:
                        window['s_btn'].update(label_stop)
                        is_start = not is_start
                        start_event(int(interval))
                else:
                    # ストップ
                    window['s_btn'].update(label_start)
                    is_start = not is_start
                    end_event()
        except Exception as ex:
            print('エラー発生')
            print('----------------------------')
            print(ex)
            print(ex.args)
            print('----------------------------')

    window.close()


def main():
    show_gui()


if __name__ == '__main__':
    main()
