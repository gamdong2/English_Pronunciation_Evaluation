# 초등 영어 발음 채점 서비스
<p align="center">
  <img src="https://github.com/user-attachments/assets/0e65d798-b81d-4719-9fc2-61fecf3ae362" width="80%" alt="epa"/>
</p>

## Skills
<img src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/PostgreSQL-336791?style=for-the-badge&logo=postgresql&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/librosa-0.10.0-brightgreen?style=for-the-badge&logo=python&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/Parselmouth-0.4.5-brightgreen?style=for-the-badge&logo=python&logoColor=white"/>&nbsp;
<img src="https://img.shields.io/badge/AWS_S3-569A31?style=for-the-badge&logo=amazons3&logoColor=white"/>&nbsp;

## 프로젝트 상세

- **진행 기간**: 2024년 11월 4일 ~ 2024년 11월 28일 (총 25일)
- **프로젝트 유형**: 팀 프로젝트 (총 3명)

## 프로젝트 목표
- 초등학생 대상의 영어 발음 학습 웹 애플리케이션 개발
- 사용자 음성을 표준 발음과 비교하여 오인식 단어 수 기반 피드백 제공
- 실시간 채점과 맞춤 콘텐츠 제공으로 자기주도 학습 유도

## 나의 역할 [팀장]
- 프로젝트 기획 및 일정 조율
  - 기능 설계, 학습 흐름 구상, 팀원 업무 분배 및 일정 관리
-  AWS 인프라 및 DB 구성·운영
  - EC2 환경 구축, S3/Lambda 연동 자동화
  - Docker 기반 PostgreSQL 컨테이너 구축 및 데이터 마이그레이션
  - AWS Step Functions 를 통해 채점 로직 병렬화
- Django 백엔드 및 API 개발
  - REST API로 사용자 음성 업로드/결과 조회 기능 구현
  - DB와의 연동을 통해 채점 결과 자동 저장

## 사용한 데이터 셋
- 학습용 아동 영어 음성 데이터 (AI Hub)
- Tortoise TTS를 사용하여 생성한 표준 영어 음성 데이터

## 프로젝트 결과
### 구현 기능
- Google STT API 기반 오인식 단어 채점 기능 구현
- 파닉스, 동화, 회화 콘텐츠 선택 및 학습 레벨 설정 기능
- 사용자별 발음 이력 관리, 실시간 채점 결과 및 응원 메시지 제공
- Django REST API로 S3 업로드 · DB 저장 · 조회 기능 통합

## 문제 해결 사례
### 구현 기능
- **실시간 발음 채점 및 피드백**: 사용자가 녹음한 음성을 기반으로 3초 이내에 채점 결과 제공
- **맞춤형 학습 콘텐츠 제공**: 파닉스, 회화, 소설 카테고리에서 학생 수준에 맞는 콘텐츠 선택 가능
- **Django REST Framework(DRF)와 S3 연동**: REST API를 통해 사용자 음성을 S3에 업로드하고, 저장된 데이터를 분석하여 채점 결과 제공

### 주요 성과
- 채점 정확성: 피치, 리듬, 발화 속도, 발음 정확성에서 평균 95% 이상의 유사도 확보
- 실시간 처리: 채점 결과 반환 시간을 3초 이내로 단축하여 사용자 경험 최적화

## 트러블 슈팅

- **문제**: S3 파일 접근 오류로 인해 사용자 음성 파일이 누락됨
  - **해결**: IAM 정책을 수정하여 Django 애플리케이션이 S3 버킷에 안전하게 접근할 수 있도록 설정
- **문제**: 음성 데이터 샘플링 속도 불일치로 인한 분석 오류 발생
  - **해결**: Librosa로 모든 음성을 16,000Hz로 리샘플링하여 데이터 일관성 확보

## 프로젝트를 통해 얻은 역량

- 클라우드 환경(AWS S3, EC2)에서 대규모 음성 데이터 처리 및 저장
- Docker를 활용해 PostgreSQL을 컨테이너화함으로써 데이터베이스 관리 및 협업 효율성 향상
- Librosa와 Parselmouth를 활용한 음성 데이터 분석 및 평가
