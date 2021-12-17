FROM python:3.9

# Define container working directory
WORKDIR listener

# Copy source code and requirements file

COPY requirements.txt /listener/requirements.txt
COPY web3_listener /listener/web3_listener
COPY main.py /listener/main.py

ENV SECRET_INFURA=projects/148433842428/secrets/infura-listener/versions/1
ENV SECRET_ETHERSCAN=projects/148433842428/secrets/etherscan-listener/versions/1

COPY gcp-creds.json /listener/gcp-creds.json
# Install dependencies
RUN pip3 install --upgrade pip
RUN pip install -r requirements.txt

# Keep container running
CMD ["python3", "main.py"]
