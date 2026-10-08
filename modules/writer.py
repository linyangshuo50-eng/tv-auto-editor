"""
影视短视频文案生成模块

负责生成：
- 视频标题
- 视频简介
- 发布文案
- 话题标签

当前为基础版本，
后续可以接入 AI 自动生成。
"""


class VideoWriter:

    def generate_title(self, topic):
        """生成视频标题"""
        return f"这段剧情太精彩了：{topic}"

    def generate_description(self, topic):
        """生成视频简介"""
        return (
            f"精彩影视片段：{topic}。"
            "完整剧情请观看视频。"
        )

    def generate_tags(self, topic):
        """生成话题标签"""
        return [
            "#影视剪辑",
            "#影视推荐",
            "#精彩片段",
            f"#{topic}",
        ]

    def generate(self, topic):
        """一次生成完整发布文案"""

        return {
            "title": self.generate_title(topic),
            "description": self.generate_description(topic),
            "tags": self.generate_tags(topic),
        }


if __name__ == "__main__":

    writer = VideoWriter()

    result = writer.generate(
        "主角意外发现隐藏真相"
    )

    print("标题：")
    print(result["title"])

    print("\n简介：")
    print(result["description"])

    print("\n标签：")
    print(" ".join(result["tags"]))
