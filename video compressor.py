import logging
import os
import shlex
import subprocess

logging.basicConfig(filename='output.log', level=logging.DEBUG)

VIDEO_EXTENSIONS = ['mp4', 'mkv', 'mov', 'flv']
FILENAME_PLACEHOLDER = 'vFileName'
H264_FFMPEG_CMD = f'ffmpeg -c:v h264_cuvid -i "{FILENAME_PLACEHOLDER}" -c:v hevc_nvenc -c:a copy -map 0 -tag:v hvc1 "{FILENAME_PLACEHOLDER} (compressed).mp4"'
H265_FFMPEG_CMD = f'ffmpeg -c:v hevc_cuvid -i "{FILENAME_PLACEHOLDER}" -c:v hevc_nvenc -c:a copy -map 0 -tag:v hvc1 "{FILENAME_PLACEHOLDER} (compressed).mp4"'

while True:
    try:
        op_mode = int(input(
        '''
        Please select an option:
        1. Compress all videos
        2. Compress all videos but ignore videos with "compressed" tag
        3. Recompress all videos with "compressed" tag
        '''
        ))
    except ValueError:
        continue
    if op_mode > 3:
        continue
    break

def call_ffmpeg(ffmpeg_cmd, dirpath, filename):
    try:
        subprocess.run(shlex.split(ffmpeg_cmd.replace(FILENAME_PLACEHOLDER, os.path.join(dirpath, filename))), check=True, capture_output=True)
        os.remove(os.path.join(dirpath, filename))
    except subprocess.CalledProcessError as e:
        print('FFMPEG ended with a non-zero error code. Problematic video has been logged.')
        logging.debug(f'INPUT COMMAND: {e.cmd}')
        logging.critical(f'STDERR: {e.stderr}')
        logging.info('\n\n\n-----------SEPERATOR-----------\n\n\n')
        os.remove(os.path.join(dirpath, filename + ' (compressed).mp4'))

for dirpath, dirnames, filenames in os.walk(os.getcwd()):
    for filename in filenames:
        if any(extension in filename.split('.')[-1] for extension in VIDEO_EXTENSIONS):
            if 'compressed' in filename:
                if op_mode == 2:
                    continue
                call_ffmpeg(H265_FFMPEG_CMD, dirpath, filename)          
            else:
                if op_mode == 3:
                    continue
                call_ffmpeg(H264_FFMPEG_CMD, dirpath, filename) 
