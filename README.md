# 🎩 AI Furniture Arrangement App

This is a **Streamlit-based AI application** that predicts and visualizes **optimal furniture placements** in a room using a trained **TensorFlow model**.

## 🚀 Features
- 📏 **User Inputs:** Room dimensions and number of furniture items
- 🔮 **AI Predictions:** Uses a trained neural network to predict furniture placements
- 🎨 **Visualization:** Displays the predicted layout using `matplotlib`
- 🌐 **Deployed on Streamlit Cloud**: [Live App](https://furniture-arrangement.streamlit.app/)

---

## 🏗️ Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** TensorFlow/Keras for ML model
- **Data Processing:** NumPy
- **Visualization:** Matplotlib
- **Deployment:** Streamlit Cloud
- **Version Control:** Git & GitHub

---

## 📂 Project Structure
```
📁 furniture-arrangement-app
│── app.py                 # Streamlit app
│── train_model.py         # Training script
│── generate_layout.py     # Visualization logic
│── furniture_model.keras  # Trained ML model
│── requirements.txt       # Required dependencies
│── README.md              # Project documentation
│── images/                # Folder containing furniture images
```

---

## 📦 Installation
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/nandasantosh74/Furniture-arrangement-Project.git
cd Furniture-arrangement-Project
```

### 2️⃣ Install Dependencies
```sh
pip install -r requirements.txt
```

### 3️⃣ Run the Application Locally
```sh
streamlit run app.py
```

---

## 📡 Deploying on Streamlit Cloud
### 1️⃣ Push Code to GitHub
```sh
git add .
git commit -m "Added README.md"
git push origin main
```

### 2️⃣ Deploy on [Streamlit Cloud](https://share.streamlit.io/)
- Click **"New App"**
- Select your GitHub repository
- Set **Main file path** to `app.py`
- Click **Deploy** 🚀

### 3️⃣ Access the Deployed App
Your app is live at:  
[https://furniture-arrangement.streamlit.app/](https://furniture-arrangement.streamlit.app/)

---

## 🔧 Troubleshooting
### **1. Slow Performance?**
- Make sure you **use caching** (`@st.cache_resource`, `@st.cache_data`)
- Reduce the **model size** if possible

### **2. Streamlit Not Recognizing Model?**
- Ensure `furniture_model.keras` is in the **root directory**

### **3. Images Not Loading?**
- Make sure all images are inside an `images/` folder
- Ensure `generate_layout.py` is using the correct file paths

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## ⭐ Contribute
If you find this project useful, feel free to ⭐ star the repo and contribute!

---

**👨‍💻 Author:** Nanda Santosh  
**📌 GitHub:** [nandasantosh74](https://github.com/nandasantosh74)

