# Lolcommits Recap

🎬 **Transform your Lolcommits photos into amazing video recaps!**

This tool automatically organizes your git commit selfies into monthly videos and a complete timeline, helping you relive your coding journey and capture every important development moment.

English | [简体中文](./README.md)

## ✨ Features

- 🔍 **Smart Scanning**: Automatically scans all Lolcommits photos in `~/.lolcommits`
- 📅 **Time Organization**: Organizes photos by year and month, creating an ordered timeline
- 🎥 **Monthly Videos**: Generates individual monthly recap videos
- 🎬 **Complete Summary**: Creates a complete video summary with all photos
- ⏰ **Timestamp Display**: Shows timestamp for each photo in the video
- 🖼️ **Multi-format Support**: Supports jpg, jpeg, png, gif and other image formats
- 🎨 **Smart Adaptation**: Automatically adjusts image size for optimal display

## 📋 Requirements

- **Python**: 3.6 or higher
- **OpenCV**: For video processing and generation
- **Pillow**: For image processing and format conversion
- **NumPy**: For numerical calculations and array operations
- **tqdm**: For progress bar display

## 🚀 Installation

### Install from PyPI (Recommended)
```bash
pip install lolcommits_recap
```

### Install from Source
1. Clone this repository:
```bash
git clone https://github.com/lly-ke/lolcommits_recap
cd lolcommits_recap
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

## ⚡ Quick Start

```bash
# Generate video recaps with default settings
lolcommits_recap

# Specify source directory
lolcommits_recap --source ~/my_photos

# Specify output directory
lolcommits_recap --output ./my_videos

# Adjust playback speed (each photo shows for 2 seconds)
lolcommits_recap --fps 0.5

# View help information
lolcommits_recap --help
```

## 📖 Usage

1. **Prerequisites**: Ensure you have [Lolcommits](https://github.com/lolcommits/lolcommits) installed and have some photos in `~/.lolcommits`.

2. **Run the command**:
```bash
lolcommits_recap
```

3. **View results**: Find the generated videos in the `output_videos` directory:
   - `photos_YYYY-MM.mp4`: Individual monthly videos
   - `final_summary.mp4`: Complete video summary with all photos

## 🎥 Video Specifications

- **Resolution**: 1920x1080 (1080p HD)
- **Frame Rate**: 1 fps (each photo shows for 1 second, adjustable via `--fps` parameter)
- **Format**: MP4
- **Codec**: H.264

## 🔗 Integration with Lolcommits

[Lolcommits](https://github.com/lolcommits/lolcommits) takes a photo every time you make a git commit. This video generator helps you:

- 📈 **Review Coding Journey**: Relive your development process through timeline videos
- ⏱️ **Track Work Time**: Monitor time spent on different projects
- 🎬 **Create Timeline**: Make interesting development process timeline videos
- 📤 **Share Stories**: Share your coding story with team or community

### 💡 Lolcommits Setup Tips

For best results with Lolcommits:

1. **Lighting**: Ensure good lighting conditions for clear photos
2. **Camera Angle**: Adjust camera angle appropriately
3. **Regular Cleanup**: Regularly clean up unnecessary photos to keep directory organized
4. **Project Configuration**: Set different Lolcommits configs for different projects

## ⚙️ Command Line Parameters

| Parameter | Short | Description | Default |
|-----------|-------|-------------|---------|
| `--source` | `-s` | Specify Lolcommits photos source directory | `~/.lolcommits` |
| `--output` | `-o` | Specify video output directory | `output_videos` |
| `--fps` | - | Set video frame rate, control photo display duration | `1` |
| `--version` | `-v` | Show version information | - |
| `--help` | `-h` | Show help information | - |

## 🎯 Usage Examples

```bash
lolcommits_recap                    # Default settings
lolcommits_recap --source ~/photos  # Specify source directory
lolcommits_recap --output ./videos  # Specify output directory
lolcommits_recap --fps 0.5          # Adjust playback speed
```

## 🛠️ Customization

You can adjust the following parameters:

- **fps**: Control photo display duration via `--fps` parameter
- **target_size**: Modify in source code to control video resolution
- **image_patterns**: Modify in source code to support more image formats

## ❓ FAQ

### Q: Video playback is too fast/slow?
**A**: Use the `--fps` parameter to adjust playback speed, e.g., `lolcommits_recap --fps 0.5` to show each photo for 2 seconds.

### Q: How to change video resolution?
**A**: Currently fixed at 1080p. To modify, check the `target_size` parameter in the source code.

### Q: What image formats are supported?
**A**: Currently supports jpg, jpeg, png, and gif formats.

### Q: How to specify a different source directory?
**A**: Use the `--source` parameter, e.g., `lolcommits_recap --source /path/to/photos`.

## 🤝 Contributing

Issues and Pull Requests are welcome!

- 🐛 **Report Issues**: Report bugs or suggest features in [Issues](https://github.com/lly-ke/lolcommits_recap/issues)
- 💻 **Contribute Code**: Submit Pull Requests to improve the project
- 📖 **Improve Documentation**: Help improve documentation and examples

## 📄 License

MIT License
