# Lolcommits Recap

Transform your [Lolcommits](https://github.com/lolcommits/lolcommits) photos into amazing video recaps! This tool automatically organizes your git commit selfies into monthly videos and a complete timeline, helping you relive your coding journey.

English | [简体中文](./README.md)

## Features

- Automatically scans all Lolcommits photos in `~/.lolcommits`
- Organizes photos by year and month
- Generates individual monthly recap videos
- Creates a complete video summary with all photos
- Displays timestamp for each photo in the video
- Supports multiple image formats (jpg, jpeg, png, gif)
- Automatically adjusts image size for optimal display

## Requirements

- Python 3.6+
- OpenCV
- Pillow
- NumPy

## Installation

1. Clone this repository:
```bash
git clone [repository-url]
cd lolcommits_recap
```

2. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have [Lolcommits](https://github.com/lolcommits/lolcommits) installed and configured.

## Quick Start

```bash
# Generate video recaps for all lolcommits photos
python lolcommits_recap.py

# View the generated video
open output_videos/final_summary.mp4
```

## Usage

1. Ensure you have [Lolcommits](https://github.com/lolcommits/lolcommits) installed and have some photos in `~/.lolcommits`.

2. Run the script:
```bash
python lolcommits_recap.py
```

3. Find the generated videos in the `output_videos` directory:
   - `photos_YYYY-MM.mp4`: Individual monthly videos
   - `final_summary.mp4`: Complete video summary with all photos

## Video Specifications

- Resolution: 1920x1080 (1080p)
- Frame Rate: 1 fps (each photo shows for 1 second)
- Format: MP4
- Codec: H.264

## Integration with Lolcommits

[Lolcommits](https://github.com/lolcommits/lolcommits) takes a photo every time you make a git commit. This video generator helps you:

- Review your coding journey
- Track time spent on different projects
- Create an interesting development timeline
- Share your coding story

### Lolcommits Setup Tips

For best results with Lolcommits:

1. Ensure good lighting conditions
2. Adjust camera angle appropriately
3. Regularly clean up unnecessary photos
4. Set different Lolcommits configs for different projects

## Customization

You can adjust the following parameters:

- `fps`: In `create_video()` function to control photo display duration
- `target_size`: In `create_video()` function to control video resolution
- `image_patterns`: In `organize_images_by_date()` function to support more image formats

## FAQ

1. Q: Video playback is too fast/slow?
   A: Modify the `fps` parameter in `lolcommits_recap.py`.

2. Q: How to change video resolution?
   A: Modify the `target_size` parameter in the `create_video()` function.

3. Q: What image formats are supported?
   A: Currently supports jpg, jpeg, png, and gif formats. You can add more formats in the `image_patterns` list.

## Contributing

Issues and Pull Requests are welcome!

## License

MIT License
