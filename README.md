# 🏦 AI-Powered Furniture Arrangement (Reinforcement Learning)

This project uses **Reinforcement Learning (RL)** to **optimize furniture placement** in a room. The AI model is trained using **Stable-Baselines3 (PPO)** and deployed as an interactive **Streamlit web app**.

---

## 🚀 Live Demo

🔗 [**Try the App on Streamlit**](https://your-app.streamlit.app) (*Replace with your actual link*)

---

## 📌 Features

- ✅ AI **automatically arranges furniture** in a room
- ✅ Uses **Reinforcement Learning (PPO)** to **optimize placement**
- ✅ Avoids **overlapping furniture** using an RL reward system
- ✅ Supports **different room sizes & furniture counts**
- ✅ Interactive **Streamlit UI** for real-time testing

---

## 🤦️ Installation & Running Locally

### **1️⃣ Clone the Repository**

```bash
git clone https://github.com/YOUR_USERNAME/furniture_ai_rl.git
cd furniture_ai_rl
```

### **2️⃣ Install Dependencies**

```bash
pip install -r requirements.txt
```

### **3️⃣ Run the AI App**

```bash
streamlit run app.py
```

🛠 Open `` in your browser to interact with the AI! 🎉

---

## 📊 Training the RL Model (Optional)

If you want to **train the RL model yourself**, run:

```bash
python train_rl.py
```

This will train the AI for **200K+ steps** and save multiple models:

```
furniture_rl_model_2_items.zip
furniture_rl_model_3_items.zip
furniture_rl_model_4_items.zip
furniture_rl_model_5_items.zip
```

Each model corresponds to different furniture counts.

---

## 🖥 Tech Stack

- **Python 3.8+**
- **Stable-Baselines3 (PPO)**
- **Gymnasium**
- **Streamlit**
- **Matplotlib**
- **TensorFlow**

---

## 🚀 Deploying on Streamlit Cloud

You can make your AI **publicly available** by deploying it on **Streamlit Cloud**.

### **1️⃣ Push Your Code to GitHub**

Run the following commands:

```bash
git add .
git commit -m "Updated RL model training and deployment"
git push origin main
```

### **2️⃣ Deploy on Streamlit Cloud**

1. Go to [**Streamlit Cloud**](https://share.streamlit.io/)
2. Click **"New App"** → Select your GitHub repo
3. Set **Main file:** `app.py`
4. Click **"Deploy"** 🚀

🔗 **Your AI-powered furniture app is now public!** 🎉

---

## 🌟 License

This project is licensed under the **MIT License** – Free to use & modify!

---

## 🤝 Contributing

Want to improve the AI? Fork the repo & submit a pull request! 😊
