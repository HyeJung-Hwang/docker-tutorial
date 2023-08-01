# Docker Tutorial for BOAZ Menmen Study
2023.08.01

## Contents
- BOAZ 엔지니어링 트랙 멘멘 스터디를 위해 준비한 도커 심화 세션 레포지토리입니다.
- [이론 설명](https://bead-group-eb2.notion.site/Docker-Tutorial-by-ME-92f4f7c6216f4d879f7c36ce51d83224?pvs=4)과 도커 컴포즈로 Airflow 를 사용하는 실습으로 이루어집니다.

## 실습 과정
- 개발환경에 도커와 도커 컴포즈를 설치해주세요.
- 현 레포지토리를 개발환경에 clone 해주세요.
```
 git clone https://github.com/HyeJung-Hwang/docker-tutorial.git
 ```
- clone된 docker-practice 폴더 안으로 들어가 주세요.
```
cd docker-practice
```
- Airflow 실행에 필요한 폴더를 만들어주세요.
```
mkdir -p ./logs ./plugins ./config
```
- Airflow 실행에 필요한 환경변수를 셋팅해주세요.
```
echo -e "AIRFLOW_UID=$(id -u)" > .env
```
- Airflow 실행에 필요한 초기화 작업(유저셋팅)등에 해당하는 docker compose 서비스를 먼저 실행합니다. 아래 이미지가 출력되면 초기화가 잘 된것입니다.
```
docker compose up airflow-init
```
<img width="382" alt="image" src="https://github.com/HyeJung-Hwang/docker-tutorial/assets/79091824/5f6b5bd9-317d-488b-837e-83d45bf3698f">

- 전체 docker compose를 실행해주세요.
```
docker compose up
```
- localhost:8080 에서 Airflow Webserver 실행을 확인해주세요.
<img width="1430" alt="image" src="https://github.com/HyeJung-Hwang/docker-tutorial/assets/79091824/a8b8b731-2aa2-4bef-91e8-f137ff4b31a9">

