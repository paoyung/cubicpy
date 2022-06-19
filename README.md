# cubicpy

說明
---

俐方體11號的衍生字庫檔 for MicroPython

字庫來源：[ACh-K/Cubic-11: 免費開源的 11×11 中文點陣體](https://github.com/ACh-K/Cubic-11)

授權
---

- 本字庫檔衍生於 SIL Open Font License 1.1 [Cubic11/俐方體11號](https://github.com/ACh-K/Cubic-11) 所發布的開源字型。

- 本字庫檔亦基於 SIL Open Font License 1.1 授權條款公開發布。關於授權合約的詳細內容，請詳讀授權文件檔（OFL.txt）。

  - **cubicpy** 為本專案的保留名稱。
  - 任何人可以無償使用此字型，包含商用。無須告知原作者。
  - 您可自由傳送、分享此字型，或與其他軟體綑綁發行、銷售。捆包中必須同時包含授權文件檔（OFL.txt）。
  - 您可自由改造、衍生此字型並公開。修改後的字型必須同樣以 [SIL OFL](https://scripts.sil.org/OFL) 進行發布，勿使用字型的保留名稱。
  - 依照 [SIL OFL](https://scripts.sil.org/OFL) 規定，**禁止單獨出售字型檔**。

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

注意事項
---

- 空格也是文字，請記得加入字詞清單中。
- 符號有分全型半型，務必分清楚才不會產生錯誤。
