# cubicpy

說明
---

俐方體11號的衍生字庫檔 for MicroPython

字庫來源：[ACh-K/Cubic-11: 免費開源的 11×11 中文點陣體](https://github.com/ACh-K/Cubic-11)

檔案說明
---

| 檔案 | 說明 |
|:---|:---|
| cubicpy.py | 中文字庫主檔 |
| cubicpy_fetch.py | Python 取字範例 |
| my_font.py | 取字後產生要上傳至 MCU 的小型字庫檔 |
| cubicpy_demo.py | MicroPython 調用及顯示範例
| my_util.py | 包含設定 SSD1306 的 function 自訂 module，需按不同顯示設備做修改
| OFL.txt | SIL OPEN FONT LICENSE file |

用法
---

1. 先以 Python 依 cubicpy_fetch.py 範例從字庫主檔中取字，產生包含自訂字詞資料的小型字庫檔。
1. 將小型字庫檔上傳至 MicroPython，再依 cubicpy_demo.py 範例調用並顯示。
1. 更多說明在 「[MicroPython feat. 俐方體11號 - HackMD](https://hackmd.io/@PaoyungChang/mpy_cubic11)」
