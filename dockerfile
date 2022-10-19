FROM python:3
RUN git clone https://github.com/perezmatias/Numeros_romanos.git
WORKDIR /Numeros_romanos
RUN pip install -r requirements.txt
CMD ["python3", "-m", "unittest"]