"""
影视自动剪辑系统统一配置
"""

from pathlib import Path


# 项目根目录
BASE_DIR = Path(__file__).resolve().parent.parent


# 视频目录
OUTPUT_DIR = BASE_DIR / "output"


# 素材目录
MEDIA_DIR = BASE_DIR / "media"


# 临时文件目录
TEMP_DIR = BASE_DIR / "temp"


# 创建必要目录
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)
MEDIA_DIR.mkdir(parents=True, exist_ok=True)
TEMP_DIR.mkdir(parents=True, exist_ok=True)


# 视频默认设置
VIDEO_WIDTH = 1080
VIDEO_HEIGHT = 1920

VIDEO_FPS = 30


# 默认短视频时长
MIN_VIDEO_DURATION = 15
MAX_VIDEO_DURATION = 60


# AI片段最低推荐分数
MIN_SCENE_SCORE = 70


# 默认输出格式
VIDEO_FORMAT = "mp4"
