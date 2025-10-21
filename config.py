import pytz

# 시간대
KST = pytz.timezone("Asia/Seoul")

# 서버 관련 설정
SERVER_URL = "https://discord.com/channels/1310854848442269767"
BACKUP_CHANNEL_ID = 1427608696547967026

# 점수 기준
DAILY_GOAL_POINTS = 10
WEEK_GOAL_POINTS = 50
WEEKLY_BEST_THRESHOLD = 60
MONTHLY_BEST_THRESHOLD = 200

# 채널 점수 체계
CHANNEL_POINTS = {
    1423170386811682908: {"name": "일일-그림보고", "points": 6, "daily_max": 6, "image_only": True},
    1423172691724079145: {"name": "자유채팅판", "points": 1, "daily_max": 4, "image_only": False},
    1423359059566006272: {"name": "정보-공모전", "points": 1, "daily_max": 1, "image_only": False},
    1423170949477568623: {"name": "정보-그림꿀팁", "points": 1, "daily_max": 1, "image_only": False},
    1423242322665148531: {"name": "고민상담", "points": 1, "daily_max": 1, "image_only": False},
    1423359791287242782: {"name": "출퇴근기록", "points": 4, "daily_max": 4, "image_only": False},
    1423171509752434790: {"name": "다-그렸어요", "points": 5, "daily_max": 5, "image_only": True},
}
