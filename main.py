# This is a sample Python script.

import ffmpeg
def get_video(video_file_path):
    {
        """ 
        Read in video data into an FFMPeg object
        input:
        (string) video file path
        output:
        (ffmpeg object) ffmpeg video object
        """
    }

def display_video_metadata(video):
    {
        """
        Extract and print the video file data in a pretty format for inspection
        input:
        (ffmpeg object) video object
        output:
        none
        """
    }

def video_metadata_to_dict(video):
    {
        """
        Extract video metadata from a video file and output to a python dict
        input:
        (ffmpeg object) video object
        output: 
        (dict) metadata dictionary of provided file
        """
    }

def dict_to_video_metadata(vid_metadata):
    {
        """
        Receives a dict and inserts it back in the video object
        input:
        (dict) video metadata dictionary to insert into video
        output:
        (ffmpeg object) video object with new metadata
        """
    }





# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
