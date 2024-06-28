FROM python:3.10
EXPOSE 5000
WORKDIR /app
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /app
ENV PYTHONPATH=/app
CMD ["/bin/bash", "docker-entrypoint.sh"]