FROM python:3.9

WORKDIR /user/src/app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --system --deploy

COPY . .

CMD python bot.py