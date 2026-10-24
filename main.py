# main.py
import sys
from src.utils import get_current_time, ensure_dir
from config.settings import APP_NAME, VERSION

def run():
    print("🚀 项目开始运行...")
    print(f"📦 {APP_NAME} v{VERSION}")
    print(f"🕒 当前时间: {get_current_time()}")

    output_dir = "data/output"
    ensure_dir(output_dir)
    print(f"📁 数据输出目录已准备就绪: {output_dir}")

    print("✅ 运行结束！")


if __name__ == "__main__":
    run()