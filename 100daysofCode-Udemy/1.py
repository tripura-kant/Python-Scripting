# print('Welcome 1.py')

from youtube_transcript_api import YouTubeTranscriptApi

# YouTube video URL
video_url = "https://www.youtube.com/watch?v=8fbhI1qVj0c"

# Get video ID from the URL
video_id = video_url.split("v=")[1]

# Get transcript
transcript = YouTubeTranscriptApi.get_transcript(video_id)

# Create a text file to save the transcript
output_file = "transcript.txt"

# Write the transcript to the text file
with open(output_file, "w") as f:
    for item in transcript:
        f.write(item["text"] + "\n")

print(f"Transcript saved to {output_file}")
