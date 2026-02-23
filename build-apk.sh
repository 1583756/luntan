#!/bin/bash

# ============================================
#  论坛体小说生成器 - APK打包脚本
# ============================================

echo "============================================"
echo "  论坛体小说生成器 - APK打包工具"
echo "============================================"
echo ""

# 检查Node.js
if ! command -v node &> /dev/null; then
    echo "❌ 未检测到 Node.js"
    echo "   请先安装 Node.js: https://nodejs.org"
    exit 1
fi

echo "✅ Node.js 已安装: $(node -v)"

# 检查npm
if ! command -v npm &> /dev/null; then
    echo "❌ 未检测到 npm"
    exit 1
fi

echo "✅ npm 已安装: $(npm -v)"
echo ""

# 询问应用URL
echo "📝 请输入你的应用网址："
echo "   示例："
echo "   - 本地：http://localhost:5000"
echo "   - 云端：https://forum-novel-generator.onrender.com"
echo ""
read -p "URL: " APP_URL

if [ -z "$APP_URL" ]; then
    echo "❌ URL不能为空"
    exit 1
fi

# 创建项目目录
PROJECT_DIR="forum-novel-apk"
echo ""
echo "📁 创建项目目录: $PROJECT_DIR"
mkdir -p "$PROJECT_DIR"
cd "$PROJECT_DIR"

# 初始化npm项目
echo ""
echo "📦 初始化项目..."
npm init -y

# 安装Capacitor
echo ""
echo "📥 安装 Capacitor..."
npm install @capacitor/core @capacitor/cli @capacitor/android --save

# 初始化Capacitor
echo ""
echo "⚙️  初始化 Capacitor..."
npx cap init "论坛小说" com.forum.novel --web-dir www

# 创建www目录
mkdir -p www

# 复制assets内容
echo ""
echo "📋 复制Web资源..."
if [ -d "../assets" ]; then
    cp -r ../assets/* www/
    echo "✅ 已复制assets目录"
else
    echo "⚠️  未找到assets目录"
fi

# 修改manifest.json（如果存在）
if [ -f "www/manifest.json" ]; then
    # 这里可以添加修改manifest.json的逻辑
    echo "✅ manifest.json 已准备"
fi

# 创建capacitor.config.json
echo ""
echo "⚙️  创建 Capacitor 配置..."
cat > capacitor.config.json <<EOF
{
  "appId": "com.forum.novel",
  "appName": "论坛小说",
  "webDir": "www",
  "server": {
    "url": "$APP_URL",
    "cleartext": true,
    "allowNavigation": ["*"]
  },
  "android": {
    "buildOptions": {}
  },
  "plugins": {
    "SplashScreen": {
      "launchShowDuration": 2000,
      "launchAutoHide": true,
      "backgroundColor": "#764ba2",
      "androidSplashResourceName": "splash",
      "androidScaleType": "CENTER_CROP",
      "showSpinner": false,
      "androidSpinnerStyle": "large",
      "spinnerColor": "#999999"
    }
  }
}
EOF

echo "✅ 配置文件已创建"

# 添加Android平台
echo ""
echo "📱 添加 Android 平台..."
npx cap add android

# 同步资源
echo ""
echo "🔄 同步资源到 Android..."
npx cap sync android

echo ""
echo "============================================"
echo "  🎉 准备工作完成！"
echo "============================================"
echo ""
echo "接下来需要手动操作："
echo ""
echo "1️⃣  打开 Android Studio"
echo "   cd android"
echo "   npx cap open android"
echo ""
echo "2️⃣  在 Android Studio 中:"
echo "   - 等待 Gradle 同步完成"
echo "   - 点击 Build → Build Bundle(s)/APK(s) → Build APK(s)"
echo "   - 选择 debug 或 release"
echo "   - 等待构建完成"
echo ""
echo "3️⃣  获取 APK"
echo "   - Debug APK: android/app/build/outputs/apk/debug/app-debug.apk"
echo "   - Release APK: android/app/build/outputs/apk/release/app-release.apk"
echo ""
echo "4️⃣  安装到手机"
echo "   - 将 APK 传到手机"
echo "   - 点击安装"
echo "   - 允许安装未知来源应用"
echo ""
echo "💡 提示:"
echo "   - Debug APK: 用于测试，无需签名"
echo "   - Release APK: 用于发布，需要签名"
echo "   - 首次构建需要下载依赖，可能需要较长时间"
echo ""
echo "需要帮助？查看: APK打包指南.md"
