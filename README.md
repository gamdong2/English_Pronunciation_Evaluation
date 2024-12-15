# 초등 영어 발음 채점 서비스
![library](https://github.com/user-attachments/assets/dbe2dc05-6514-4469-aada-f464f7a35285)
![epa](https://github.com/user-attachments/assets/0e65d798-b81d-4719-9fc2-61fecf3ae362)

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
  - Tortoise TTS를 활용해 생성된 표준 영어 발화 음성 데이터

## 워크플로우

1. **데이터 준비**
   - AI Hub에서 제공된 음성 데이터를 TTS와 결합하여 학습 데이터 생성
   - 표준 발화 음성을 기준으로 채점 기준 설정 (피치, 리듬, 발화 속도 등)

2. **데이터 전처리**
   - Librosa를 사용해 음성을 디지털 신호로 변환 후 샘플링 속도 통일 (16,000Hz)
   - Parselmouth를 사용해 억양, 리듬, 음절 길이 추출 및 분석

3. **발음 채점 시스템 설계**
   - Django를 기반으로 사용자 음성을 S3에 업로드 후 분석
   - 분석 결과를 PostgreSQL 데이터베이스에 저장하고 학습 이력 관리

4. **결과 시각화 및 피드백 제공**
   - 사용자의 발음 채점 결과를 5가지 항목(피치, 리듬, 속도, 발화 중단 패턴, 발음 정확성)으로 분석하여 시각화된 결과 제공
   - 학생들에게 격려 및 피드백 메시지를 반환

5. **클라우드 환경 구성**
   - S3를 활용한 음성 데이터 관리 (원어민 음성과 사용자 음성)
   - Docker로 PostgreSQL 데이터베이스 컨테이너화 및 배포

6. **성능 평가**
   - 정확도, 처리 속도, 시스템 안정성을 평가하여 실시간 발음 채점 가능 여부 분석

## 프로젝트 결과

### 구현 기능
- **실시간 발음 채점 및 피드백**: 학생들이 녹음한 음성을 기반으로 3초 이내에 채점 결과 제공
- **맞춤형 학습 콘텐츠 제공**: 파닉스, 회화, 소설 카테고리에서 학생 수준에 맞는 콘텐츠 추천
- **Django와 S3 연동**: 데이터 저장 및 관리 자동화

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
- Django와 PostgreSQL 기반의 안정적인 웹 애플리케이션 설계 및 구현
- Librosa와 Parselmouth를 활용한 음성 데이터 분석 및 평가 자동화
