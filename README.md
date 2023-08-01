# Docker Tutorial for BOAZ Menmen Study
2023.08.01

## Contents
- BOAZ 엔지니어링 트랙 멘멘 스터디를 위해 준비한 도커 심화 세션 레포지토리입니다.
- 이론 설명과 Airflow 실습으로 이루어집니다.

## 실습 과정
- 현 레포지토리를 개발환경에 clone 해주세요.
```
 git clone https://github.com/HyeJung-Hwang/docker-tutorial.git
 ```
- clone된 docker-practice 폴더 안으로 들어가 주세요.
```
cd docker-practice
```
- Aiflow 실행에 필요한 환경변수를 셋팅해주세요.
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
- Airflow 실행에 필요한 기초 작업(유저셋팅)등에 해당하는 docker compose 서비스를 먼저 실행합니다.
```
docker compose up airflow-init
```
- 전체 docker compose를 실행해주세요.
```
docker compose up
```

