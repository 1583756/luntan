# 📱 APK打包完整指南

## 🎯 目标

将论坛体小说生成器打包成原生Android APK，可以：
- 安装到Android手机
- 在手机上独立运行
- 上传到应用商店
- 分享给朋友

---

## 📦 方案选择

### 方案1：Capacitor（推荐）⭐⭐⭐⭐⭐

**优点**：
- ✅ 最简单快速
- ✅ 直接使用现有Web界面
- ✅ 无需重写代码
- ✅ 自动配置
- ✅ 支持更新

**缺点**：
- ⚠️ 依赖网络（访问后端API）

**适合**：快速打包，利用现有Web界面

**时间**：30分钟

---

### 方案2：Apache Cordova ⭐⭐⭐⭐

**优点**：
- ✅ 成熟稳定
- ✅ 插件丰富
- ✅ 社区活跃

**缺点**：
- ❌ 配置复杂
- ❌ 文档较旧

**适合**：需要复杂原生功能

**时间**：1小时

---

### 方案3：React Native ⭐⭐⭐

**优点**：
- ✅ 完全原生体验
- ✅ 性能最好

**缺点**：
- ❌ 需要重写界面
- ❌ 开发时间长
- ❌ 学习成本高

**适合**：长期维护、需要完全原生

**时间**：数小时到数天

---

### 方案4：Flutter ⭐⭐⭐

**优点**：
- ✅ 跨平台（Android + iOS）
- ✅ 性能好
- ✅ 界面美观

**缺点**：
- ❌ 需要重写代码
- ❌ 学习成本高

**适合**：需要iOS和Android双平台

**时间**：数小时到数天

---

## 🚀 推荐方案：Capacitor详细步骤

### 准备工作

#### 第1步：安装Node.js

**Windows:**
1. 访问：https://nodejs.org
2. 下载LTS版本（推荐18.x或20.x）
3. 双击安装
4. 一路"Next"
5. 安装完成

**验证安装：**
```bash
node -v
npm -v
```

应该看到版本号。

---

#### 第2步：安装JDK

**下载安装：**
1. 访问：https://adoptium.net/
2. 选择版本17或更高
3. 下载安装包
4. 安装

**验证安装：**
```bash
java -version
```

---

#### 第3步：安装Android Studio

**下载安装：**
1. 访问：https://developer.android.com/studio
2. 下载最新版本
3. 安装

**首次配置：**
1. 打开Android Studio
2. 选择 "Standard" 安装
3. 点击 "Next" 接受协议
4. 等待下载SDK（可能需要较长时间）
5. 完成安装

**验证安装：**
```bash
adb version
```

---

### 打包步骤

#### 方法1：使用自动脚本（推荐）

**Linux/Mac:**
```bash
chmod +x build-apk.sh
./build-apk.sh
```

**Windows:**
```bat
build-apk.bat
```

**脚本会自动：**
- 创建项目
- 安装Capacitor
- 复制Web资源
- 配置应用
- 同步到Android

---

#### 方法2：手动步骤

**第1步：创建项目**
```bash
mkdir forum-novel-apk
cd forum-novel-apk
npm init -y
```

**第2步：安装Capacitor**
```bash
npm install @capacitor/core @capacitor/cli @capacitor/android
```

**第3步：初始化Capacitor**
```bash
npx cap init "论坛小说" com.forum.novel --web-dir www
```

**第4步：复制Web资源**
```bash
mkdir www
cp -r ../assets/* www/
```

**第5步：配置应用**

编辑 `capacitor.config.json`：
```json
{
  "appId": "com.forum.novel",
  "appName": "论坛小说",
  "webDir": "www",
  "server": {
    "url": "https://你的应用地址.onrender.com",
    "cleartext": true,
    "allowNavigation": ["*"]
  }
}
```

**第6步：添加Android平台**
```bash
npx cap add android
```

**第7步：同步资源**
```bash
npx cap sync android
```

**第8步：打开Android Studio**
```bash
npx cap open android
```

---

### 使用Android Studio构建APK

**第1步：打开项目**
- 在Android Studio中打开项目
- 等待Gradle同步完成（首次可能需要5-10分钟）

**第2步：构建Debug APK（测试用）**
1. 点击菜单 `Build`
2. 选择 `Build Bundle(s)/APK(s)`
3. 选择 `Build APK(s)`
4. 等待构建完成
5. 点击右下角的 `locate` 查看APK

