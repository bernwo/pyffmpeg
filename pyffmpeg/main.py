# mymodule/main.py
from pathlib import Path
from shlex import split
from subprocess import run

CWD = Path.cwd()


def list_mp4_files():
    mp4_files = list(CWD.glob("*.mp4"))
    return mp4_files


def main():
    mp4_files = list_mp4_files()
    vcodec = "libx265"
    crf = 18
    preset = "veryslow"

    if len(mp4_files) > 0:
        output_dir = (CWD / "pyffmpeg_output").resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        for file in mp4_files:
            output_file = (output_dir / file.name).resolve()
            # command_str = f"ffmpeg -i {file.resolve().as_posix()} -vcodec {vcodec} -crf {crf} -preset {preset} {output_file.as_posix()}"
            # command_str = f"ffmpeg -i {file.resolve().as_posix()} -c:v hevc_videotoolbox -q:v 65 -tag:v hvc1 {output_file.as_posix()}"
            command_str = f"ffmpeg -i {file.resolve().as_posix()} -vcodec {vcodec} -crf {crf} -tag:v hvc1 -preset {preset} {output_file.as_posix()}"
            run(split(command_str))
