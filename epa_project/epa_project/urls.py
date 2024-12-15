"""
URL configuration for epa_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
"""

from django.views.generic import RedirectView
from django.contrib import admin
from django.urls import path
from core.views import (
    signup_view,
    login_view,
    logout_view,
    mypage_view,
    library_view,
    UserPronunciationView,
    ProcessAudioLambdaView,
    UpdatePronunciationScoreView,
    lesson_view,
    feedback_view,
    get_lessons,
    # get_learning_books,
    get_reading_books,
)
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse


# 간단한 홈 페이지
def home_view(request):
    return HttpResponse("홈페이지에 오신 것을 환영합니다!")  # 홈 화면 메시지


urlpatterns = [
    path("admin/", admin.site.urls),  # Django Admin
    path("", home_view, name="home"),  # 홈 페이지
    path("signup/", signup_view, name="signup"),  # 회원가입 페이지
    path("login/", login_view, name="login"),  # 로그인 페이지
    path("logout/", logout_view, name="logout"),  # 로그아웃
    path("mypage/", mypage_view, name="mypage"),  # 마이페이지
    path("library/", library_view, name="library"),  # 서재 페이지
    path("lesson/<str:content_type>/<int:lesson_id>/", lesson_view, name="lesson"),  # 문자열 + 정수 지원  # 학습 화면
    path("upload/audio/", UserPronunciationView.as_view(), name="upload_audio"),  # 오디오 업로드
    path("process_audio_lambda/", ProcessAudioLambdaView.as_view(), name="process_audio_lambda"),  # 발음 채점
    path('update_pronunciation_score/', UpdatePronunciationScoreView.as_view(), name='update_pronunciation_score'),
    path("api/lessons/", get_lessons, name="get_lessons"),  # 학습 도서 API
    #path("api/learning_books/", get_learning_books, name="get_learning_books"),  # 학습 도서 목록 API
    path("api/reading_books/", get_reading_books, name="get_reading_books"),  # 읽고 있는 도서 API
    path("feedback/", feedback_view, name="feedback"),  # 발음 피드백 페이지
    path('favicon.ico', RedirectView.as_view(url='/static/favicon.ico', permanent=True)),
]

# 정적 파일 URL 추가 (개발 중에만 사용)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
