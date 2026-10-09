"""
影视素材采集模块

负责后续接入：
- 视频素材来源
- 素材下载
- 素材保存
- 素材信息记录
"""

from pathlib import Path


class VideoCollector:
    def __init__(self, output_dir="output"):
        self.output_dir = Path(output_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def collect(self, source_url):
        """
        采集视频素材。

        当前先建立基础接口，
        后续再接入实际的视频来源和下载模块。
        """
        print(f"准备采集素材：{source_url}")

        return {
            "source": source_url,
            "status": "pending",
        }


if __name__ == "__main__":
    collector = VideoCollector()

    result = collector.collect(
        "https://example.com/video"
    )

    print(result)
