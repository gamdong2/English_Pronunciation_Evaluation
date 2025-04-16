# 초등 영어 발음 채점 서비스
<p align="center">
  <img src="https://github.com/user-attachments/assets/0e65d798-b81d-4719-9fc2-61fecf3ae362" width="80%" alt="epa"/>
</p>

## Skills
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/AWS_EC2-FF9900?style=for-the-badge&logo=amazon-aws&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/AWS_Lambda-F90?style=for-the-badge&logo=aws-lambda&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/AWS_Step_Functions-FF4F00?style=for-the-badge&logo=amazonaws&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Google_STT-4285F4?style=for-the-badge&logo=google&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Tortoise_TTS-7F52FF?style=for-the-badge&logo=python&logoColor=white"/>&nbsp;

## 프로젝트 상세
- **진행 기간** : 2024년 11월 4일 ~ 2024년 11월 28일 (총 25일)
- **프로젝트 유형** : 팀 프로젝트 (총 3명)

## 프로젝트 목표
- 초등학생 대상의 영어 발음 학습 웹 애플리케이션 개발
- 사용자 음성을 표준 발음과 비교하여 오인식 단어 수 기반 피드백 제공
- 실시간 채점과 맞춤 콘텐츠 제공으로 자기주도 학습 유도

## 나의 역할 [팀장]
### 프로젝트 기획 및 일정 조율
- 기능 설계, 학습 흐름 구상, 팀원 업무 분배 및 일정 관리
### AWS 인프라 및 DB 구성·운영
- EC2 환경 구축, S3/Lambda 연동 자동화
- Docker 기반 PostgreSQL 컨테이너 구축 및 데이터 마이그레이션
- AWS Step Functions 를 통해 채점 로직 병렬화
### Django 백엔드 및 API 개발
- REST API로 사용자 음성 업로드/결과 조회 기능 구현
- DB와의 연동을 통해 채점 결과 자동 저장

## 사용한 데이터 셋
- 학습용 아동 영어 음성 데이터 (AI Hub)
- Tortoise TTS를 사용하여 생성한 표준 영어 음성 데이터

## 문제 해결 사례
### 세분화된 채점 기준의 사용자 부담   
- ‘오인식 단어 수’ 한 가지로 단순화하여 사용자 몰입도와 지속성 확보
### 오픈소스 STT 성능 한계  
- Google Cloud STT로 변경하여 아동 음성 인식률 향상 및 정확한 채점 로직 확보
- Enhanced 모델 대비 약 1.5배 저렴한 Default 모델 채택(평균 3.90원 / 1회 채점)

## 프로젝트 결과
### 구현 기능
- Google STT API 기반 오인식 단어 채점 기능 구현
- 파닉스, 동화, 회화 콘텐츠 선택 및 학습 레벨 설정 기능
- 사용자별 발음 이력 관리, 실시간 채점 결과 및 응원 메시지 제공
- Django REST API로 S3 업로드 · DB 저장 · 조회 기능 통합 
  
