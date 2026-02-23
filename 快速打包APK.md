# 🚀 快速打包APK（10分钟）

## 前提条件

1. **Node.js** - https://nodejs.org
2. **JDK 17+** - https://adoptium.net/
3. **Android Studio** - https://developer.android.com/studio

## 第1步：准备后端

**必须先部署到云端！**

```bash
# 运行部署脚本
./deploy-to-render.sh
```

获得云端地址，如：
```
https://forum-novel-generator.onrender.com
```

**APK需要这个地址才能访问API！**

---

## 第2步：使用自动脚本

### Windows：
```bat
build-apk.bat
```

### Linux/Mac：
```bash
chmod +x build-apk.sh
./build-apk.sh
```

脚本会询问你的应用URL，输入云端地址即可。

---

## 第3步：在Android Studio构建APK

1. **打开Android Studio**
   - 脚本会自动打开
   - 或手动运行：`npx cap open android`

2. **等待Gradle同步**
   - 首次需要5-10分钟
   - 等待右下角进度条完成

3. **构建APK**
   - 菜单：`Build` → `Build Bundle(s)/APK(s)` → `Build APK(s)`
   - 等待构建完成
   - 点击右下角 `locate`

4. **获取APK**
   - Debug APK: `android/app/build/outputs/apk/debug/app-debug.apk`
   - 传到手机安装

---

## 第4步：安装到手机

### USB连接：
```bash
adb install app-debug.apk
```

### 或直接传输：
- 通过微信、QQ、云盘传到手机
- 点击安装
- 允许安装未知来源

---

## 🎯 完成！

你的手机上现在有一个"论坛小说"应用了！

点击图标，直接使用，无需浏览器！

---

## 💡 注意事项

1. **必须先部署云端** - APK需要访问后端API
2. **首次构建慢** - 需要下载依赖，5-10分钟
3. **Debug APK** - 用于测试，无需签名
4. **Release APK** - 需要签名，可上架商店

---

## 🆘 遇到问题？

查看详细文档：[APK打包指南.md](APK打包指南.md)

常见问题：
- Gradle错误 → 检查网络
- 构建失败 → 清理项目：`./gradlew clean`
- 安装失败 → 允许安装未知来源

---

**立即开始！运行 `build-apk.bat`（Windows）或 `./build-apk.sh`（Linux/Mac）** 🚀
