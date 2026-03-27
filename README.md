# 📸 Smart Attendance System 
### **AI-Powered Student Management via Computer Vision**
[![Python](https://img.shields.io/badge/Python-3.x-blue?style=for-the-badge&logo=python)](https://www.python.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-Computer%20Vision-green?style=for-the-badge&logo=opencv)](https://opencv.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

---

## 📌 Project Overview
The **Smart Attendance System** is my **Final Year Campus Project (BSc IT)**. It is a desktop application designed to automate student attendance using **Facial Recognition**. By identifying students in real-time through a camera feed, the system eliminates manual paperwork and logs presence instantly into a secure database.

---

## 🚀 Key Features
* **🔍 Real-time Detection:** Uses **Haar Cascade Classifiers** for instant face detection.
* **📸 Automated Training:** Captures 100+ photo samples per student to build a robust local dataset.
* **🧠 High Accuracy:** Implements the **LBPH (Local Binary Patterns Histograms)** algorithm for reliable face matching.
* **🖥️ Admin Dashboard:** A custom-built **Tkinter GUI** to manage student records and photo samples.
* **📊 Data Export:** Automatically generates attendance logs with timestamps in **CSV/Excel** format.

---

## 🔧 Technical Challenges & Solutions

### 1. Handling Lighting Variations
**Challenge:** Accuracy dropped in low-light or overexposed campus environments.  
**Solution:** Applied **Grayscale Conversion** and **Histogram Equalization** to normalize every frame before the recognition phase.

### 2. Processing Speed (FPS)
**Challenge:** High-resolution frames caused lag on standard hardware.  
**Solution:** Optimized the script to **downscale** frames during the detection phase and upscale only for final display, maintaining a smooth 30+ FPS.

---

## 🛠 Tech Stack
| Component | Technology |
| :--- | :--- |
| **Language** | Python 3.x |
| **Computer Vision** | OpenCV (`cv2`) |
| **GUI Framework** | Tkinter |
| **Image Processing** | Pillow (PIL) |
| **Database** | SQLite / CSV |

---

## 📂 Project Structure
```text
FaceRecognitionSystem/
├── data/               # Trained XML data files
├── images/             # Collected student photo samples
├── main.py             # Main GUI application
├── train.py            # Dataset trainer script
└── attendance.csv      # Real-time attendance logs

```

📦 Quick Start
Clone the repo:

Bash
git clone [https://github.com/isaacmugwimi/FaceRecognitionSystem.git](https://github.com/isaacmugwimi/FaceRecognitionSystem.git)
Install requirements:

Bash
pip install opencv-python pillow
Run the Application:

Bash
python main.py
👨‍💻 Author
Isaac Mugwimi Full-Stack Developer & BSc IT Graduate LinkedIn | GitHub

⭐ If you find this project useful, feel free to star the repository!
