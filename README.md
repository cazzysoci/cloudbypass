```bash
git clone https://github.com/cazzysoci/cloudbypass.git
cd cloudbypass
```

###  Create a Virtual Environment (Recommended)  

Creating a virtual environment is recommended to isolate project dependencies:  

```bash
python3 -m venv venv
```

Activate the virtual environment:  

- **Linux/macOS:**  

  ```bash
  source venv/bin/activate
  ```

- **Windows:**  

  ```bash
  .\venv\Scripts\activate
  ```

###  Install Dependencies  

Use `pip` to install the required dependencies:  

```bash
pip install -r requirements.txt
```
###  Run the Tool  

Once installation is complete, run the tool using:  

```bash
python3 cloudbypass.py
```

---

## 📌 OS-Specific Installation  

### **🖥 Windows**  

- Ensure **Python** is added to **PATH** during installation.  
- **Install Nmap (Optional):** If you want to use the **Port Scanning** feature, install [Nmap](https://nmap.org/download.html) and add its installation directory to **PATH**.  
- Run the terminal as **Administrator** if needed.  
- Update `pip` if necessary:  

  ```bash
  python -m pip install --upgrade pip
  ```

### **🐧 Linux**  

- Install **Nmap** using the following command:  

  ```bash
  sudo apt update && sudo apt install nmap  # Debian/Ubuntu
  sudo yum install nmap  # Fedora/CentOS/RHEL
  ```

- Run with root privileges if required:  

  ```bash
  sudo python3 cloudbypass.py
  ```

### **🍎 macOS**  

- Install **Homebrew** if not already installed:  

  ```bash
  /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
  ```

- Install **Nmap** using Homebrew:  

  ```bash
  brew install nmap
  ```

### **📱 Termux (Android)**  

- Install **Termux** from Google Play Store or F-Droid.  
- Update packages:  

  ```bash
  pkg update
  ```

- Install **Python** and **Git**:  

  ```bash
  pkg install python git
  ```

- Install **Nmap**:  

  ```bash
  pkg install nmap
  ```

---

## 📖 Usage  

1. Run the tool and select an option from the main menu.  
2. Some features require a domain or target IP address.  
3. Follow the on-screen instructions to input the necessary information.  

---

## ⚠️ Disclaimer  

- **This tool is for educational and testing purposes only.**  
- **Use it only on systems you have explicit permission to test.**  
- **Misuse of this tool may lead to legal consequences.**  
