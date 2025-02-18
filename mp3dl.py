import os
import subprocess
import sys
from yt_dlp import YoutubeDL

def search_youtube(song_name):
    """Search YouTube for the song and return the first result URL."""
    ydl_opts = {
        'writethumbnail': True,   
        'quiet': True,  # Allow detailed logs
        'default_search': 'ytsearch5',  # Search for more results
        'extract_flat': True,
    }
    with YoutubeDL(ydl_opts) as ydl:
        try:
            info = ydl.extract_info(f"ytsearch5:{song_name}", download=False)
            #print("DEBUG: Full yt-dlp response:", info)  # Show full response

            if 'entries' in info and info['entries']:
                return info['entries'][0]['url']  # Get the first result
            else:
                print("No results found. Try a different song name.")
                sys.exit(1)

        except Exception as e:
            print("ERROR: ", e)
            sys.exit(1)
            
def download_mp3(youtube_url, song_name):
    """Download the YouTube video as an MP3."""
    ydl_opts = {    
        'writethumnbail': True,       
        'format': 'bestaudio/best',
                'postprocessors': [
                    {'key': 'FFmpegExtractAudio','preferredcodec': 'mp3','preferredquality': '192'},
                    {'key': 'EmbedThumbnail'},
                    ],
        'ffmpeg_location': '/usr/bin/ffmpeg',
        'outtmpl': f"{song_name}.%(ext)s",
    }
    with YoutubeDL(ydl_opts) as ydl:
        ydl.download([youtube_url])

def main():
    song_name = input("Enter the song name: ")
    print("Searching for song...")
    youtube_url = search_youtube(song_name)
    print(f"Found: {youtube_url}")
    print("Downloading...")
    download_mp3(youtube_url, song_name)
    print("Download complete!")

if __name__ == "__main__":
    main()
