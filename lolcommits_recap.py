import os
from datetime import datetime
import cv2
import numpy as np
from PIL import Image
import glob
from collections import defaultdict
from tqdm import tqdm

def get_image_creation_time(image_path):
    """获取图片的创建时间"""
    return datetime.fromtimestamp(os.path.getctime(image_path))

def organize_images_by_date(source_dir):
    """将图片按年月分类"""
    images_by_date = defaultdict(list)
    
    # 支持的图片格式
    image_patterns = ['*.jpg', '*.jpeg', '*.png', '*.gif']
    image_files = []
    
    print("正在扫描图片文件...")
    # 递归遍历所有子目录
    for root, _, _ in os.walk(source_dir):
        for pattern in image_patterns:
            image_files.extend(glob.glob(os.path.join(root, pattern)))
    
    print(f"找到 {len(image_files)} 张图片，正在整理...")
    for image_path in tqdm(image_files, desc="整理图片"):
        creation_time = get_image_creation_time(image_path)
        year_month = creation_time.strftime('%Y-%m')
        images_by_date[year_month].append((image_path, creation_time))
    
    # 对每个月份内的图片按时间排序
    for year_month in images_by_date:
        images_by_date[year_month].sort(key=lambda x: x[1])
    
    return images_by_date

def create_video(images_with_dates, output_path, fps=1):
    """创建视频，显示图片创建时间"""
    if not images_with_dates:
        print("没有找到图片")
        return
    
    # 设置视频参数
    target_size = (1920, 1080)  # 1080p
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    
    # 创建视频写入器
    video_writer = None
    
    for image_path, creation_time in tqdm(images_with_dates, desc="生成视频"):
        # 读取图片
        try:
            img = Image.open(image_path)
            # 转换为RGB模式（处理RGBA图片）
            if img.mode == 'RGBA':
                img = img.convert('RGB')
            # 调整图片大小，保持比例
            img.thumbnail(target_size, Image.Resampling.LANCZOS)
            # 创建黑色背景
            background = Image.new('RGB', target_size, (0, 0, 0))
            # 将图片粘贴到中心
            offset = ((target_size[0] - img.size[0]) // 2,
                     (target_size[1] - img.size[1]) // 2)
            background.paste(img, offset)
            # 转换为OpenCV格式
            frame = cv2.cvtColor(np.array(background), cv2.COLOR_RGB2BGR)
            
            # 添加时间戳
            timestamp = creation_time.strftime('%Y-%m-%d %H:%M:%S')
            cv2.putText(frame, timestamp, (50, target_size[1] - 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
            
            # 初始化视频写入器（如果还没有）
            if video_writer is None:
                video_writer = cv2.VideoWriter(output_path, fourcc, fps, target_size)
            
            video_writer.write(frame)
            
        except Exception as e:
            print(f"\n处理图片 {image_path} 时出错: {str(e)}")
            continue
    
    if video_writer is not None:
        video_writer.release()

def merge_videos(video_paths, output_path):
    """合并多个视频文件为一个"""
    if not video_paths:
        print("没有视频文件可合并")
        return
    
    # 读取第一个视频以获取参数
    cap = cv2.VideoCapture(video_paths[0])
    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))
    cap.release()

    # 创建视频写入器
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    # 依次处理每个视频
    for video_path in tqdm(video_paths, desc="合并视频"):
        cap = cv2.VideoCapture(video_path)
        total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
        
        with tqdm(total=total_frames, desc=f"处理 {os.path.basename(video_path)}", leave=False) as pbar:
            while cap.isOpened():
                ret, frame = cap.read()
                if not ret:
                    break
                out.write(frame)
                pbar.update(1)
                
        cap.release()

    out.release()
    print(f"已生成汇总视频: {output_path}")

def main():
    # 源目录和输出文件
    source_dir = os.path.expanduser('~/.lolcommits')
    
    # 按年月组织图片
    images_by_date = organize_images_by_date(source_dir)
    
    # 存储所有生成的视频路径
    video_paths = []
    
    # 为每个月份创建视频
    for year_month, images in images_by_date.items():
        output_dir = 'output_videos'
        os.makedirs(output_dir, exist_ok=True)
        output_path = os.path.join(output_dir, f'photos_{year_month}.mp4')
        print(f"正在创建 {year_month} 的视频...")
        create_video(images, output_path)
        print(f"视频已保存到: {output_path}")
        video_paths.append(output_path)
    
    # 按时间顺序排序视频路径
    video_paths.sort()
    
    # 创建汇总视频
    if video_paths:
        final_output = os.path.join('output_videos', 'final_summary.mp4')
        print("正在创建汇总视频...")
        merge_videos(video_paths, final_output)

if __name__ == "__main__":
    main()
