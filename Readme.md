# ATS Resume Expert

## Prerequisites -
1. You need gemini api key. You can obtain that here - https://aistudio.google.com/app/apikey
2. Python installed

## How to run locally
1. Clone repo using `git clone`
2. Latest poppler for windows downloaded which is required for pdf to image library used. You can obtain latest release here - https://github.com/oschwartz10612/poppler-windows/releases. Make sure to extract zipped files and put **poppler\library\bin** folder path in your %PATH% environment variable
3. `pip install -r requirements.txt`
4. Add your gemini api key to .env file.
5. `streamlit run app.py` ==> This will open application on port 8501 and will be shown
