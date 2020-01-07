
1. Install requirements
```bash
pipenv install
```
2. Create a MySQL database
```sql
CREATE DATABASE chat CHARACTER SET utf8;
```
3. Init database
```bash
./manage.py migrate
```

4. Create admin user
```bash
./manage.py createsuperuser
```

5. Run development server
```bash
./manage.py runserver
```

Note :
Message prefetch config (load last n messages):
```python
MESSAGES_TO_LOAD = 15
```
