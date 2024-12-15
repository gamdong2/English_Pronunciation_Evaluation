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

- **진행 기간**: 2024년 11월 4일 ~ 2024년 11월 29일
- **프로젝트 유형**: 팀 프로젝트

## 프로젝트 목표
- 초등학생 대상의 영어 발음 학습을 위한 웹 애플리케이션 개발
- 학생들의 음성을 표준 음성과 비교하여 발음 평가 점수와 피드백 제공
- 학습 수준에 맞춘 맞춤형 콘텐츠와 흥미를 유도할 수 있는 UX/UI 제공

## 사용한 데이터 셋
- **데이터**:
  - AI Hub의 학습용 아동 영어 음성 데이터
  - Tortoise TTS를 활용해 생성된 표준 영어 음성 데이터

## 워크플로우

1. **데이터 준비**
   - 천재교육 영어 교과서의 학년별 문장 및 어휘를 바탕으로 수준별 스크립트 생성 (Open API) →  표준 음성 데이터 생성 (Tortoise TTS)
  - AI Hub의 아동 영어 음성 데이터를 표준 음성과 비교∙분석하여 피치, 리듬, 발화 속도 등 채점 기준을 수립

2. **데이터 전처리**
   - Librosa를 사용해 음성을 디지털 신호로 변환 후 샘플링 속도 통일 (16,000Hz)
   - Parselmouth를 사용해 억양, 리듬, 음절 길이 추출 및 분석

3. **발음 채점 시스템 설계**
   - Django REST Framework(DRF)를 기반으로 사용자 음성을 S3에 업로드하고 분석하는 REST API 구현
   - 분석 결과를 PostgreSQL 데이터베이스에 저장하고 학습 이력을 관리

4. **결과 시각화 및 피드백 제공**
  - 사용자의 발음 채점 결과를 5가지 항목(피치, 리듬, 속도, 발화 중단 패턴, 잘못 인식된 단어 비율)으로 분석하여 시각화된 결과 제공
   - 학생들에게 격려 및 피드백 메시지를 반환

5. **클라우드 환경 구성**
   - S3를 활용한 음성 데이터 관리 (원어민 음성과 사용자 음성)
   - Docker로 PostgreSQL 데이터베이스 컨테이너화 및 배포

## 프로젝트 결과

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
