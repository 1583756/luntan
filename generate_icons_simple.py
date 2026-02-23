#!/usr/bin/env python3
"""
生成App图标（使用PIL）
需要安装：pip install pillow
"""

try:
    from PIL import Image, ImageDraw, ImageFont
    import os

    def generate_icon(size):
        """生成指定尺寸的图标"""
        # 创建画布
        img = Image.new('RGB', (size, size), color='#764ba2')
        draw = ImageDraw.Draw(img)

        # 绘制渐变背景（简化版）
        for y in range(size):
            r = int(102 + (118 - 102) * y / size)
            g = int(126 + (75 - 126) * y / size)
            b = int(234 + (162 - 234) * y / size)
            draw.line([(0, y), (size, y)], fill=(r, g, b))

        # 绘制边框
        border_radius = size // 5
        draw.rounded_rectangle(
            [(0, 0), (size-1, size-1)],
            radius=border_radius,
            outline='#ffffff',
            width=size // 50
        )

        # 绘制书籍图标（简化版）
        center_x = size // 2
        center_y = size // 2 - size // 10
        book_size = size // 3

        # 书本主体
        draw.rectangle(
            [(center_x - book_size, center_y - book_size // 2),
             (center_x + book_size, center_y + book_size // 2)],
            fill='#ffffff',
            outline='#ffffff'
        )

        # 书本中线
        draw.line(
            [(center_x, center_y - book_size // 2),
             (center_x, center_y + book_size // 2)],
            fill='#764ba2',
            width=2
        )

        # 书页效果
        for i in range(1, 4):
            y_pos = center_y - book_size // 2 + (book_size // 2) * i / 4
            draw.line(
                [(center_x - book_size + 5, y_pos),
                 (center_x - 5, y_pos)],
                fill='#764ba2',
                width=1
            )
            draw.line(
                [(center_x + 5, y_pos),
                 (center_x + book_size - 5, y_pos)],
                fill='#764ba2',
                width=1
            )

        return img

    def main():
        """主函数"""
        print("=" * 50)
        print("  生成App图标")
        print("=" * 50)
        print()

        # 检查输出目录
        output_dir = "assets"
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)

        # 需要的尺寸
        sizes = [192, 512]

        for size in sizes:
            png_file = f"{output_dir}/icon-{size}.png"

            try:
                # 生成图标
                img = generate_icon(size)

                # 保存
                img.save(png_file, 'PNG')
                print(f"✅ 已生成: {png_file} ({size}x{size})")

            except Exception as e:
                print(f"❌ 生成 {png_file} 失败: {e}")
                return False

        print()
        print("🎉 图标生成完成！")
        print()
        print("💡 PWA配置已完成，你的应用现在可以：")
        print("   - 添加到主屏幕（像原生App）")
        print("   - 支持离线使用")
        print("   - 拥有自己的图标")
        print("   - 全屏显示")
        print()
        print("📱 使用方法：")
        print("   iOS: Safari → 分享 → 添加到主屏幕")
        print("   Android: Chrome → 菜单 → 添加到主屏幕")
        return True

    if __name__ == "__main__":
        main()

except ImportError:
    print("❌ 缺少必要的库")
    print()
    print("💡 请安装依赖:")
    print("   pip install pillow")
