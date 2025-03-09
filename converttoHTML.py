import pandas as pd

columns = ["Animal","Class","Diet","Province","Endangered Status","Population","Native/Invasive","Habitat"]
df = pd.read_csv('SDCC_Database.csv', names=columns)

html_string =df.to_html()
Func = open ('list.html','w')
Func.write(html_string)
Func.close()