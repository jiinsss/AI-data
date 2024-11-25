FROM python:3.12

# Poetry 설치
RUN pip install -U poetry

# 경로 정의
WORKDIR /insp

# 로컬에 있는 pyproject.toml, poetry.lock 파일을 컨테이너로 복사
COPY poetry.lock pyproject.toml /insp/

# Poetry를 이용하여 의존성 설치 
RUN poetry config virtualenvs.create false \
 && poetry install --no-root --no-interaction 

# 로컬에 있는 소스코드를 컨테이너로 복사
COPY . /insp

# Python 경로 설정
ENV PYTHONPATH=/usr/local/bin/python3.12

# Poetry 바이너리 권한 확인 및 설정
RUN chmod +x /usr/local/bin/poetry

# Poetry가 설치된 Python을 사용하도록 설정
RUN sed -i '1s|^.*$|#!/usr/local/bin/python3.12|' /usr/local/bin/poetry

# 권한과 바이너리 위치 확인
RUN ls -l /usr/local/bin/poetry


#크롬
RUN apt-get update
RUN wget -q https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
RUN apt-get install -y ./google-chrome-stable_current_amd64.deb
RUN rm ./google-chrome-stable_current_amd64.deb

#google-play-scraper
RUN pip install google-play-scraper

EXPOSE 8000
# Python 출력 버퍼링을 비활성화
ENV PYTHONUNBUFFERED=1

