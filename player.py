import tkinter as tk
from tkinter import filedialog
import cv2
from PIL import Image, ImageTk

class VideoPlayer:
    def __init__(self, master):
        self.master = master
        self.master.title("MP4 Video Player")
        self.master.geometry("800x600")  # Initial window size
        
        self.canvas = tk.Canvas(master)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        self.video_path = None
        self.cap = None
        self.frame = None
        self.photo = None
        self.frame_width = 0
        self.frame_height = 0

        self.master.bind("<Configure>", self.resize_video)
        
        # Create a menu
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open Video", command=self.open_video)
        self.file_menu.add_command(label="Exit", command=master.quit)

    def open_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if self.video_path:
            print(f"Video selected: {self.video_path}")
            self.cap = cv2.VideoCapture(self.video_path)
            self.play_video()

    def play_video(self):
        if self.cap.isOpened():
            ret, frame = self.cap.read()
            if ret:
                self.frame = frame
                self.show_frame()
                self.master.after(10, self.play_video)  # Adjust the delay for video speed

    def resize_video(self, event=None):
        if self.frame is not None:
            screen_width = self.master.winfo_width()
            screen_height = self.master.winfo_height()
            self.frame_width = screen_width
            self.frame_height = screen_height
            self.show_frame()

    def show_frame(self):
        if self.frame is not None:
            # Resize frame maintaining aspect ratio
            frame = self.frame
            h, w, _ = frame.shape
            scale = min(self.frame_width / w, self.frame_height / h)

            # Ensure new dimensions are positive and non-zero
            new_w = max(1, int(w * scale))
            new_h = max(1, int(h * scale))

            frame_resized = cv2.resize(frame, (new_w, new_h))
            frame_rgb = cv2.cvtColor(frame_resized, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            self.photo = ImageTk.PhotoImage(image=img)
            self.canvas.create_image((self.frame_width - new_w) // 2, (self.frame_height - new_h) // 2, anchor=tk.NW, image=self.photo)

if __name__ == "__main__":
    root = tk.Tk()
    player = VideoPlayer(root)
    root.mainloop()
