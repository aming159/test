from moviepy.editor import VideoFileClip,vfx
print("successful!")

# 加载视频文件
video = VideoFileClip('rt2_videos_compressed.mp4')

# 将视频速度加快16倍
video_speedx16 = video.fx(vfx.speedx, 4)

# 输出加速后的视频
video_speedx16.write_videofile('4x_rt2.mp4')
print("successful!")
