from moviepy.editor import *
from PIL import Image
from voiceProcessor import create_speech

def images_to_video(images: list[str], audios: list[str]):
    #clips = [
    #    VideoFileClip(img).set_duration(2) for img in images
    #]
    #clip = ImageClip(images[0], duration=3)
    clips = [ImageClip(m).set_audio(audios[i]).set_duration(audios[i].duration)
      for i, m in enumerate(images)]
    clips = [clips[i % 2] for i in range(100)]
    
    concat_clip = concatenate_videoclips(clips, method="compose")
    concat_clip.write_videofile("test.mp4", fps=30)
    #concat_clip = concatenate_videoclips(clips, method="compose")
    #concat_clip.write_videofile("tes.mp4", fps=1)

def resize_imgs(images: list[str], mwidth: int=1920, mheight: int=1080):
    new_images = []
    for i, img in enumerate(images):
        im = Image.open(img)
        ratio = min(mwidth/im.width, mheight/im.height)
        im = im.resize((int(im.width * ratio), int(im.height * ratio)))
        dst = f"imge{i}.png"
        im.save(dst)
        new_images.append(dst)
    return new_images

def add_white_background(images: list[str]):
    new_images = []
    for i, img in enumerate(images):
        im = Image.open(img)
        bg = Image.new('RGBA', (1920, 1080), (255, 255, 255, 255))
        offset = ((bg.width - im.width) // 2, (bg.height - im.height) // 2)
        bg.paste(im, offset)
        dst = f"imge{i}.png"
        bg.save(dst)
        new_images.append(dst)
    return new_images

class TtsVideo:
    default_transition = "../assets/transition/transition.mp4"
    def __init__(self, transition_clip):
        self.Tts_clips = []
        self.transition = transition_clip

class TtsClip:
    def __init__(self, image_clip, audio_clip):
        self.image = None
        self.audio = None


if __name__ == "__main__":
    #vid = VideoFileClip("26.mp4")
    #vid.write_videofile("new.mp4")
    pass

    
    
    
    