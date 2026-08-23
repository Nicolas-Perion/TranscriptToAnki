import os
from config import TEMP_AUDIO_DIRECTORY_PATH, COOKIES_PATH, DENO_PATH
from yt_dlp import YoutubeDL
from yt_dlp.postprocessor import PostProcessor
import subprocess

temp_audio_directory = os.makedirs(name=TEMP_AUDIO_DIRECTORY_PATH, exist_ok=True)

ydl_opts = {
    "format": "m4a/ba",
    "postprocessors": [
        {
            "key": "FFmpegExtractAudio",
            "preferredcodec": "m4a",
        },
        {
            "key": "SponsorBlock",
            "categories": [
                "sponsor",
                "selfpromo",
                "preview",
                "interaction",
            ],  # For both 'categories' and 'remove_sponsor_segments',
            # the available segments are :
            # 'sponsor', 'intro', 'outro', 'selfpromo', 'preview',
            # 'filler', 'interaction', 'music_offtopic', 'hook',
            # 'poi_highlight', 'chapter' and 'all'
            "when": "after_filter",
        },
        {
            "key": "ModifyChapters",
            "remove_sponsor_segments": [
                "sponsor",
                "selfpromo",
                "preview",
                "interaction",
            ],
        },
        {"key": "FFmpegMetadata", "add_chapters": True},
    ],
    "cookiefile": COOKIES_PATH,
    "js_runtimes": {"deno": {"path": DENO_PATH}},
    # 'quiet': False,
    # 'verbose': True,
    "paths": {"home": TEMP_AUDIO_DIRECTORY_PATH},
    "outtmpl": "%(title)s [%(id)s].%(ext)s",  # Default structure of the name : 'title.ext'
}

final_info = {}


class CaptureFinalInfoPP(PostProcessor):
    def run(self, info):
        final_info.clear()
        final_info.update(info)
        return [], info


def download_split_by_chapters(
    url: str, chapters_to_exclude: list[str] = [], split: bool = True
) -> None:
    """
    Download the audio of separated chapters (if prompted so, and only kept chapters) from a video.

    Args:
        url (str): URL of the video.
        chapters_to_exclude (list[str], optional): Chapters to exlude. Defaults to an empty list.
        split (bool, optional): If the audio is split along chapters. Defaults to True.
    """

    if split == False and len(chapters_to_exclude) > 0:
        raise ValueError(
            "If no split will be performed, no chapters to exclude should be provided."
        )

    with YoutubeDL(ydl_opts) as ydl:
        ydl.add_post_processor(CaptureFinalInfoPP(), when="post_process")
        # info_dict = ydl.extract_info(url, download=True)
        ydl.extract_info(url, download=True)
        # info_dict = ydl.sanitize_info(info_dict, remove_private_keys=True)

        if (
            split == False
        ):  # If we don't want to split the audio, we just stop after downloading it.
            return

        all_chapters = final_info.get("chapters")
        final_filepath = final_info.get("filepath")

        if (
            all_chapters is None
        ):  # If we want to split but the audio has no chapters, we just stop after downloading it.
            return

        chapters_to_keep = [
            chap for chap in all_chapters if chap["title"] not in chapters_to_exclude
        ]  # The structure of all_chapters is list[dict[str, Any]

        for chap in chapters_to_keep:
            title = chap["title"]
            start_time = chap["start_time"]
            end_time = chap["end_time"]
            duration = end_time - start_time
            cmd = [
                "ffmpeg",
                "-y",
                "-i",
                final_filepath,
                "-ss",
                f"{start_time:.3f}",
                "-t",
                f"{duration:.3f}",
                "-c",
                "copy",
                f"temp_audio/{title}.m4a",
            ]

        if os.path.exists(final_filepath):
            os.remove(final_filepath)
