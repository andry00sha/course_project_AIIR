
FROM python:3.9
COPY djangoProjects/requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt
COPY djangoProjects djangoProjects
ADD .env /env_file/.env
WORKDIR /djangoProjects
RUN python manage.py migrate
RUN python manage.py collectstatic
#Порты
#EXPOSE 8000