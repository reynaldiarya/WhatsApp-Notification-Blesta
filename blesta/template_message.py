# Nama Depan: {firstName}
# Nama Belakang: {lastName}
# Nomor HP: {phone}
# Nomor Invoice: {invoiceNumber}
# Due Date: {duedate}
# Total Tagihan: {duetotal}

invoice_unpaid = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* sudah terbit.\n\nUntuk menghindari layanan ter-suspend, silahkan login ke portal https://my.hexahost.id dan lakukan pembayaran sesuai nominal *Rp{duetotal}* sebelum tanggal *{duedate}*.\n\nTerimakasih"
invoice_paid = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* sudah *LUNAS*, \n\nJika anda memerlukan bantuan teknis silahkan hubungi kami\n\nTerimakasih"
invoice_duedate = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* sudah terbit dan dalam waktu tenggang.\n\nUntuk menghindari layanan ter-suspend, silahkan login ke portal https://my.hexahost.id dan lakukan pembayaran sesuai nominal *Rp{duetotal}* maksimal tanggal *{duedate}*.\n\nTerimakasih"
invoice_comingTerminate = "Halo, *{firstName} {lastName}* kami informasikan invoice: *{invoiceNumber}* status belum terbayar.\n\nUntuk menghindari layanan terminate, silahkan login ke portal https://my.hexahost.id dan lakukan pembayaran sesuai nominal *Rp{duetotal}* maksimal tanggal *hari ini*.\n\nTerimakasih"