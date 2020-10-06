import telebot

flybot = telebot.TeleBot("1144307188:AAG2GrlSnZy0hKf7Sx9sCK_sEY9FRgoEzwc")

@flybot.message_handler(commands=['Start','start'])
def send_welcome(message):
    chatid = message.chat.id
    usuario = message.chat.first_name + " " + message.chat.last_name + "\nEspero que se encuentre bien." + "\nSoy Fly bot,¿Como le puedo ayudar?"
    saludo = "Hola {nombre}"
    flybot.send_message(chatid,saludo.format(nombre=usuario))

@flybot.message_handler(commands=['Help', 'help'])
def handle_start_help(message):
    chatid = message.chat.id
    flybot.send_message(chatid,"Escriba"+"\nMenu - menu---- Funcionalidades disponibles.")

@flybot.message_handler(func=lambda message: message.text=='Hola' or message.text=='hola' or message.text=='HOLA')
def send_text_hola(message):
    chatid = message.chat.id
    usuario = message.chat.first_name + " " + message.chat.last_name + "\nEspero que se encuentre bien." + "\nSoy Fly bot,¿Como le puedo ayudar?"
    saludo = "Hola {nombre}"
    flybot.send_message(chatid,saludo.format(nombre=usuario))

@flybot.message_handler(func=lambda message: message.text=='Menu' or message.text=='menu' or message.text=='MENU')
def command_text_menu(message):
    chatid = message.chat.id
    flybot.send_message(chatid,"\nListar -> Lista los proximos vuelos disponibles."+"\nBuscar -> Busca vuelo especifico."+"\nComprar -> Compra un vuelo disponible.")
    #Listar,Buscar,Comprar

@flybot.message_handler(func=lambda message: message.text=='Listar' or message.text=='listar' or message.text=='LISTAR')
def command_text_listar(message):
    chatid=message.chat.id
    flybot.send_message(chatid,"----Vuelos Disponibles---- "
    "\nBRASIL - CUBA" + "\nESPAÑA - FRANCIA" + "\nCANADA - COLOMBIA"
    "\nIRLANDA - SUIZA" + "\nECUADOR - PANAMA" + "\nMARRUECOS - UCRANIA"
    "\nGRAN BRETAÑA - RUSIA" + "\nPERU - POLONIA" + "\nHONDURAS - CHILE"
    "\nPORTUGAL - JAPON" + "\nESTADOS UNIDOS - MEXICO" + "\nITALIA - HOLANDA"
    "\nCUBA - ESTADOS UNIDOS" + "\nCANADA - CHILE" + "\nSUIZA - PERU"
    "\nMARRUECOS - HOLANDA" + "\nUCRANIA - RUSIA" + "\nECUADOR - HONDURAS"
    "\nCOLOMBIA - JAPON" + "\nESPAÑA - ITALIA" + "\nCHILE - PERU"
    "\nJAPON - CHILE" + "\nSUIZA - PANAMA" + "\nESPAÑA - ECUADOR"
    "\nINDIA - CHILE" + "\nESPAÑA - JAPON" + "\nECUADOR - INDIA"
    "\nIRLANDA - PANAMA" + "\nHONDURAS - INDIA" + "\nCANADA - FRANCIA")

@flybot.message_handler(func=lambda message: message.text=='Buscar' or message.text=='buscar' or message.text=='BUSCAR')
def command_text_buscar(message):
    chatid = message.chat.id
    flybot.send_message(chatid,'Ingrese caracteres en mayuscula'+'\nIngrese Salida y Destino:'+'\n Salida-Destino'+'\n Ejemplo: ECUADOR-COLOMBIA')
    salida1 = flybot.send_message(chatid,'Ingrese vuelo: ')
    flybot.register_next_step_handler(salida1,step_Set_registro)
def step_Set_registro(message):
    chatid = message.chat.id
    registro = message.text
    if message.text == "BRASIL-CUBA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ESPAÑA-FRANCIA":
        flybot.send_message(chatid,"Vuelo disponible")
    elif message.text == "CANADA-COLOMBIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "IRLANDA-SUIZA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ECUADOR-PANAMA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "MARRUECOS-UCRANIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "GRAN BRETAÑA-RUSIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "PERU-POLONIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "HONDURAS-CHILE":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "PORTUGAL-JAPON":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ESTADOS UNIDOS-MEXICO":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ITALIA-HOLANDA" :
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "CUBA-ESTADOS UNIDOS":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "CANADA-CHILE":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "SUIZA-PERU":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "MARRUECOS-HOLANDA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "UCRANIA-RUSIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ECUADOR-HONDURAS":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "COLOMBIA-JAPON":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ESPAÑA-ITALIA" :
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "CHILE-PERU":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "JAPON-CHILE":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text ==  "SUIZA-PANAMA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text ==  "ESPAÑA-ECUADOR":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "INDIA-CHILE":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ESPAÑA-JAPON":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "ECUADOR-INDIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "IRLANDA-PANAMA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text == "HONDURAS-INDIA":
        flybot.send_message(chatid, "Vuelo disponible")
    elif message.text ==  "CANADA-FRANCIA":
        flybot.send_message(chatid, "Vuelo disponible")
    else:
        flybot.send_message(chatid,'Vuelo no existente o No disponible')

@flybot.message_handler(func=lambda message: message.text=='Comprar' or message.text=='comprar' or message.text=='COMPRAR')
def command_text_comprar(message):
    chatid = message.chat.id
    flybot.send_message(chatid,'Ingrese caracteres en mayuscula' + '\nIngrese Salida y Destino:' + '\n Salida-Destino' + '\n Ejemplo: ECUADOR-COLOMBIA')
    salida1 = flybot.send_message(chatid, 'Ingrese vuelo: ')
    flybot.register_next_step_handler(salida1, step_Set_vuelo)
