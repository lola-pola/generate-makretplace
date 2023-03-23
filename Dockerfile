FROM python:3.9


WORKDIR /app
COPY app .
COPY req req
RUN pip install -r req

CMD [ "streamlit", "run", "mainer.py" ] 