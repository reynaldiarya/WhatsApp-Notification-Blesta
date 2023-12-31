# Introduction
Original: https://github.com/Intprism-Technology/Whatsapp-WHMCS

## Changelog


## Features
- [OK] API Kirim Pesan ke Nomor
- [OK] Auto Response / BOT
- [OK] Blesta Billing Alert
    - Invoice Terbit
    - Invoice Paid
    - Invoice DueDate
    - Last Notification 1day Before Terminate

# Requirements
- NodeJS v18
- Python v3
- Pip Python

# Install
- Install NodeJS
    ```
    https://nodejs.org/en/download/
    ```
- Install Python3 PIP & dependency (Ubuntu)
    ```
    apt install python3-pip
    ```
- Clone repository and Install Library
    ```
    git clone https://github.com/reynaldiarya/WhatsApp-Notification-Blesta.git
    cd WhatsApp-Notification-Blesta
    npm install
    ```
- Konfigurasi API
    ```
    nano blesta/config.py
    ```
    edit baris berikut
    ```
    url = ''
    user = ''
    key = ''
    ```
- Konfigurasi template pesan notifikasi Blesta
    ```
    nano blesta/template_message.py
    ```
    template variabel
    ```
    # Nama Depan: {firstName}
    # Nama Belakang: {lastName}
    # Nomor HP: {phone}
    # Nomor Invoice: {invoiceNumber}
    # Due Date: {duedate}
    # Total Tagihan: {duetotal}

    invoice_unpaid = "Halo, *{firstName} {lastName}*"
    invoice_paid = "Halo, *{firstName} {lastName}*"
    invoice_duedate = "Halo, *{firstName} {lastName}*"
    invoice_comingTerminate = "Halo, *{firstName} {lastName}*"
    ```
- Login Whatsapp
    sebagai contoh, instalasi di path /var/www/WhatsApp-Notification-Blesta
    ```
    node /var/www/WhatsApp-Notification-Blesta/index.js
    ```
    - scan qr hingga muncul success pairing
    - exit program / CTRL + C
# Run Service
- Whatsapp BOT & API
    - edit cron
    ```
    @reboot sleep 5 && node /var/www/WhatsApp-Notification-Blesta/index.js &
    ```
    - jalankan service ulang
    ```
    node /var/www/WhatsApp-Notification-Blesta/index.js &
    ```
- Service Kirim Invoice Blesta Notifikasi (tiap hari, jam 8 pagi) dan notifikasi invoice paid & unpaid (tiap 5menit)
    ```
    */5 * * * * /usr/bin/python3 /var/www/WhatsApp-Notification-Blesta/blesta/invoice_paid.py
    */5 * * * * /usr/bin/python3 /var/www/WhatsApp-Notification-Blesta/blesta/invoice_unpaid.py
    0 8 * * * /usr/bin/python3 /var/www/WhatsApp-Notification-Blesta/blesta/invoice_duedate.py
    0 8 * * * /usr/bin/python3 /var/www/WhatsApp-Notification-Blesta/blesta/invoice_comingTerminate.py
    ```
# Endpoint
- API Endpoint
    ```
    <ip>:8080/api/send
    ```
    Type: POST

    Variable:
    ```
    phone (required)
    message (required)
    ```
