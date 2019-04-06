# source: https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
# Dockerfile - this is a comment. Delete me if you want.
FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]