**APK位置：**
```
android/app/build/outputs/apk/debug/app-debug.apk
```

**第3步：构建Release APK（发布用）**

**方式A：使用调试签名（快速测试）**
1. 点击菜单 `Build`
2. 选择 `Generate Signed Bundle / APK`
3. 选择 `APK`
4. 点击 `Next`
5. 勾选 "Generate unsigned (for app bundle) APK"
6. 选择 `release`
7. 点击 `Finish`

**方式B：使用正式签名（发布到商店）**
1. 生成密钥库：
```bash
keytool -genkey -v -keystore forum-novel.jks -keyalg RSA -keysize 2048 -validity 10000 -alias forum-novel
```
2. 在Android Studio选择 `Generate Signed Bundle / APK`
3. 选择刚生成的密钥库
4. 填入密码和别名
5. 选择 `release`
6. 构建

**APK位置：**
```
android/app/build/outputs/apk/release/app-release.apk
```

---

## 📲 安装APK到手机

### 方法1：USB连接

**第1步：开启USB调试**
- 手机：设置 → 关于手机 → 连续点击"版本号"7次
- 设置 → 开发者选项 → 开启USB调试

**第2步：连接手机**
- USB连接手机
- 手机上允许USB调试

**第3步：安装**
```bash
adb install app-debug.apk
```

### 方法2：蓝牙/云盘

**第1步：传输APK**
- 通过蓝牙、微信、QQ、云盘传输到手机

**第2步：安装**
- 在手机文件管理器找到APK
- 点击安装
- 允许安装未知来源应用

---

## 🎨 自定义应用

### 修改应用名称

编辑 `android/app/src/main/res/values/strings.xml`：
```xml
<string name="app_name">论坛小说</string>
```

### 修改应用图标

**方法1：使用Capacitor Assets**
```bash
npm install @capacitor/assets
npx cap assets:generate
```

**方法2：手动替换**
- 准备图标文件（1024x1024 PNG）
- 替换 `android/app/src/main/res/mipmap-*/ic_launcher.png`

### 修改应用启动页

编辑 `capacitor.config.json`：
```json
{
  "plugins": {
    "SplashScreen": {
      "launchShowDuration": 2000,
      "backgroundColor": "#764ba2"
    }
  }
}
```

---

## 📊 Debug vs Release

| 特性 | Debug APK | Release APK |
|------|-----------|-------------|
| 用途 | 测试 | 发布 |
| 签名 | 调试签名 | 正式签名 |
| 大小 | 较大 | 较小 |
| 性能 | 一般 | 优化后 |
| 可发布 | ❌ | ✅ |
| 上传商店 | ❌ | ✅ |

---

## 🆘 常见问题

### Q: 构建失败，提示Gradle错误
A: 检查网络，确保能访问maven仓库，或使用国内镜像

### Q: APK体积很大
A: Release APK会自动优化，减小体积

### Q: 安装失败
A: 确保开启"允许安装未知来源应用"

### Q: 应用无法联网
A: 检查AndroidManifest.xml是否有网络权限，Capacitor会自动添加

### Q: 如何更新应用？
A: 修改代码后，重新构建APK，重新安装即可

### Q: 可以上架应用商店吗？
A: 可以！使用Release APK并正式签名后，可以上传到Google Play

---

## 🎯 快速开始（总结）

### 最快方式（30分钟）：

**Windows:**
```bat
build-apk.bat
```

**Linux/Mac:**
```bash
./build-apk.sh
```

然后：
1. 在Android Studio打开项目
2. Build → Build APK(s)
3. 获取APK文件
4. 传到手机安装

### 注意事项：

1. **首次构建**：需要下载依赖，时间较长（5-10分钟）
2. **应用URL**：需要配置后端API地址
3. **网络权限**：Capacitor自动添加，无需手动配置
4. **发布签名**：上架商店需要正式签名

---

## 📚 相关资源

- [Capacitor官方文档](https://capacitorjs.com/docs)
- [Android Studio下载](https://developer.android.com/studio)
- [Node.js下载](https://nodejs.org)

---

**立即开始打包APK吧！** 🚀

使用自动脚本，30分钟内完成APK打包！
