# Lolcommits Recap

将你的 [Lolcommits](https://github.com/lolcommits/lolcommits) 提交照片转换成精彩的视频回顾！这个工具可以自动将你的 git commit 自拍照整理成月度视频和完整的时间轴记录，帮助你回顾编码历程。

[English](./README_EN.md) | 简体中文

## 功能特点

- 自动扫描 `~/.lolcommits` 目录下所有的 Lolcommits 截图
- 按年月自动整理照片
- 为每个月份生成单独的视频回顾
- 生成一个包含所有照片的完整视频总结
- 在视频中显示每张照片的具体拍摄时间
- 支持多种图片格式 (jpg, jpeg, png, gif)
- 自动调整图片尺寸，保持最佳显示效果

## 环境要求

- Python 3.6+
- OpenCV
- Pillow
- NumPy

## 安装

1. 克隆此仓库：
```bash
git clone [repository-url]
cd lolcommits_recap
```

2. 安装依赖：
```bash
pip install -r requirements.txt
```

## 快速开始

```bash
# 生成所有 lolcommits 照片的视频回顾
python lolcommits_recap.py

# 查看生成的视频
open output_videos/final_summary.mp4
```

## 使用方法

1. 确保你已经安装并使用了 [Lolcommits](https://github.com/lolcommits/lolcommits)，并且在 `~/.lolcommits` 目录下有截图。

2. 运行脚本：
```bash
python lolcommits_recap.py
```

3. 脚本会在 `output_videos` 目录下生成以下文件：
   - `photos_YYYY-MM.mp4`：每个月份的单独视频
   - `final_summary.mp4`：包含所有照片的完整视频总结

## 视频规格

- 分辨率：1920x1080 (1080p)
- 帧率：1 fps（每张图片显示1秒）
- 格式：MP4
- 编码：H.264

## 配合 Lolcommits 使用

[Lolcommits](https://github.com/lolcommits/lolcommits) 是一个有趣的工具，它会在你每次 git commit 时自动拍摄一张照片。这个视频生成器可以帮助你：

- 回顾你的编码历程
- 记录你在不同项目上的工作时间
- 创建有趣的开发过程时间轴
- 分享你的编码故事

### Lolcommits 设置建议

为了获得最佳效果，建议在使用 Lolcommits 时：

1. 保持良好的光线条件
2. 调整摄像头角度到合适位置
3. 定期清理不需要的照片
4. 为不同项目设置不同的 Lolcommits 配置

## 自定义选项

如果你想调整视频效果，可以修改以下参数：

- `fps`：在 `create_video()` 函数中修改，控制每张图片的显示时间
- `target_size`：在 `create_video()` 函数中修改，控制视频分辨率
- `image_patterns`：在 `organize_images_by_date()` 函数中修改，支持更多图片格式

## 常见问题

1. Q: 视频播放速度太快/太慢？
   A: 可以在 `lolcommits_recap.py` 中修改 `fps` 参数来调整播放速度。

2. Q: 如何修改视频分辨率？
   A: 在 `create_video()` 函数中修改 `target_size` 参数。

3. Q: 支持哪些图片格式？
   A: 目前支持 jpg、jpeg、png 和 gif 格式。可以在代码中的 `image_patterns` 添加其他格式。

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License
