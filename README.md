# CCU_Class_Robot
## Using host
1. Install python package
```
pip install -r requirements.txt
```
2. Install pytesseract and pytesseract-eng language pack on your computer
3. Copy a copy of env_example.py to env.py
```
cp env_example.py env.py
```
4. Enter your account password and the course you want to choose in env.py
5. Run the bot
```python
python main.py
```
## Using docker-compose
1. Copy a copy of env_example.py to env.py
```
cp env_example.py env.py
```
2. Enter your account password and the course you want to choose in env.py
3. Build docker image
```
docker-compose build --no-cache
```
4. Run the bot
```
docker-compose up
```
