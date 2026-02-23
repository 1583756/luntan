#!/usr/bin/env python3
"""
生成应用二维码的脚本
需要安装：pip install qrcode
"""

import qrcode
import sys
import os

def generate_qr_code(url, output_file="qrcode.png"):
    """
    生成二维码

    Args:
        url: 要生成的网址
        output_file: 输出文件名
    """
    try:
        # 创建QR码实例
        qr = qrcode.QRCode(
            version=1,
            error_correction=qrcode.constants.ERROR_CORRECT_L,
            box_size=10,
            border=4,
        )

        # 添加数据
        qr.add_data(url)
        qr.make(fit=True)

        # 创建图像
        img = qr.make_image(fill_color="purple", back_color="white")

        # 保存
        img.save(output_file)
        print(f"✅ 二维码已生成: {output_file}")
        print(f"📱 扫描二维码访问: {url}")
        return True

    except ImportError:
        print("❌ 未安装 qrcode 库")
        print("💡 安装命令: pip install qrcode")
        return False
    except Exception as e:
        print(f"❌ 生成二维码失败: {e}")
        return False

def main():
    """主函数"""
    print("=" * 50)
    print("  论坛体小说生成器 - 二维码生成工具")
    print("=" * 50)
    print()

    # 获取URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        print("📝 请输入你的应用网址:")
        print("   示例: https://forum-novel-generator.onrender.com")
        print()
        url = input("URL: ").strip()

    if not url:
        print("❌ URL不能为空")
        return

    # 检查URL格式
    if not url.startswith(("http://", "https://")):
        url = "https://" + url
        print(f"💡 自动添加 https:// 前缀")
        print(f"   完整网址: {url}")

    print()
    print("🔄 正在生成二维码...")
    print()

    # 生成二维码
    output_file = "assets/qrcode.png"
    success = generate_qr_code(url, output_file)

    if success:
        print()
        print("=" * 50)
        print("  生成完成！")
        print("=" * 50)
        print()
        print("📱 使用方法:")
        print(f"   1. 打开 {output_file}")
        print("   2. 用手机扫码")
        print("   3. 开始使用论坛体小说生成器！")
        print()
        print("💡 提示:")
        print("   - 可以打印出来贴在墙上")
        print("   - 可以分享二维码图片")
        print("   - 可以嵌入到你的网站中")
    else:
        print()
        print("=" * 50)
        print("  生成失败")
        print("=" * 50)
        print()
        print("💡 请先安装 qrcode 库:")
        print("   pip install qrcode")

if __name__ == "__main__":
    main()
