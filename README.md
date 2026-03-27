# 📸 Smart Attendance System 
### **AI-Powered Student Management via Computer Vision**
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)](https://opencv.org/)

---
The **Smart Attendance System** is an AI-powered platform designed to automate student attendance using **Facial Recognition**. 
The goal of the project is to provide a **seamless, fast, and paperless** way to manage student records in real-time.

This system was developed as my **Final Year Project (BSc IT)** to solve the problem of manual attendance taking in campus environments.

---

## 🚀 Features

* 🔍 **Real-time Detection:** Uses Haar Cascade Classifiers for instant face detection.
* 📸 **Automated Training:** Captures and processes 100+ photo samples per student.
* 🧠 **High Accuracy:** Implements the LBPH algorithm for reliable face matching.
* 🖥️ **Admin Dashboard:** A custom-built UI to manage student records and photo samples.
* 📊 **Data Export:** Automatically generates attendance logs in CSV format.

---

## 🛠️ Technologies Used

This project was built using:

* **Python 3.x** – Core programming logic
* **OpenCV** – Computer vision and image processing
* **Tkinter** – Desktop Graphical User Interface (GUI)
* **Pillow (PIL)** – Image handling and manipulation
* **SQLite / CSV** – Local data storage and logging

---

## 🔧 Technical Challenges & Solutions

### 1. Handling Lighting Variations
**Challenge:** Accuracy dropped significantly in low-light or overexposed campus environments.  
**Solution:** Implemented **Grayscale Conversion** and **Histogram Equalization** to normalize every frame before processing.

### 2. Processing Speed (FPS)
**Challenge:** High-resolution video frames caused lag on standard hardware.  
**Solution:** Optimized the script to **downscale frames** during the detection phase, maintaining a smooth 30+ FPS.

---

## 📂 Project Structure

FaceRecognitionSystem/
├── data/               # Trained XML data files
├── images/             # Collected student photo samples
├── main.py             # Main GUI application logic
├── train.py            # Dataset trainer script
├── attendance.csv      # Real-time attendance logs
└── README.md           # Project documentation


---

## ⚙️ Installation & Setup

To run this project locally:

1. Clone the repository
```bash
git clone [https://github.com/isaacmugwimi/FaceRecognitionSystem.git](https://github.com/isaacmugwimi/FaceRecognitionSystem.git)
Install dependencies

Bash
pip install opencv-python pillow
Start the application

Bash
python main.py
```
🎯 Purpose of the Project
The aim of the Smart Attendance System is to:

Replace manual attendance sheets with biometric automation.

Reduce human error and "proxy" attendance.

Provide real-time data for school administration.

Demonstrate the practical use of Computer Vision in education.

🤝 Contributing
Contributions are welcome.

If you would like to improve the recognition accuracy or UI:

Fork the repository

Create a new branch

Submit a pull request

👨‍💻 Author
Isaac Mugwimi

Full-Stack Developer & IT Graduate passionate about Computer Vision and automation.

GitHub:
https://github.com/isaacmugwimi

⭐ Support
If you find this project useful, consider starring the repository to support the project.
