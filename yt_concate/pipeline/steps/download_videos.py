from .step import Step

from pytube import YouTube
from yt_concate.settings import VIDEOS_DIR

class DownloadVideos(Step):
    def process(self, data, inputs, utils):

        yt_set = set([found.yt for found in data])
        print('videos to download', len(yt_set))

        for yt in yt_set:
            url = yt.url

            if utils.video_file_exist(yt):
                print(f'found existing video file for {url}, skipping')
                continue

            try:
                print('downloading', url)
                YouTube(url).streams.get_highest_resolution().download(output_path=VIDEOS_DIR, filename=yt.id + '.mp4')
            except:
                print(f'Downloading {url}  fail, skipping')
                continue

        return data
