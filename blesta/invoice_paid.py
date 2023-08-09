import config
import datetime
import requests
import template_message

currentDate = datetime.datetime.now()
currentDate = currentDate.year

access = config.db.cursor()
access.execute("SELECT * FROM invoices WHERE paid != 0 AND date_closed >= date_sub(now(), interval 5 minute)")
resultInvoice = access.fetchall()
for x in resultInvoice:
    sql = "SELECT * FROM contacts WHERE client_id = %s"
    access.execute(sql, (x[3],))
    resultUser = access.fetchall()
    for user in resultUser:
        firstName = user[5]
        lastName = user[6]
        sql2 = "SELECT * FROM contact_numbers WHERE contact_id = %s"
        access.execute(sql2, (user[1],))
        resultContact = access.fetchall()
        for contact in resultContact:
            phonetemp = contact[2].replace('.', '').replace('-', '')
            if phonetemp.startswith('0'):
                phonetemp = '62' + phonetemp[1:]
            elif phonetemp.startswith('8'):
                phonetemp = '62' + phonetemp
            phone = '+' + phonetemp
            invoiceNumber = x[2]
            if invoiceNumber == "":
                invoiceNumber = x[0]
            messageToSend = template_message.invoice_paid.format(firstName = firstName,lastName = lastName,phone = phone, invoiceNumber = invoiceNumber, duedate = str(x[4]), duetotal= x[13])
            url = 'http://127.0.0.1:8080/api/send'
            data = {'phone': phone, 'message': messageToSend}
            sendMessage = requests.post(url, json = data)

            print(sendMessage.text)