def step_Set_vuelo(message):
    chatid = message.chat.id
    registro = message.text
    if message.text == "BRASIL-CUBA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------"+"\nNombre: {nombre}" + "\nSalida: BRASIL \nDestino: CUBA" + "\nGate: 001" + "\nCodigo: BR/CU/001"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ESPAÑA-FRANCIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ESPAÑA \nDestino: FRANCIA" + "\nGate: 002" + "\nCodigo:ES/FR/002 "
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "CANADA-COLOMBIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: CANADA \nDestino: COLOMBIA" + "\nGate: 003" + "\nCodigo: CA/CO/003"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "IRLANDA-SUIZA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: IRLANDA \nDestino: SUIZA" + "\nGate: 004" + "\nCodigo: IE/CH/004"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ECUADOR-PANAMA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ECUADOR \nDestino: PANAMA" + "\nGate: 005" + "\nCodigo: EC/PA/005"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "MARRUECOS-UCRANIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: MARRUECOS \nDestino: UCRANIA" + "\nGate: 006" + "\nCodigo: MA/UA/006"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "GRAN BRETAÑA-RUSIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: GRAN BRETAÑA \nDestino: RUSIA" + "\nGate: 001" + "\nCodigo: GB/RU/001"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "PERU-POLONIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: PERU \nDestino: POLONIA" + "\nGate: 002" + "\nCodigo: PE/PL/002"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "HONDURAS-CHILE":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: HONDURAS \nDestino: CHILE" + "\nGate: 003" + "\nCodigo: HN/CL/003"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "PORTUGAL-JAPON":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: PORTUGAL \nDestino: JAPON" + "\nGate: 004" + "\nCodigo:PT/JP/004"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ESTADOS UNIDOS-MEXICO":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ESTADOS UNIDOS \nDestino: MEXICO" + "\nGate: 005" + "\nCodigo: US/MX/005"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ITALIA-HOLANDA" :
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ITALIA \nDestino: HOLANDA" + "\nGate: 006" + "\nCodigo: IT/NL/006"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "CUBA-ESTADOS UNIDOS":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: CUBA \nDestino: ESTADOS UNIDOS" + "\nGate: 001" + "\nCodigo: CU/US/001"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "CANADA-CHILE":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: CANADA \nDestino: CHILE" + "\nGate: 002" + "\nCodigo: CA/CL/002"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "SUIZA-PERU":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: SUIZA \nDestino: PERU" + "\nGate: 003" + "\nCodigo: CH/PE/003"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "MARRUECOS-HOLANDA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: MARRUECOS \nDestino: HOLANDA" + "\nGate: 004" + "\nCodigo: MA/NL/004"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "UCRANIA-RUSIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: UCRANIA \nDestino: RUSIA" + "\nGate: 005" + "\nCodigo: UA/RU/005"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ECUADOR-HONDURAS":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ECUADOR \nDestino: HONDURAS" + "\nGate: 006" + "\nCodigo: EC/HN/006"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "COLOMBIA-JAPON":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: COLOMBIA \nDestino: JAPON" + "\nGate: 001" + "\nCodigo: CO/JP/001"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ESPAÑA-ITALIA" :
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ESPAÑA \nDestino: ITALIA" + "\nGate: 002" + "\nCodigo: ES/IT/002"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "CHILE-PERU":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: CHILE \nDestino: PERU" + "\nGate: 003" + "\nCodigo: CL/PE/003"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "JAPON-CHILE":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: JAPON \nDestino: CHILE" + "\nGate: 004" + "\nCodigo: JP/CL/004"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text ==  "SUIZA-PANAMA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: SUIZA \nDestino: PANAMA" + "\nGate: 005" + "\nCodigo: CH/PA/005"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text ==  "ESPAÑA-ECUADOR":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ESPAÑA \nDestino: ECUADOR" + "\nGate: 006" + "\nCodigo: ES/EC/006"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "INDIA-CHILE":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: INDIA \nDestino: CHILE" + "\nGate: 001" + "\nCodigo: IN/CL/001"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ESPAÑA-JAPON":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ESPAÑA \nDestino: JAPON" + "\nGate: 002" + "\nCodigo: ES/JP/002"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "ECUADOR-INDIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: ECUADOR \nDestino: INDIA" + "\nGate: 003" + "\nCodigo: EC/IN/003"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "IRLANDA-PANAMA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: IRLANDA \nDestino: PANAMA" + "\nGate: 004" + "\nCodigo: IE/PA/004"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text == "HONDURAS-INDIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: HONDURAS \nDestino: INDIA" + "\nGate: 005" + "\nCodigo: HN/IN/005"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    elif message.text ==  "CANADA-FRANCIA":
        chatid = message.chat.id
        usuario = message.chat.first_name + " " + message.chat.last_name
        boleto = "---------BOLETO---------" + "\nNombre: {nombre}" + "\nSalida: CANADA \nDestino: FRANCIA" + "\nGate: 006" + "\nCodigo: CA/FR/006"
        flybot.send_message(chatid, boleto.format(nombre=usuario))
    else:
        flybot.send_message(chatid, 'Vuelo no existente o No disponible')

@flybot.message_handler(func=lambda message: True)
def echo_all(message):
    chatid = message.chat.id
    flybot.send_message(chatid,"No se reconoce este comando"+"\nUse el comando /help obtener ayuda")

flybot.polling()