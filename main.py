from download_audio import download_split_by_chapters
from config import URL
# from transcript import write_transcriptions

download_split_by_chapters(URL, chapters_to_exclude=["Ad"], split=True)
# write_transcriptions()