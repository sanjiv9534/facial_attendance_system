from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import os
from student import student
from train import Train
from face_recognition import Face_Recognition

class FaceRecognitionSystem:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1920x1080+0+0")
        self.root.title("Face Recognition System")

        # First image
        img = Image.open("college_images/images.jpeg")
        img = img.resize((650, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)

        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=650, height=130)

        # Second image
        img1 = Image.open("college_images/images3.jpeg")
        img1 = img1.resize((650, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)

        f_lbl1 = Label(self.root, image=self.photoimg1)
        f_lbl1.place(x=650, y=0, width=650, height=130)

        # Third image
        img2 = Image.open("college_images/images2.jpeg")
        img2 = img2.resize((650, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        f_lbl2 = Label(self.root, image=self.photoimg2)
        f_lbl2.place(x=1300, y=0, width=650, height=130)

        # Background image
        img3 = Image.open("college_images/pngtree-abstract-bg-image_914283.jpeg")
        img3 = img3.resize((1850, 1010), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)

        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=130, width=1850, height=1010)

        title_lbl = Label(bg_img, text="Face Recognition Attendance System ", font=("times new roman", 35, "bold"),
                          bg="white", fg="red")
        title_lbl.place(x=0, y=0, width=1920, height=45)

        # Student button
        img4 = Image.open("college_images/images (1).jpeg")
        img4 = img4.resize((220, 220), Image.ANTIALIAS)
        self.photoimg4 = ImageTk.PhotoImage(img4)

        b1 = Button(bg_img, image=self.photoimg4,command=self.student_details, cursor="hand2")
        b1.place(x=200, y=100, width=220, height=220)

        b1_1 = Button(bg_img, text="Students Details",command=self.student_details, cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b1_1.place(x=200, y=300, width=220, height=40)

        # Deduct face button
        img5 = Image.open("college_images/images6.jpeg")
        img5 = img5.resize((220, 220), Image.ANTIALIAS)
        self.photoimg5 = ImageTk.PhotoImage(img5)

        b2 = Button(bg_img, image=self.photoimg5, cursor="hand2",command=self.face_data)
        b2.place(x=500, y=100,width=220, height=220)

        b2_1 = Button(bg_img, text="Face Detector", cursor="hand2",command=self.face_data, font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b2_1.place(x=500, y=300, width=220, height=40)

        # Attendance face button
        img6 = Image.open("college_images/images.jpeg")
        img6 = img6.resize((220, 220), Image.ANTIALIAS)
        self.photoimg6 = ImageTk.PhotoImage(img6)

        b3 = Button(bg_img, image=self.photoimg6, cursor="hand2")
        b3.place(x=800, y=100,width=220, height=220)

        b3_1 = Button(bg_img, text="Attendance", cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b3_1.place(x=800, y=300, width=220, height=40)

        # Help desk face button
        img7 = Image.open("college_images/Untitled.jpeg")
        img7 = img7.resize((220,220), Image.ANTIALIAS)
        self.photoimg7 = ImageTk.PhotoImage(img7)

        b4 = Button(bg_img, image=self.photoimg7, cursor="hand2")
        b4.place(x=1100, y=100,width=220, height=220)

        b4_1 = Button(bg_img, text="Help Desk", cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b4_1.place(x=1100, y=300, width=220, height=40)

        # Train face button
        img8 = Image.open("college_images/images5.jpeg")
        img8 = img8.resize((220, 220), Image.ANTIALIAS)
        self.photoimg8 = ImageTk.PhotoImage(img8)

        b5 = Button(bg_img, image=self.photoimg8, cursor="hand2",command=self.train_data)
        b5.place(x=200, y=380, width=220, height=220)

        b5_1 = Button(bg_img, text="Train Data", cursor="hand2",command=self.train_data,font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b5_1.place(x=200, y=600, width=220, height=40)

        # Photo face button
        img9 = Image.open("college_images/Untitled2.jpeg")
        img9 = img9.resize((220, 220), Image.ANTIALIAS)
        self.photoimg9 = ImageTk.PhotoImage(img9)

        b6 = Button(bg_img, image=self.photoimg9, cursor="hand2")
        b6.place(x=500, y=380, width=220, height=220)

        b6_1 = Button(bg_img, text="Photos", cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b6_1.place(x=500, y=600, width=220, height=40)

        # Developer face button
        img10 = Image.open("college_images/Untitled1.png")
        img10 = img10.resize((220, 220), Image.ANTIALIAS)
        self.photoimg10 = ImageTk.PhotoImage(img10)

        b7 = Button(bg_img, image=self.photoimg10, cursor="hand2")
        b7.place(x=800, y=380, width=220, height=220)

        b7_1 = Button(bg_img, text="Developer", cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b7_1.place(x=800, y=600, width=220, height=40)

        # Exit button
        img11 = Image.open("college_images/images4.jpeg")
        img11 = img11.resize((220, 220), Image.ANTIALIAS)
        self.photoimg11 = ImageTk.PhotoImage(img11)

        b8 = Button(bg_img, image=self.photoimg11, cursor="hand2")
        b8.place(x=1100, y=380, width=220, height=220)

        b8_1 = Button(bg_img, text="EXIT", cursor="hand2", font=("times new roman", 20, "bold"),
                      bg="white", fg="red")
        b8_1.place(x=1100, y=600, width=220, height=40)
        
        
        #=====================================for photos button===============================================
        
        
        
        
    #=================================================function button====================================================================================
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=student(self.new_window)
        
    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)
        
    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognition(self.new_window)


if __name__ == "__main__":
    root = Tk()
    obj = FaceRecognitionSystem(root)
    root.mainloop()


