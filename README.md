# Mixture-of-Agents – Setup & Installation Guide

This repository contains a **Streamlit-based AI agent application** that sends your query to multiple LLMs through the **Hugging Face Inference Router**, then aggregates the responses into one final answer.

This README provides clear, structured instructions to help any user install, configure, and run the project smoothly.

---

# ✅ Requirements

## **1. Python Version (IMPORTANT)**

This project **does not work** on Python **3.13 or 3.14**.
You must use one of the supported versions:

* ✔ **Python 3.11** (strongly recommended)
* ✔ Python 3.10

> If your device already has Python 3.13 or 3.14 installed, you **must** download Python 3.11 to run this project.

Download Python 3.11:
[https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)

---

## **2. Required Python Libraries**

All dependencies are installed via the `requirements.txt` file.

Main libraries used:

* **streamlit** – Web UI framework
* **openai** – API client for HuggingFace Inference Router
* **pandas** – Data handling
* **pyarrow** – Required backend dependency
* **asyncio** – Async execution

---

## **3. Other Requirements**

* A stable internet connection
* Your **Hugging Face Access Token**

Create a token here:
[https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

# 🚀 Installation

## **Step 1 – Clone the Repository**

```
git clone <repo-url>
cd mixture-of-agents
```

## **Step 2 – Create a Virtual Environment**

```
py -3.11 -m venv venv
venv\Scripts\activate
```

## **Step 3 – Install Dependencies**

```
pip install -r requirements.txt
```

---

# ▶️ Running the Application

```
streamlit run mixture-of-agents.py
```

The app will open automatically at:

```
http://localhost:8501
```

---

# 📝 Usage Guide

1. Enter your **Hugging Face Access Token**.
2. Type your question in the input field.
3. Click **Get Answer**.
4. The system will:

   * Query multiple LLMs.
   * Collect individual responses.
   * Generate one final aggregated answer.

---

# ⚠️ Common Errors & Solutions

## ❌ **1. Python 3.13 or 3.14 Error**

```
Failed building wheel for pyarrow
No matching distribution for pandas
```

**Solution:** Install Python **3.11**.

---

## ❌ ModuleNotFoundError

```
No module named streamlit
```

**Solution:**

```
pip install streamlit
```

---

## ❌ Token Permission Error

If models fail to respond:

* Ensure your token has **read** permissions.

---

# 📦 Project Structure

```
mixture-of-agents/
│
├── mixture-of-agents.py
├── requirements.txt
├── README.md
└── venv/ (optional)
```

---

# 🌐 Project Overview

This application implements a simple **Mixture-of-Agents** workflow using:

* HuggingFace Inference Router
* Multiple LLM sources
* Asynchronous model requests
* A final aggregator model

---

# 🙋 Support

If you face issues:

* Open an Issue on GitHub
* Or contact me directly

Happy coding! 🚀
