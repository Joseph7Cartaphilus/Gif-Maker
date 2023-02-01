import ffmpeg
import os


def video_to_gif():
    for file in os.listdir('your directory video'):
        if file.endswith(('.mp4', '.MP4')):
            file_name = file.split('.')[0]
            print(file_name)
            gif_file = file_name + '.gif'
            stream = ffmpeg.input(f'your directory/{file}')
            stream = ffmpeg.output(stream, f'your directory gif/{gif_file}')
            ffmpeg.run(stream)
        else:
            print('Bad extension in the file')


def main():
    video_to_gif()


if __name__ == '__main__':
    main()
