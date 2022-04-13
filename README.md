# Video Compressor
This is a personal tool I made to compress all my game recordings of which I have many (400+ GB worth of recordings). This tool also preserves audio tracks.

## Space Savings
This tool uses the incredibly efficient and now widely supported H265/HEVC codec to compress videos. Expect up to a 70% reduction in file size while still maintaining acceptable quality.

## How It Works
This tool utilizes FFMPEG to compress videos. It's a simple script that merely automates FFMPEG commands. It walks through every video file (mkv, mp4, mov, flv), compresses it, and deletes the uncompressed video file. It has basic error checking so it probably won't delete files willy-nilly. I haven't found the need to keep the uncompressed video files but if you would like that feature, just implement it and make a pull request.
