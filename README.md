# IpTracer
IpTreacer is a **Django-based** web application that allows you to track and analyze IP addresses using public geolocation and network analysis APIs. The application is designed to provide detailed information about the approximate location and technical characteristics of an IP address, facilitating monitoring, auditing, cybersecurity, and traffic analysis.

Through a simple interface, users can query IP addresses and obtain data such as:

- *Country, region, and city*
- *Internet Service Provider (ISP)*
- *Connection type*
- *Approximate geographic coordinates*
- *Network information relevant to technical analysis*

IpTreacer integrates multiple public APIs to improve the reliability of the results and is intended as an educational and support tool for developers, system administrators, and cybersecurity professionals.

```
⚠️ Note: The information provided depends on the public APIs used and may not be 100% accurate. The application does not perform physical tracking or invade user privacy.
```

## ⚙️ Installation

Follow the steps below to install and run **IpTreacer** in your local environment.

### 1️⃣ Prerequisites

Make sure you have the following installed:

* **Python 3.9+**
* **pip**
* **Git**
* (Optional) **Virtualenv**

Check versions:

```bash
python --version
pip --version
```


### 2️⃣ Clone the repository

```bash
git clone https://github.com/your-username/IpTreacer.git
cd IpTreacer
```


### 3️⃣ Create and activate a virtual environment (recommended)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```


### 4️⃣ Install dependencies

```bash
pip install -r requirements.txt
```


### 5️⃣ Configure environment variables

Create a **.env** file in the project root:

```env
SECRET_KEY=your_secret_key
DEBUG=True
```

> Some public APIs don't require a key, but if any API used in the project does, add it here.



### 6️⃣ Apply migrations

```bash
python manage.py migrate
```


### 7️⃣ Create superuser (optional)

```bash
python manage.py createsuperuser
```


### 8️⃣ Run the server

```bash
python manage.py runserver
```

Open your browser to:

```
http://127.0.0.1:8000
```


## ✅ Verification

Enter a valid IP address in the interface and verify that the data is displayed correctly.

---

## 🛑 Troubleshooting

* Ensure the virtual environment is active.

* Verify your internet connection (external APIs are required).
* Check for errors in the console or in `settings.py`.
