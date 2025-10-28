# Lolcommits Recap

🎬 **将你的 Lolcommits 提交照片转换成精彩的视频回顾！**

这个工具可以自动将你的 git commit 自拍照整理成月度视频和完整的时间轴记录，帮助你回顾编码历程，记录每一个重要的开发时刻。

[English](./README_EN.md) | 简体中文

## ✨ 功能特点

- 🔍 **智能扫描**: 自动扫描 `~/.lolcommits` 目录下所有的 Lolcommits 截图
- 📅 **时间整理**: 按年月自动整理照片，创建有序的时间轴
- 🎥 **月度视频**: 为每个月份生成单独的精彩视频回顾
- 🎬 **完整总结**: 生成包含所有照片的完整视频总结
- ⏰ **时间戳显示**: 在视频中显示每张照片的具体拍摄时间
- 🖼️ **多格式支持**: 支持 jpg、jpeg、png、gif 等多种图片格式
- 🎨 **智能适配**: 自动调整图片尺寸，保持最佳显示效果

## 📋 环境要求

- **Python**: 3.6 或更高版本
- **OpenCV**: 用于视频处理和生成
- **Pillow**: 用于图片处理和格式转换
- **NumPy**: 用于数值计算和数组操作
- **tqdm**: 用于显示进度条

## 🚀 安装

### 从 PyPI 安装（推荐）
```bash
pip install lolcommits_recap
```

### 从源码安装
1. 克隆此仓库：
```bash
git clone https://github.com/lly-ke/lolcommits_recap
cd lolcommits_recap
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## ⚡ 快速开始

```bash
# 使用默认设置生成视频
lolcommits_recap

# 指定源目录
lolcommits_recap --source ~/my_photos

# 指定输出目录
lolcommits_recap --output ./my_videos

# 调整播放速度（每张图片显示2秒）
lolcommits_recap --fps 0.5

# 查看帮助信息
lolcommits_recap --help
```

## 📖 使用方法

1. **准备工作**: 确保你已经安装并使用了 [Lolcommits](https://github.com/lolcommits/lolcommits)，并且在 `~/.lolcommits` 目录下有截图。

2. **运行命令**：
```bash
lolcommits_recap
```

3. **查看结果**: 脚本会在 `output_videos` 目录下生成以下文件：
   - `photos_YYYY-MM.mp4`：每个月份的单独视频
   - `final_summary.mp4`：包含所有照片的完整视频总结

## 🎥 视频规格

- **分辨率**: 1920x1080 (1080p 高清)
- **帧率**: 1 fps（每张图片显示1秒，可通过 `--fps` 参数调整）
- **格式**: MP4
- **编码**: H.264

## 🔗 配合 Lolcommits 使用

[Lolcommits](https://github.com/lolcommits/lolcommits) 是一个有趣的工具，它会在你每次 git commit 时自动拍摄一张照片。这个视频生成器可以帮助你：

- 📈 **回顾编码历程**: 通过时间轴视频回顾你的开发过程
- ⏱️ **记录工作时间**: 追踪你在不同项目上的工作时间
- 🎬 **创建时间轴**: 制作有趣的开发过程时间轴视频
- 📤 **分享故事**: 与团队或社区分享你的编码故事

### 💡 Lolcommits 设置建议

为了获得最佳效果，建议在使用 Lolcommits 时：

1. **光线条件**: 保持良好的光线条件，确保照片清晰
2. **摄像头角度**: 调整摄像头角度到合适位置
3. **定期清理**: 定期清理不需要的照片，保持目录整洁
4. **项目配置**: 为不同项目设置不同的 Lolcommits 配置

## ⚙️ 命令行参数

| 参数 | 简写 | 说明 | 默认值 |
|------|------|------|--------|
| `--source` | `-s` | 指定Lolcommits照片源目录 | `~/.lolcommits` |
| `--output` | `-o` | 指定视频输出目录 | `output_videos` |
| `--fps` | - | 设置视频帧率，控制每张图片显示时间 | `1` |
| `--version` | `-v` | 显示版本信息 | - |
| `--help` | `-h` | 显示帮助信息 | - |

## 🎯 使用示例

```bash
lolcommits_recap                    # 默认设置
lolcommits_recap --source ~/photos  # 指定源目录
lolcommits_recap --output ./videos  # 指定输出目录
lolcommits_recap --fps 0.5          # 调整播放速度
```

## 🛠️ 自定义选项

如果你想调整视频效果，可以修改以下参数：

- **fps**: 通过 `--fps` 参数控制每张图片的显示时间
- **target_size**: 在源码中修改，控制视频分辨率
- **image_patterns**: 在源码中修改，支持更多图片格式

## ❓ 常见问题

### Q: 视频播放速度太快/太慢？
**A**: 可以使用 `--fps` 参数来调整播放速度，例如 `lolcommits_recap --fps 0.5` 让每张图片显示2秒。

### Q: 如何修改视频分辨率？
**A**: 目前固定为1080p，如需修改请查看源码中的 `target_size` 参数。

### Q: 支持哪些图片格式？
**A**: 目前支持 jpg、jpeg、png 和 gif 格式。

### Q: 如何指定不同的源目录？
**A**: 使用 `--source` 参数，例如 `lolcommits_recap --source /path/to/photos`。

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

- 🐛 **报告问题**: 在 [Issues](https://github.com/lly-ke/lolcommits_recap/issues) 中报告 bug 或提出功能建议
- 💻 **贡献代码**: 提交 Pull Request 来改进项目
- 📖 **完善文档**: 帮助改进文档和示例

## 📄 许可证

MIT License
