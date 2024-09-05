FROM python:3.9
WORKDIR /git/flaskfrm
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD ["python", "frm.py"]