<p align="center">
 <img src="https://img.shields.io/badge/Python-3.9%2B-red?style=for-the-badge&logo=python&logoColor=white">
  <img src="https://img.shields.io/badge/Platform-Termux%20%7C%20Linux%20%7C%20Windows-blue?style=for-the-badge&logo=linux&logoColor=white">
  <img src="https://img.shields.io/badge/License-MIT-red?style=for-the-badge">
  <img src="https://img.shields.io/badge/Maintained%3F-Yes-brightgreen?style=for-the-badge">
 <img width="1080" height="595" alt="image" src="https://github.com/user-attachments/assets/a45e58d6-b1c6-4070-9be1-df7cf19140e6" />
 <img width="1076" height="596" alt="image" src="https://github.com/user-attachments/assets/f267e031-b5b4-4672-8eb0-468c9f5944b1" />
</p>



# 🛡️ Termux Setup Tools
**Termux için gelişmiş otomatik kurulum altyapısı.**

---

## 🚀 Yeni Başlayanlar İçin Hızlı Kurulum
Termux'u ilk kez açtıysanız aşağıdaki komutları **sırasıyla** yapıştırın:

### 1. Adım: Git ve Python Kurulumu
```bash
pkg update -y && pkg upgrade -y
pkg install git python -y
git clone https://github.com/zarvoxx/termuxsetuptool.git
ls
cd termuxsetuptool
python setup.py
