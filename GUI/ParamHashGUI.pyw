import os
import shutil
import subprocess   
import pathlib
import PySimpleGUI as sg
import sys
from tkinter import messagebox

sg.theme('TanBlue')

layout = [
    [sg.Text('ファイルを選択してください')],
    [sg.Text('ファイル', size=(10, 1)), sg.Input(), sg.FileBrowse('ファイルを選択', key='file')],
    [sg.Button('スタート', key='start'), sg.Button('終了', key='exit')],
]

window = sg.Window('ParamHashGUI', layout)

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED or event == 'exit':
        break

    if event == 'start':
        messagebox.showinfo('確認', 'ホーム画面に戻ります')
        messagebox.showwarning('注意', '処理は続行されます。\n黒い画面が表示されるまでしばらくお待ちください。')
        window.close()     
        shutil.copy2(values['file'], "./source")
        shutil.copy2("2-1.sp2", "ParamHash.exe")
        shutil.copy2("2-2.sp2", "convert.exe")
        shutil.copy2("2-3.sp2", "param.csv")
        subprocess.run("ParamHash.exe")
        messagebox.showwarning('注意', 'ファイルを読みやすくします。\n再度黒い画面が表示されるのでしばらくお待ちください。')
        subprocess.run("ParamHash.exe")
        messagebox.showinfo('成功！', 'ファイルの処理が完了しました\nファイルは"複合化・暗号化済み"フォルダに保存されています。')
        shutil.rmtree('./source/')
        os.mkdir('./source')
        shutil.copytree('./build', './複合化・暗号化済み')
        shutil.rmtree('./build/')
        os.mkdir('./build')
        os.remove('ParamHash.exe')
        os.remove('param.csv')
        os.remove('convert.exe')
        os.remove('log.txt')
        
