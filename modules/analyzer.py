"""
影视片段 AI 分析模块

负责后续判断：
- 哪些片段精彩
- 哪些片段适合做短视频
- 情绪强度
- 冲突程度
- 片段推荐分数
"""

from dataclasses import dataclass


@dataclass
class SceneAnalysis:
    start_time: float
    end_time: float
    score: float
    reason: str


class VideoAnalyzer:
    def analyze_scene(
        self,
        start_time: float,
        end_time: float,
        description: str,
    ) -> SceneAnalysis:
        """
        分析一个影视片段。

        当前使用基础评分接口，
        后续接入 AI 模型后自动判断。
        """

        score = self._calculate_score(description)

        return SceneAnalysis(
            start_time=start_time,
            end_time=end_time,
            score=score,
            reason=description,
        )

    def _calculate_score(self, description: str) -> float:
        """
        当前基础评分。

        后续这里会接入 AI：
        - 剧情冲突
        - 情绪高潮
        - 悬念
        - 人物对白
        - 反转
        """

        keywords = [
            "冲突",
            "反转",
            "高潮",
            "悬念",
            "打斗",
            "感人",
            "震撼",
        ]

        score = 50.0

        for keyword in keywords:
            if keyword in description:
                score += 7.0

        return min(score, 100.0)


if __name__ == "__main__":
    analyzer = VideoAnalyzer()

    result = analyzer.analyze_scene(
        start_time=120,
        end_time=150,
        description="人物发生激烈冲突并出现反转",
    )

    print(result)
