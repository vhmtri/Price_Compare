
# Price-Compare-Django
* Home page
![image](https://github.com/vhmtri/Project_PTUD/assets/125715460/6403daa2-67fc-4d36-a803-3487a718cd82)
# Hướng dẫn sử dụng
## Bước 1: Tạo môi trường ảo Python và Cài đặt thư viện 
trong `cmd` chạy các lệnh
```bash
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
```
## Bước 2. Để thiết lập kết nối tới database, bạn cần chỉnh sửa file `settings.py` trong project của mình. Ví dụ, nếu bạn sử dụng PostgreSQL, bạn có thể sử dụng các thông tin kết nối sau:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'products_db',
        'USER': 'project_ptud',
        'PASSWORD': '241', #cài pass
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```
Trong đó:

- `ENGINE`: Loại database backend sử dụng (trong trường hợp này là PostgreSQL).
- `NAME`: Tên của database.
- `USER`: Tên đăng nhập để truy cập database.
- `PASSWORD`: Mật khẩu để truy cập database.
- `HOST`: Địa chỉ của database server (trong trường hợp này là localhost).
- `PORT`: Cổng kết nối tới database (trong trường hợp này là 5432 cho PostgreSQL).

Bạn có thể sửa file **settings.py** trong project của mình để thêm các thông tin kết nối tới database của bạn. Lưu ý rằng, bạn cần phải cài đặt driver tương ứng cho database của mình (ví dụ: psycopg2 cho PostgreSQL) để Django có thể kết nối và thao tác với database.
## Bước 3: Cài đặt các package, thêm dữ liệu vào database và chạy server
`Ta vào thư mục ComparePrice:`
```bash
cd ComparePrice
```

```bash
python manage.py makemigrations
```
```bash
python manage.py migrate
```
```bash
python manage.py migrate
```

```bash
python manage.py createsuperuser
```

`Mọi người, hãy chạy lệnh này để điền vào cơ sở dữ liệu.`
```bash
python get_laptop_Xgear.py
```
## Bước 4: Chạy chương trình
`Sử dụng file` **run.bat**
```bash
run.bat
```
Sau khi chạy xong, bạn có thể truy cập trang web của mình trên trình duyệt với địa chỉ:
```bash
http://127.0.0.1:8000/
```
