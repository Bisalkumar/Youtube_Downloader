import pytube
from tkinter import Tk, filedialog, simpledialog, messagebox
from datetime import datetime


def sanitize_filename(filename):
    """Remove or replace characters in filename that are invalid for file system."""
    invalid_chars = ['<', '>', ':', '"', '/', '\\', '|', '?', '*']
    for char in invalid_chars:
        filename = filename.replace(char, "_")
    return filename

def download_video(url, download_path):
    try:
        video = pytube.YouTube(url)
        stream = video.streams.filter(progressive=True, file_extension="mp4").first()

        # Generate unique filename using sanitized video title and current timestamp
        sanitized_title = sanitize_filename(video.title)
        filename = f"{sanitized_title}_{datetime.now().strftime('%Y%m%d%H%M%S')}.mp4"
        filepath = os.path.join(download_path, filename)

        stream.download(output_path=download_path, filename=filename)
        return True
    except Exception as e:
        print(f"An error occurred: {e}")
        return False


def main():
    root = Tk()
    root.withdraw()  # Hide the main window
    
    url = simpledialog.askstring("Input", "Paste the YouTube video URL:")
    if not url:
        return
    
    download_path = filedialog.askdirectory(title="Select Download Directory")
    if not download_path:
        return

    success = download_video(url, download_path)

    if success:
        messagebox.showinfo("Success", f"Video downloaded successfully to {download_path}")
    else:
        messagebox.showerror("Error", "Failed to download the video. Please check the URL or your connection.")

if __name__ == "__main__":
    main()
