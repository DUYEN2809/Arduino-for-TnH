# Arduino-for-TnH
# Hướng dẫn cài đặt và sử dụng Arduino-for-TnH

## Cài đặt

### Cách 1: Cài đặt tự động

1. **Cài đặt tự động:**
Đối với windows:
   - Chạy file `setup_run.bat`: `./setup_run.bat`
   - Lệnh này sẽ tự động cài đặt các thư viện cần thiết và chạy ứng dụng.

### Cách 2: Cài đặt thủ công

1. **Clone Repository:**
   ```bash
   git clone https://github.com/yourusername/your-repo.git
   cd your-repo
   ```
2. **Cài đặt các thư viện:**
    + Cách 1: Sử dụng môi trường ảo
	```
	python -m venv venv
	source venv/bin/activate    # For Linux/Mac
	.\venv\Scripts\activate    # For Windows
	```
	+ Cách 2: Cài đặt các thư viện
	```
	pip install -r requirements.txt
	```
3. **Sử dụng**
	***Chạy ứng dụng:***
	+ Sử dụng câu lệnh sau để khởi chạy ứng dụng:
	```
	python -m streamlit run homepage.py
	```
	Truy cập trình duyệt web và điều hướng đến http://localhost:8501 để xem ứng dụng.


