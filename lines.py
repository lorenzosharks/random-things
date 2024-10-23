import tkinter as tk
from tkinter import filedialog
import cv2
import math
from PIL import Image, ImageTk

class LineDrawer:
    def __init__(self, master):
        self.master = master
        self.master.title("Line Drawer and Video Viewer")
        self.canvas = tk.Canvas(master, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.lines = []
        self.start_x = None
        self.start_y = None
        self.total_length = 0
        self.video_path = None
        self.frame_index = 0
        self.frames = []
        self.current_frame = None

        self.canvas.bind("<Button-1>", self.on_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_release)
        self.canvas.bind("<Button-3>", self.next_frame)  # Right-click for next frame
        self.canvas.bind("<Button-2>", self.prev_frame)  # Middle-click for previous frame

        # Create a menu
        self.menu = tk.Menu(master)
        master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open Video", command=self.open_video)

    def on_click(self, event):
        self.start_x = event.x
        self.start_y = event.y

    def on_drag(self, event):
        self.canvas.delete("temp_line")
        self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, tag="temp_line")

    def on_release(self, event):
        self.canvas.delete("temp_line")
        end_x = event.x
        end_y = event.y
        line = (self.start_x, self.start_y, end_x, end_y)
        self.lines.append(line)
        self.canvas.create_line(line)
        
        length = math.sqrt((end_x - self.start_x)**2 + (end_y - self.start_y)**2)
        self.total_length += length
        print(f"Line drawn: {line}, Length: {length:.2f}")
        print(f"Total length: {self.total_length:.2f}")

    def open_video(self):
        self.video_path = filedialog.askopenfilename(filetypes=[("MP4 files", "*.mp4")])
        if self.video_path:
            print(f"Video selected: {self.video_path}")
            self.load_video()

    def load_video(self):
        cap = cv2.VideoCapture(self.video_path)
        screen_height = self.master.winfo_screenheight()

        self.frames = []
        while True:
            ret, frame = cap.read()
            if not ret:
                break
            # Resize the frame to fit the screen height while maintaining aspect ratio
            h, w, _ = frame.shape
            scale_factor = screen_height / h
            frame_resized = cv2.resize(frame, (int(w * scale_factor), screen_height))
            self.frames.append(frame_resized)

        cap.release()
        self.show_frame(self.frame_index)

    def show_frame(self, index):
        if 0 <= index < len(self.frames):
            self.current_frame = self.frames[index]
            self.frame_index = index
            frame_rgb = cv2.cvtColor(self.current_frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)
            self.canvas.create_image(0, 0, anchor=tk.NW, image=imgtk)
            self.canvas.image = imgtk

    def next_frame(self, event=None):
        if self.frame_index + 1 < len(self.frames):
            self.show_frame(self.frame_index + 1)

    def prev_frame(self, event=None):
        if self.frame_index - 1 >= 0:
            self.show_frame(self.frame_index - 1)


    def clear_numbers(self, event=None):
        # Clear length text
        if self.length_text_id:
            self.canvas.delete(self.length_text_id)
            self.length_text_id = None
        # Optionally clear total length or other relevant information
        self.total_length = 0
        print("All length information cleared.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LineDrawer(root)
    root.mainloop()
