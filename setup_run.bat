@echo off

rem Install required libraries using pip --user
pip install --user -r requirements.txt

rem Run homepage.py using streamlit
python -m streamlit run homepage.py
