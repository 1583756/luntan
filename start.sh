#!/bin/bash

# 论坛体小说生成器 - 启动脚本

echo "========================================="
echo "  论坛体小说生成器"
echo "========================================="
echo ""

# 检查Python是否安装
if ! command -v python &> /dev/null
then
    echo "❌ 错误：未检测到Python，请先安装Python"
    exit 1
fi

echo "✅ Python已安装"
echo ""

# 默认端口
PORT=5000

# 检查是否指定了端口参数
if [ ! -z "$1" ]; then
    PORT=$1
fi

echo "🚀 正在启动服务..."
echo "📡 服务端口: $PORT"
echo "🌐 访问地址: http://localhost:$PORT"
echo "📱 Web界面: http://localhost:$PORT/assets/index.html"
echo ""
echo "⚠️  按 Ctrl+C 停止服务"
echo ""
echo "========================================="
echo ""

# 启动服务
python src/main.py -m http -p $PORT
