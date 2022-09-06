import qrcode 

data = 'https://github.com/germinatech/gtech_python_controle/blob/main/Angelica_Nunes_Mendes/Angelica_Nunes_Mendes.pdf'
img = qrcode.make(data) 
img.save('teste1.png')