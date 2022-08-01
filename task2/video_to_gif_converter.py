import os
import hashlib
from urllib import request
from moviepy.editor import VideoFileClip


def convert_video_to_gif(video_url: str) -> str:
    gif_media_path = './media/gifs'
    request.urlretrieve(video_url, 'video.mp4')
    video_file = VideoFileClip('video.mp4')

    gif_name = hashlib.sha256(video_url.encode('utf-8')).hexdigest()
    if os.path.exists(f'{gif_media_path}/{gif_name}.gif'):
        raise FileExistsError
    else:
        video_file.write_gif(f'{gif_media_path}/{gif_name}.gif')
        os.remove('video.mp4')
        return os.path.abspath(f'{gif_media_path}/{gif_name}.gif')


if __name__ == '__main__':
    url = 'https://v16-webapp.tiktok.com/1a769de2296d82d6cb9baca92659fdd9/62e88b82/video/tos/useast2a/tos-useast2a' \
          '-pve-0068/2431af3bd4814a1999c471b963a86817/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br' \
          '=6794&bt=3397&btag=80000&cs=0&ds=3&ft=eXd.6H-oMyq8ZVN3Kwe2NQhoyl7Gb&mime_type=video_mp4&qs=0&rc' \
          '=Omk6MzQzNmQ6aGU7ZTo6OEBpM3ZpZ2Q6ZnM6PDMzNzczM0A1Xy41YzBiNTIxLmBiNF5fYSNra2A2cjRnaWJgLS1kMTZzcw%3D%3D&l' \
          '=202208012027030101901901531B62FEF4 '
    print(convert_video_to_gif(url))
