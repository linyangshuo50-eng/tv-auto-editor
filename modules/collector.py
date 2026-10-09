from pathlib import Path


class VideoCollector:
    """影视素材采集模块。"""

    def __init__(self, source_dir="data/input"):
        self.source_dir = Path(source_dir)

    def collect(self):
        """查找输入目录中的视频文件。"""
        if not self.source_dir.exists():
            return []

        video_extensions = {
            ".mp4",
            ".mkv",
            ".avi",
            ".mov",
            ".webm",
            ".flv",
        }

        return sorted(
            str(path)
            for path in self.source_dir.rglob("*")
            if path.is_file()
            and path.suffix.lower() in video_extensions
        )

    def run(self):
        """执行素材采集。"""
        videos = self.collect()
        print(f"素材采集完成，找到 {len(videos)} 个视频。")
        return videos
