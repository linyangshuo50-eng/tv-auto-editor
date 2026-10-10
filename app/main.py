"""
影视自动剪辑系统主程序
"""

from modules.collector import VideoCollector
from modules.analyzer import VideoAnalyzer
from modules.editor import VideoEditor
from modules.writer import VideoWriter


def main():
    print("=" * 50)
    print("影视自动剪辑系统")
    print("=" * 50)

    # 初始化模块
    collector = VideoCollector()
    analyzer = VideoAnalyzer()
    editor = VideoEditor()
    writer = VideoWriter()

    print("\n[1] 素材采集模块：已加载")
    print("[2] AI分析模块：已加载")
    print("[3] 自动剪辑模块：已加载")
    print("[4] 文案生成模块：已加载")

    # 测试 AI 分析
    scene = analyzer.analyze_scene(
        start_time=120,
        end_time=150,
        description="人物发生激烈冲突并出现反转",
    )

    print("\nAI片段分析结果：")
    print(f"开始时间：{scene.start_time} 秒")
    print(f"结束时间：{scene.end_time} 秒")
    print(f"推荐分数：{scene.score}")
    print(f"推荐原因：{scene.reason}")

    # 测试文案生成
    content = writer.generate(
        "主角意外发现隐藏真相"
    )

    print("\n自动生成文案：")
    print(f"标题：{content['title']}")
    print(f"简介：{content['description']}")
    print(f"标签：{' '.join(content['tags'])}")

    print("\n系统初始化完成。")


if __name__ == "__main__":
    main()
