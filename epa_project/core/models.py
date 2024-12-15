from django.contrib.auth.models import User  # Django 기본 User 모델 사용
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from dotenv import load_dotenv

load_dotenv()


class UserLoginLog(models.Model):
    """사용자 로그인 로그"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 참조
    login_time = models.DateTimeField(auto_now_add=True)  # 로그인 시간
    ip_address = models.GenericIPAddressField(blank=True, null=True)  # IP 주소
    user_agent = models.CharField(
        max_length=255, blank=True, null=True
    )  # 브라우저 정보


class UserSession(models.Model):
    """사용자 세션"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 참조
    session_id = models.CharField(max_length=255)  # 세션 ID
    created_at = models.DateTimeField(auto_now_add=True)  # 세션 생성 시간
    ip_address = models.GenericIPAddressField(blank=True, null=True)  # IP 주소


class LessonNovel(models.Model):
    """동화(Novel) 레슨 정보"""

    level = models.IntegerField()
    title = models.CharField(max_length=255)
    title_kor = models.CharField(max_length=255, blank=True, null=True)  # 한글 제목
    sentence = models.TextField()
    sentence_kor = models.TextField(blank=True, null=True)  # 한글 문장
    audio_file = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["level", "title", "sentence"],
                name="unique_lesson_novel_entry",
            )
        ]

    def __str__(self):
        return f"Novel - Level {self.level} - {self.title}: {self.sentence}"


class LessonConversation(models.Model):
    """회화(Conversation) 레슨 정보"""

    level = models.IntegerField()
    title = models.CharField(max_length=255)
    title_kor = models.CharField(max_length=255, blank=True, null=True)  # 한글 제목
    sentence = models.TextField()
    sentence_kor = models.TextField(blank=True, null=True)  # 한글 문장
    audio_file = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["level", "title", "sentence", "audio_file"],
                name="unique_lesson_conversation_entry",
            )
        ]

    def __str__(self):
        return f"Conversation - Level {self.level} - {self.title}: {self.sentence}"


class LessonPhonics(models.Model):
    """파닉스(Phonics) 레슨 정보"""

    level = models.IntegerField()
    title = models.CharField(max_length=255)
    title_kor = models.CharField(max_length=255, blank=True, null=True)  # 한글 제목
    sentence = models.TextField()
    sentence_kor = models.TextField(blank=True, null=True)  # 한글 문장
    audio_file = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    image_path = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["level", "title", "sentence", "audio_file"],
                name="unique_lesson_phonics_entry",
            )
        ]

    def __str__(self):
        return f"Phonics - Level {self.level} - {self.title}: {self.sentence}"


class ReadingLog(models.Model):
    """사용자가 읽고 있는 도서 로그"""

    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="reading_logs"
    )  # 사용자
    lesson_id = models.PositiveIntegerField()  # 읽었던 Lesson ID
    content_type = models.CharField(
        max_length=50
    )  # 콘텐츠 유형 ('phonics', 'novel', 'conversation')
    title = models.CharField(max_length=255)  # Lesson 제목
    level = models.PositiveIntegerField()  # Lesson 레벨
    last_read_at = models.DateTimeField(auto_now=True)  # 마지막으로 읽은 시간
    last_read_sentence_index = models.PositiveIntegerField(
        default=0
    )  # 마지막으로 읽은 문장 인덱스

    class Meta:
        unique_together = (
            "user",
            "lesson_id",
            "content_type",
        )  # 사용자와 Lesson의 중복 로그 방지

    def __str__(self):
        return f"{self.user.username} - {self.title} (Level {self.level}, Last Sentence Index {self.last_read_sentence_index})"


class UserPronunciation(models.Model):
    """사용자 발음 평가"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 참조
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )  # Lesson 모델 타입
    object_id = models.PositiveIntegerField()  # Lesson 모델 ID
    lesson = GenericForeignKey("content_type", "object_id")  # 다형성 참조
    audio_file = models.URLField()  # 업로드된 음성 파일 S3 URL
    pitch_similarity = models.FloatField(null=True, blank=True)  # 채점 항목1) 피치 패턴 유사도
    rhythm_similarity = models.FloatField(null=True, blank=True)  # 채점 항목2) 리듬 패턴 유사도
    speed_ratio = models.FloatField(null=True, blank=True)  # 채점 항목3) 발화 속도 비율
    pause_similarity = models.FloatField(null=True, blank=True)  # 채점 항목4) 휴지 패턴 유사도
    mispronounced_words = models.JSONField(null=True, blank=True)  # 잘못 인식된 단어 리스트 저장
    mispronounced_ratio = models.FloatField(null=True, blank=True)  # 잘못 인식된 단어 비율
    feedback = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    processed_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=[("pending", "Pending"), ("completed", "Completed")], default="pending")

    def __str__(self):
        return f"User {self.user.id} - {self.lesson}: {self.score}"


class FeedbackLog(models.Model):
    """사용자 피드백 기록"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 참조
    feedback_text = models.TextField()  # 피드백 내용
    created_at = models.DateTimeField(auto_now_add=True)  # 작성 시간


class Recommendation(models.Model):
    """추천 레슨"""

    user = models.ForeignKey(User, on_delete=models.CASCADE)  # 사용자 참조
    content_type = models.ForeignKey(
        ContentType, on_delete=models.CASCADE
    )  # Lesson 모델 타입
    object_id = models.PositiveIntegerField()  # Lesson 모델 ID
    lesson = GenericForeignKey("content_type", "object_id")  # 다형성 참조
    created_at = models.DateTimeField(auto_now_add=True)  # 추천 시간

    def __str__(self):
        return f"Recommendation for User {self.user.id} - {self.lesson}"


class UserScore(models.Model):
    """사용자 점수 누적 관리"""

    user = models.OneToOneField(User, on_delete=models.CASCADE)  # 사용자와 1:1 관계
    total_score = models.FloatField(default=0.0)  # 누적 점수
    last_updated = models.DateTimeField(auto_now=True)  # 마지막 업데이트 시간

    def update_score(self, new_score):
        """새 점수를 추가하고 누적 점수 업데이트"""
        self.total_score += new_score
        self.save()
