#!/usr/bin/env python3
"""
生成App图标
需要安装：pip install cairosvg pillow
"""

try:
    import cairosvg
    from PIL import Image
    import os

    def generate_icons():
        """生成不同尺寸的图标"""
        svg_file = "assets/icon.svg"
        output_dir = "assets"

        if not os.path.exists(svg_file):
            print(f"❌ SVG文件不存在: {svg_file}")
            return False

        # 需要的尺寸
        sizes = [192, 512]

        for size in sizes:
            png_file = f"{output_dir}/icon-{size}.png"

            try:
                # 将SVG转换为PNG
                cairosvg.svg2png(
                    url=svg_file,
                    write_to=png_file,
                    output_width=size,
                    output_height=size
                )
                print(f"✅ 已生成: {png_file} ({size}x{size})")
            except Exception as e:
                print(f"❌ 生成 {png_file} 失败: {e}")
                return False

        print()
        print("🎉 图标生成完成！")
        return True

    if __name__ == "__main__":
        print("=" * 50)
        print("  生成App图标")
        print("=" * 50)
        print()

        # 检查依赖
        try:
            import cairosvg
            import PIL
        except ImportError as e:
            print("❌ 缺少依赖库")
            print(f"   {e}")
            print()
            print("💡 请安装依赖:")
            print("   pip install cairosvg pillow")
            exit(1)

        # 生成图标
        generate_icons()

except ImportError:
    print("❌ 缺少必要的库")
    print()
    print("💡 请安装依赖:")
    print("   pip install cairosvg pillow")
