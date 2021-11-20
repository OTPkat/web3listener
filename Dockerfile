FROM python:3.9

# Define container working directory
WORKDIR listener

# Copy source code and requirements file

COPY requirements.txt /listener/requirements.txt
COPY web3_listener /listener/web3_listener
COPY main.py /listener/main.py
# Install dependencies
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Keep container running
CMD ["python3", "main.py"]
