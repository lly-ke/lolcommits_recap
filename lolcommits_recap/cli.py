#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import sys
import os
from . import main as core_main, __version__

def main():
    """命令行入口点"""
    parser = argparse.ArgumentParser(
        description="将Lolcommits提交照片转换成精彩的视频回顾",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  lolcommits_recap                    # 使用默认设置生成视频
  lolcommits_recap --source ~/my_photos  # 指定源目录
  lolcommits_recap --output ./my_videos   # 指定输出目录
        """
    )
    
    parser.add_argument(
        '--source', '-s',
        default=os.path.expanduser('~/.lolcommits'),
        help='Lolcommits照片源目录 (默认: ~/.lolcommits)'
    )
    
    parser.add_argument(
        '--output', '-o',
        default='output_videos',
        help='视频输出目录 (默认: output_videos)'
    )
    
    parser.add_argument(
        '--fps',
        type=int,
        default=1,
        help='视频帧率，控制每张图片显示时间 (默认: 1)'
    )
    
    parser.add_argument(
        '--version', '-v',
        action='version',
        version=f'%(prog)s {__version__}'
    )
    
    args = parser.parse_args()
    
    # 检查源目录是否存在
    if not os.path.exists(args.source):
        print(f"错误: 源目录 '{args.source}' 不存在")
        print("请确保你已经安装并使用了 Lolcommits，或者使用 --source 参数指定正确的目录")
        sys.exit(1)
    
    # 创建输出目录
    os.makedirs(args.output, exist_ok=True)
    
    print(f"Lolcommits Recap v{__version__}")
    print(f"源目录: {args.source}")
    print(f"输出目录: {args.output}")
    print(f"帧率: {args.fps} fps")
    print("-" * 50)
    
    try:
        # 调用核心功能
        core_main(source_dir=args.source, output_dir=args.output, fps=args.fps)
        print("\n✅ 视频生成完成！")
        print(f"📁 输出目录: {os.path.abspath(args.output)}")
        
    except KeyboardInterrupt:
        print("\n❌ 用户中断操作")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ 发生错误: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()
