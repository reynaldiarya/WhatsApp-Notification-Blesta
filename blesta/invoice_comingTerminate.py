import config
import datetime
import requests
import template_message

urlinvoices = f"{config.url}/invoices/getList.json"
paramsinvoices = {
    "status": 'closed',
    "order_by[date_closed]": "DESC"
}
responseinvoices = requests.get(urlinvoices, params=paramsinvoices, auth=(config.user, config.key))
if responseinvoices.status_code == 200:
    datainvoices = responseinvoices.json()
    responseinvoceslist = datainvoices.get('response', [])

    urlcompanies = f"{config.url}/companies/getSetting.json"
    paramscompanies = {
        "company_id": 1,
        "key": 'cancel_service_changes_days'
    }
    responsecompaniessetting = requests.get(urlcompanies, params=paramscompanies, auth=(config.user, config.key))
    datacompaniessetting = responsecompaniessetting.json()
    responsecompaniessettinglist = datacompaniessetting.get('response', [])
    dayBeforeTerminate = 1

    today = datetime.datetime.now().date()
    terminateDate = today - datetime.timedelta(days = int(responsecompaniessettinglist['value'])-int(dayBeforeTerminate))
    for invoice in responseinvoceslist:
        due_date_str = invoice.get('date_due')
        if due_date_str:
            due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d %H:%M:%S").date()
            if due_date == terminateDate:
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
                        messageToSend = template_message.invoice_comingTerminate.format(firstName = firstName,lastName = lastName,phone = phone, invoiceNumber = invoiceNumber, duedate = str(invoice.get('date_due')), duetotal= total)
                        url = 'http://127.0.0.1:8080/api/send'
                        data = {'phone': phone, 'message': messageToSend}
                        sendMessage = requests.post(url, json = data)

                        print(sendMessage.text)

else:
    print("Gagal mendapatkan data:", responseinvoices.status_code)
# import config
# import requests
# import template_message
# from datetime import date
# from datetime import timedelta

# access = config.db.cursor()
# access.execute("SELECT value FROM tblconfiguration WHERE setting = 'AutoTerminationDays';")
# terminateConf = access.fetchall()
# dayBeforeTerminate = 1

# today = date.today()
# terminateDate = [today - timedelta(days = int(terminateConf[0][0])-int(dayBeforeTerminate))]

# access = config.db.cursor()
# access.execute("SELECT * FROM tblinvoices WHERE status = 'Unpaid' AND duedate = %s;",terminateDate)
# resultInvoice = access.fetchall()
# for x in resultInvoice:
#     sql = "SELECT * FROM tblclients WHERE id = %s"
#     access.execute(sql, (x[1],))
#     resultUser = access.fetchall()
#     for user in resultUser:
#         firstName = user[2]
#         lastName = user[3]
#         phone = user[12].replace('.', '').replace('-', '')
#         invoiceNumber = x[2]
#         if invoiceNumber == "":
#             invoiceNumber = x[0]
#         messageToSend = template_message.invoice_duedate.format(firstName = firstName,lastName = lastName,phone = phone, invoiceNumber = invoiceNumber, duedate = str(x[4]), duetotal= x[13])
#         url = 'http://127.0.0.1:8080/api/send'
#         data = {'phone': phone, 'message': messageToSend}
#         sendMessage = requests.post(url, json = data)

#         print(sendMessage.text)
