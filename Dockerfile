FROM python:latest
WORKDIR /app/cluetail
ENV PYTHONBUFFERED=0
RUN pip install gradio scikit-learn transformers
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
COPY . .
EXPOSE 8084
CMD ["python", "cluetailFullDemo.py"]
