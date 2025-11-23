# Mixture-of-Agents – Setup & Installation Guide

This repository contains a **Streamlit-based AI agent application** that sends your query to multiple LLMs through the **Hugging Face Inference Router**, then aggregates the responses into one final answer.

هذا الملف يشرح بالتفصيل كيفية تشغيل المشروع على أي جهاز، ويعالج الأخطاء الشائعة بالكامل.

---

# ✅ Requirements

## **1. Python Version (IMPORTANT)**

* المشروع **لا يعمل** على Python **3.13 أو 3.14**.
* **يجب** استخدام:

  * ✔ Python **3.11** (مُوصى به بقوة)
  * أو Python **3.10**

> **Note:** لو جهازك مثبت عليه Python 3.13 أو 3.14، لازم تثبت Python 3.11 قبل تشغيل المشروع.

Download Python 3.11 from:
[https://www.python.org/downloads/release/python-3119/](https://www.python.org/downloads/release/python-3119/)

---

## **2. Required Python Libraries**

يتم تثبيت جميع المكتبات عبر ملف `requirements.txt` الموجود في هذا المشروع.

تشمل أهم المكتبات:

* streamlit
* openai
* pandas
* pyarrow
* asyncio

---

## **3. Other Requirements**

* اتصال إنترنت جيد.
* **Hugging Face Access Token** (مطلوب لتشغيل النماذج).
  يمكن الحصول على التوكن عبر:
  [https://huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

---

# 🚀 Installation

## **Step 1 – Clone Repository**

```
git clone <repo-url>
cd mixture-of-agents
```

## **Step 2 – Create Virtual Environment**

```
py -3.11 -m venv venv
venv\Scripts\activate
```

## **Step 3 – Install Requirements**

```
pip install -r requirements.txt
```

---

# ▶️ Run the Application

```
streamlit run mixture-of-agents.py
```

سيظهر التطبيق على الرابط:

```
http://localhost:8501
```

---

# 📝 Usage Guide

1. أدخل **Hugging Face Access Token**.
2. اكتب السؤال.
3. اضغط **Get Answer**.
4. التطبيق سيقوم بـ:

   * إرسال السؤال لعدة نماذج.
   * جمع الردود.
   * عرض الإجابة النهائية.

---

# ⚠️ Common Errors & Fixes

## ❌ **1. Python 3.13 أو 3.14 Error**

```
Failed building wheel for pyarrow
No matching distribution for pandas
```

**الحل:** استخدم Python 3.11 فقط.

---

## ❌ **2. ModuleNotFoundError**

```
No module named streamlit
```

**الحل:**

```
pip install streamlit
```

---

## ❌ **3. Token Permission Error**

إذا ظهرت مشكلة في الموديلات:

* تأكد أن التوكن يحتوي على صلاحيات **read**.

---

# 📦 File Structure

```
mixture-of-agents/
│
├── mixture-of-agents.py
├── requirements.txt
├── README.md
└── venv/ (optional)
```

---

# 🌐 About This Project

This app demonstrates a simple **Mixture-of-Agents architecture** using:

* HuggingFace Inference Router
* Multiple LLM models
* Async requests
* Final response aggregation

---

# **🙋‍♂** Support

لو واجهت أي مشكلة:

* افتح Issue على GitHub
* أو تواصل معي مباشرة

Enjoy coding! 🚀
