# Introduction
<<<<<<< HEAD
=======
## Changelog
- 30/03/2023 Update unpaid invoice from date to create date, so every invoice generate its will send to customer. important update !
- 06/08/2023 Add new ticket & reply ticket notification to whatsapp client

>>>>>>> 651f72c1c191cf9f40f85b089829f0a5f5707f25
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
    pip install mysql-connector-python
    ```
- Clone repository and Install Library
    ```
    git clone https://github.com/reynaldiarya/WhatsApp-Blesta.git
    cd WhatsApp-Blesta
    npm install
    npm update
    ```
- Konfigurasi DB MySQL
    ```
    nano blesta/config.py
    ```
    edit baris berikut
    ```
    host_db = ''
    name_db = ''
    user_db = ''
    pass_db = ''
    ```
- Konfigurasi template pesan notifikasi WHMCS
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
    # Tiket ID: {ticketID}
    # Tiket title: {ticketTitle}

    invoice_unpaid = "Halo, *{firstName} {lastName}*"
    invoice_paid = "Halo, *{firstName} {lastName}*"
    invoice_duedate = "Halo, *{firstName} {lastName}*"
    invoice_comingTerminate = "Halo, *{firstName} {lastName}*"
    new_ticket = "Halo, *{firstName} {lastName}*
    reply_ticket = "Halo, *{firstName} {lastName}*
    ```
- Login WhatsApp
    sebagai contoh, instalasi di path /WhatsApp-Blesta
    ```
    node WhatsApp-Blesta/index.js
    ```
    - scan qr hingga muncul success pairing
    - exit program / CTRL + C
# Run Service
- WhatsApp BOT & API
    - edit cron
    ```
    @reboot sleep 5 && node WhatsApp-Blesta/index.js &
    ```
    - jalankan service ulang 
    ```
    node WhatsApp-Blesta/index.js &
    ```
- Service Kirim Invoice WHMCS Notifikasi (tiap hari, jam 8 pagi) dan notifikasi invoice paid (tiap 5menit)
    ```
<<<<<<< HEAD
    */5 * * * * cd WhatsApp-Blesta/whmcs && python3 invoice_paid.py
    0 8 * * * cd WhatsApp-Blesta/whmcs && python3 invoice_unpaid.py
    0 8 * * * cd WhatsApp-Blesta/whmcs && python3 invoice_duedate.py
    0 8 * * * cd WhatsApp-Blesta/whmcs && python3 invoice_comingTerminate.py
=======
    */5 * * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_paid.py
    0 8 * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_unpaid.py
    0 8 * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_duedate.py
    0 8 * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 invoice_comingTerminate.py
    */5 * * * * cd /var/www/Whatsapp-WHMCS/whmcs && /usr/bin/python3 ticket.py
>>>>>>> 651f72c1c191cf9f40f85b089829f0a5f5707f25
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
# Request Update
Warga Diskusiwebhosting bisa request langsung melalui thread ))

    https://www.diskusiwebhosting.com/threads/WhatsApp-api-dan-notifikasi-whmcs.38061/


# Support Developer
- - - - - - - - - - - - - - - -
BCA : 3151176150

BCA Digital: 001339859866

Jago : 506512637291

Paypal: info@intprism.com
- - - - - - - - - - - - - - - -
