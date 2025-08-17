#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
GitHub Actions 专用的 IANA TLD 数据更新脚本
基于原始 iana.py，添加了命令行参数支持和错误处理
"""

import argparse
import sys
import os
from iana import IANA

def main():
    parser = argparse.ArgumentParser(description='Update IANA TLD data')
    parser.add_argument('--non-interactive', action='store_true', 
                       help='Run in non-interactive mode')
    parser.add_argument('--overwrite', action='store_true',
                       help='Overwrite existing files')
    parser.add_argument('--verbose', action='store_true',
                       help='Enable verbose output')
    parser.add_argument('--dir', default='data',
                       help='Directory to store data files (default: data)')
    parser.add_argument('--force-download', action='store_true',
                       help='Force download of TLD data')
    
    args = parser.parse_args()
    
    # 确保数据目录存在
    os.makedirs(args.dir, exist_ok=True)
    
    try:
        print("🌐 开始更新 IANA TLD 数据...")
        
        # 初始化 IANA 对象
        iana = IANA(
            dirName=args.dir,
            verbose=args.verbose,
            overwrite=args.overwrite,
            interactive=not args.non_interactive,
            autoProcessAll=True,  # 处理所有TLD
            forceDownloadTld=args.force_download,
        )
        
        print(f"📊 发现 {len(iana.getAllTlds())} 个 TLD")
        
        # 由于autoProcessAll=True，初始化时就会处理所有TLD
        print("✅ TLD 数据更新完成!")
        
        # 检查输出文件
        json_file = os.path.join(args.dir, 'tld.json')
        if os.path.exists(json_file):
            file_size = os.path.getsize(json_file)
            print(f"📄 生成的 JSON 文件大小: {file_size:,} 字节")
        else:
            print("❌ 未找到生成的 JSON 文件")
            return 1
            
        return 0
        
    except KeyboardInterrupt:
        print("\n⚠️ 用户中断了更新过程")
        return 1
    except Exception as e:
        print(f"❌ 更新失败: {e}")
        import traceback
        if args.verbose:
            traceback.print_exc()
        return 1

if __name__ == "__main__":
    sys.exit(main())