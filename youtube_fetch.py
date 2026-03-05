from googleapiclient.discovery import build

API_KEY = "AIzaSyDQjJ0WhYUyM4ooMwx84ELocQHhaF4tS1Q"

youtube = build("youtube", "v3", developerKey=API_KEY)


def search_youtube(topic, max_results=5):

    request = youtube.search().list(
        q=topic,
        part="snippet",
        type="video",
        maxResults=max_results
    )

    response = request.execute()

    videos = []

    for item in response["items"]:
        title = item["snippet"]["title"]
        video_id = item["id"]["videoId"]
        url = f"https://www.youtube.com/watch?v={video_id}"

        videos.append((title, url))

    return videos