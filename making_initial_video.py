from moviepy.editor import *
ImageSequenceClip
from PIL import Image
import os


image_folder_path=input("Enter the path of images folder: ")

#defining input directory that contains all the images and output file name
thumbnail_dir=os.path.join(image_folder_path, "output")
output_video=os.path.join(image_folder_path, "initial_video.mp4")


#adding path of all images file to the list
this_dir=os.listdir(thumbnail_dir)
filepaths=[os.path.join(thumbnail_dir, fname) for fname in this_dir
		if fname.endswith("jpg")] 

directory={}

for root, dirs, files in os.walk(thumbnail_dir):
	for fname in files:
		filepath=os.path.join(root, fname)

		try:
			key=float(fname.replace(".jpg", ""))
		except:
			key=None
		if key!=None:
			directory[key]=filepath

new_path=[]

for k in sorted(directory.keys()):
	filepath=directory[k]
	new_path.append(filepath)



clip=ImageSequenceClip(new_path, fps=1)
clip.write_videofile(output_video)

