import qrcode as qr
import PySimpleGUI as sg 

sg.theme('DarkPurple')
font =('Verdana', 12)

qrImage = [sg.Image('', key = 'QRCODE')]

# the layout
index = 0
color = {0: ("purple", "blue"), 1: ("Teal", "red")}
layout = [
    [sg.Text('Enter URL:'), sg.Input(text_color= 'black', key= 'URL' )],
    [sg.Button('Create', key='Submit',  mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1)),  sg.Button('Close', key='CLOSE',mouseover_colors= color[index], use_ttk_buttons=True, size= (7,1))],
    [sg.Column([qrImage], justification= 'center')],
]

 # Create the Window
window = sg.Window('QR coode Generator', layout, font= font)

# Event loop  
while True:
    event , values = window.read()
    if event == sg.WIN_CLOSED or event == 'CLOSE':
        break
    elif event == 'Submit':
        url = values['URL']
        if url:
            qr_code = qr.QRCode(
                version=1,
                error_correction=qr.constants.ERROR_CORRECT_L,
                box_size=20,
                border=4,
                )
            qr_code.add_data('Some data')
            qr_code.make(fit=True)
            img = qr_code.make_image(fback_color=(255, 195, 235), fill_color=(55, 95, 35))
            img.save('qr_code.png')
            window['QRCODE'].update('qr_code.png')
window.close()