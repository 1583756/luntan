@echo off
chcp 65001 >nul
echo ============================================
echo   论坛体小说生成器 - APK打包工具
echo ============================================
echo.

REM 检查Node.js
where node >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ 未检测到 Node.js
    echo    请先安装 Node.js: https://nodejs.org
    pause
    exit /b 1
)

echo ✅ Node.js 已安装
node -v

REM 检查npm
where npm >nul 2>&1
if %ERRORLEVEL% NEQ 0 (
    echo ❌ 未检测到 npm
    pause
    exit /b 1
)

echo ✅ npm 已安装
npm -v
echo.

REM 询问应用URL
echo 📝 请输入你的应用网址：
echo    示例：
echo    - 本地：http://localhost:5000
echo    - 云端：https://forum-novel-generator.onrender.com
echo.
set /p APP_URL="URL: "

if "%APP_URL%"=="" (
    echo ❌ URL不能为空
    pause
    exit /b 1
)

REM 创建项目目录
set PROJECT_DIR=forum-novel-apk
echo.
echo 📁 创建项目目录: %PROJECT_DIR%
mkdir %PROJECT_DIR% 2>nul
cd %PROJECT_DIR%

REM 初始化npm项目
echo.
echo 📦 初始化项目...
call npm init -y

REM 安装Capacitor
echo.
echo 📥 安装 Capacitor...
call npm install @capacitor/core @capacitor/cli @capacitor/android --save

REM 初始化Capacitor
echo.
echo ⚙️  初始化 Capacitor...
call npx cap init "论坛小说" com.forum.novel --web-dir www

REM 创建www目录
mkdir www 2>nul

REM 复制assets内容
echo.
echo 📋 复制Web资源...
if exist "..\assets" (
    xcopy ..\assets www\ /E /I /Y
    echo ✅ 已复制assets目录
) else (
    echo ⚠️  未找到assets目录
)

REM 创建capacitor.config.json
echo.
echo ⚙️  创建 Capacitor 配置...
(
echo {
echo   "appId": "com.forum.novel",
echo   "appName": "论坛小说",
echo   "webDir": "www",
echo   "server": {
echo     "url": "%APP_URL%",
echo     "cleartext": true,
echo     "allowNavigation": ["*"]
echo   },
echo   "android": {
echo     "buildOptions": {}
echo   },
echo   "plugins": {
echo     "SplashScreen": {
echo       "launchShowDuration": 2000,
echo       "launchAutoHide": true,
echo       "backgroundColor": "#764ba2",
echo       "androidSplashResourceName": "splash",
echo       "androidScaleType": "CENTER_CROP",
echo       "showSpinner": false,
echo       "androidSpinnerStyle": "large",
echo       "spinnerColor": "#999999"
echo     }
echo   }
echo }
) > capacitor.config.json

echo ✅ 配置文件已创建

REM 添加Android平台
echo.
echo 📱 添加 Android 平台...
call npx cap add android

REM 同步资源
echo.
echo 🔄 同步资源到 Android...
call npx cap sync android

echo.
echo ============================================
echo   🎉 准备工作完成！
echo ============================================
echo.
echo 接下来需要手动操作：
echo.
echo 1️⃣  打开 Android Studio
echo    cd android
echo    npx cap open android
echo.
echo 2️⃣  在 Android Studio 中:
echo    - 等待 Gradle 同步完成
echo    - 点击 Build → Build Bundle(s)/APK(s) → Build APK(s)
echo    - 选择 debug 或 release
echo    - 等待构建完成
echo.
echo 3️⃣  获取 APK
echo    - Debug APK: android\app\build\outputs\apk\debug\app-debug.apk
echo    - Release APK: android\app\build\outputs\apk\release\app-release.apk
echo.
echo 4️⃣  安装到手机
echo    - 将 APK 传到手机
echo    - 点击安装
echo    - 允许安装未知来源应用
echo.
echo 💡 提示:
echo    - Debug APK: 用于测试，无需签名
echo    - Release APK: 用于发布，需要签名
echo    - 首次构建需要下载依赖，可能需要较长时间
echo.
echo 需要帮助？查看: APK打包指南.md
echo.
pause
