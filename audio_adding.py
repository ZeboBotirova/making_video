import os
from moviepy.editor import AudioFileClip, VideoFileClip



org_video_path = input("Enter the video path: ")
audio_path = input("Enter the audio path: ")
final_video_path = input("Enter the output folder path: ")
final_video_name = input("Enter the changed video name with extension: ")
start_dur = int(input("Enter the starting duration in seconds: "))
end_dur = int(input("Enter the ending duration in seconds: "))


final_video_path = os.path.join(final_video_path, final_video_name)

video_clip = VideoFileClip(org_video_path)


background_audio_clip = AudioFileClip(audio_path)
bg_music = background_audio_clip.subclip(start_dur, end_dur)

final_clip = video_clip.set_audio(bg_music)

final_clip.write_videofile(final_video_path, codec='libx264', audio_codec="aac")