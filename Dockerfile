# source: https://medium.com/@mtngt/docker-flask-a-simple-tutorial-bbcb2f4110b5
# Dockerfile - this is a comment. Delete me if you want.
FROM alpine:3.9
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 8000
CMD ["gunicorn", "-b", "0.0.0.0:8000", "app"]