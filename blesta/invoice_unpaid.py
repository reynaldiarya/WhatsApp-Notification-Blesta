import config
import datetime
import requests
import template_message

urlinvoices = f"{config.url}/invoices/getList.json"
paramsinvoices = {
    "status": 'open'
}
responseinvoices = requests.get(urlinvoices, params=paramsinvoices, auth=(config.user, config.key))
if responseinvoices.status_code == 200:
    datainvoices = responseinvoices.json()
    responseinvoceslist = datainvoices.get('response', [])

    today = datetime.datetime.now().date()

    for invoice in responseinvoceslist:
        date_billed_str = invoice.get('date_billed')
        if date_billed_str:
            date_billed = datetime.datetime.strptime(date_billed_str, "%Y-%m-%d %H:%M:%S").date()
            if date_billed == today:
                urlcontact = f"{config.url}/contacts/getAll.json"
                paramscontact = {
                    "client_id": invoice.get('client_id')
                }
                responsecontact = requests.get(urlcontact, params=paramscontact, auth=(config.user, config.key))
                datacontact = responsecontact.json()
                responsecontactlist = datacontact.get('response', [])

                for contact in responsecontactlist:
                    urlcontactnumber = f"{config.url}/contacts/getNumbers.json"
                    paramscontactnumber = {
                        "contact_id": contact.get('id')
                    }
                    responsecontactnumber = requests.get(urlcontactnumber, params=paramscontactnumber, auth=(config.user, config.key))
                    datacontactnumber = responsecontactnumber.json()
                    responsecontactnumberlist = datacontactnumber.get('response', [])
                    for contactnumber in responsecontactnumberlist:
                        firstName = contact.get('first_name')
                        lastName = contact.get('last_name')
                        phonetemp = contactnumber.get('number').replace('+', '').replace('.', '').replace('-', '')
                        if phonetemp.startswith('0'):
                            phonetemp = '62' + phonetemp[1:]
                        elif phonetemp.startswith('8'):
                            phonetemp = '62' + phonetemp
                        phone = '+' + phonetemp
                        invoiceNumber = invoice.get('id_value')
                        if invoiceNumber == "":
                            invoiceNumber = invoice.get('id')
                        totaltemp = float(invoice.get('total'))
                        total = "{:,.0f}".format(totaltemp).replace(",", ".")
                        messageToSend = template_message.invoice_unpaid.format(firstName = firstName,lastName = lastName,phone = phone, invoiceNumber = invoiceNumber, duedate = str(invoice.get('date_due')), duetotal= total)
                        url = 'http://127.0.0.1:8080/api/send'
                        data = {'phone': phone, 'message': messageToSend}
                        sendMessage = requests.post(url, json = data)

                        print(sendMessage.text)

else:
    print("Gagal mendapatkan data:", responseinvoices.status_code)