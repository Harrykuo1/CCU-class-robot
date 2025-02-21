# CCU_Class_Robot
## Using host
1. Install python package
```
pip install -r requirements.txt
```
2. Install pytesseract and pytesseract-eng language pack on your computer
3. Copy the ccu traindata into the tessdata of the entrance tesseract-ocr
4. Copy a copy of env_example.py to env.py
```
cp env_example.py env.py
```
4. Enter your account password and the course you want to choose in env.py(修改教學可參考後面"設置想搶的課程")
5. Run the bot
```python
python main.py
```
## Using docker-compose
1. Copy a copy of env_example.py to env.py
```
cp env_example.py env.py
```
2. Enter your account password and the course you want to choose in env.py(修改教學可參考後面"設置想搶的課程")
3. Run the bot
```
docker-compose up
```
## 設置想搶的課程

### 設置想搶的課

建議使用Firefox瀏覽器，只有看要搶哪些課時會用到

先至選課網站，觀看自己想選的課程並且選取
![image](https://github.com/as6325400/ccuRobClass/assets/105158172/c4707c35-8cfd-453f-91f1-57f82c6457ca)


點選 F12 打開開發者模式，並選取網路
![image](https://github.com/as6325400/ccuRobClass/assets/105158172/cf25d10c-3705-48cf-b05d-b590d303e209)


之後點擊主要畫面的 ```加選以上科目```按鈕

點擊右側有 ```post``` 字樣的那筆資料，若有多筆，通常會是最下面的，但建議盡快按，這樣只有一筆比較好判斷，並且在下方點選請求按鈕
![image](https://github.com/as6325400/ccuRobClass/assets/105158172/e74633ed-9691-4327-9569-2f444e54dfe7)


隨便點擊一欄，點選複製全部

```
{
	"session_id": "bHiKQGToM8M10IbBPD4SAIrLF0H3496iM964",
	"dept": "4154",
	"grade": "3",
	"cge_cate": "",
	"cge_subcate": "",
	"page": "1",
	"e": "0",
	"m": "0",
	"SelectTag": "1",
	"4152015_01": "2",
	"4153002_01": "2",
	"4153203_01": "2",
	"4153205_01": "2",
	"course": "4153206_01",
	"4153206_01": "2",
	"4153208_01": "2",
	"4153211_01": "2",
	"4153900_01": "2",
	"4153918_01": "2",
	"4153919_01": "2"
}
```

會複製出一個json格式的物件，最終，我們將這個物件貼進，```env.py``` 裡面的 

```python=
CLASS_LIST = [
    {
	"session_id": "bHiKQGToM8M10IbBPD4SAIrLF0H3496iM964",
	"dept": "4154",
	"grade": "3",
	"cge_cate": "",
	"cge_subcate": "",
	"page": "1",
	"e": "0",
	"m": "0",
	"SelectTag": "1",
	"4152015_01": "2",
	"4153002_01": "2",
	"4153203_01": "2",
	"4153205_01": "2",
	"course": "4153206_01",
	"4153206_01": "2",
	"4153208_01": "2",
	"4153211_01": "2",
	"4153900_01": "2",
	"4153918_01": "2",
	"4153919_01": "2"
    }
]
```

若有多個，用```，```隔開，大致上會長這樣

```python=
CLASS_LIST = [
    {
        # class1
    },
    {
        # class2
    }
]
```
建立完成 !
