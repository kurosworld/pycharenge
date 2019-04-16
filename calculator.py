from tkinter import *
from tkinter import ttk

LAYOUT = [
    ['7', '8', '9', '/'],
    ['4', '5', '6', '*'],
    ['1', '2', '3', '-'],
    ['0', 'C', '=', '+'],
]

# 記号をまとめた定数. if char in CALC_SYMBOLS:... のように使うために定義
CALC_SYMBOLS = ('+', '-', '*', '/', '**', '//')

class CalcApp(ttk.Frame):
    """電卓アプリ(予定)"""

    def __init__(self,master=None):
        super().__init__(master)
        self.exp_list = ['0']  # これを足した
        self.create_style()
        self.create_widgets()

    def create_widgets(self):
        """ウィジェットの作成."""
        # 計算結果の表示ラベル
        self.display_var = StringVar()
        self.display_var.set('0')  # 初期値を0にする

        dispay_label = ttk.Label(self, textvariable=self.display_var)
        dispay_label.grid(column=0, row=0, columnspan=4, sticky=(N, S, E, W))
        
        # レイアウトの作成
        for y, row in enumerate(LAYOUT, 1):
            for x, char in enumerate(row):
                button = ttk.Button(self, text=char)
                button.grid(column=x, row=y, sticky=(N, S, E, W))
                button.bind('<Button-1>', self.calc)
        self.grid(column=0, row=0, sticky=(N, S, E, W))

        # 横の引き伸ばし設定
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)
        self.columnconfigure(3, weight=1)

        # 縦の引き伸ばし設定。0番目の結果表示欄だけ、元の大きさのまま
        self.rowconfigure(0, weight=0)
        self.rowconfigure(1, weight=1)
        self.rowconfigure(2, weight=1)
        self.rowconfigure(3, weight=1)
        self.rowconfigure(4, weight=1)

        # ウィンドウ自体の引き伸ばし設定
        self.master.columnconfigure(0, weight=1)
        self.master.rowconfigure(0, weight=1)

    def calc(self,event):
        # 押されたボタンのテキストを取得
        char = event.widget['text']

        # 最後に押したボタンの内容
        last = self.exp_list[-1]

        if char == '=':
            if last in CALC_SYMBOLS:  # ここ
                self.exp_list.pop()
            exp = eval(''.join(self.exp_list))
            self.exp_list = [str(exp)]
        elif char == 'C':
            self.exp_list = ['0']
        elif char in CALC_SYMBOLS:
            if last == char == '/':
                self.exp_list[-1] += '/'
            elif last == char == '*':
                self.exp_list[-1] += '*'
            elif last in CALC_SYMBOLS:
                self.exp_list[-1] = char
            else:
                self.exp_list.append(char)
        else:
            if last == '0':
                self.exp_list[-1] = char
            elif last in CALC_SYMBOLS:
                self.exp_list.append(char)
            else:
                self.exp_list[-1] += char

        # リストに格納している式を文字列にし、画面に反映
        self.display_var.set(
            ' '.join(self.exp_list)
        )

    def create_style(self):
        """ボタン、ラベルのスタイルを変更."""
        style = ttk.Style()

        # ラベルのスタイルを上書き
        style.configure(
            'TLabel', font=('Helvetica', 20),
            background='black', foreground='white',
        )
        # ボタンのスタイルを上書き
        style.configure('TButton', font=('Helvetica', 20))


def main():
    root =  Tk()
    root.title('簡単電卓')
    CalcApp(root)
    root.mainloop()


if __name__ == '__main__':
    main()
