import pandas as pd

columns = ["Animal","Class","Diet","Province","Endangered Status","Population","Native/Invasive","Habitat"]
df = pd.read_csv('SDCC_Database.csv', names=columns)

# # This you can change it to whatever you want to get
# age_15 = df[df['age'] == 'U15']
# # Other examples:
# bye = df[df['opp'] == 'Bye']
# crushed_team = df[df['ACscr'] == '0']
# crushed_visitor = df[df['OPPscr'] == '0']
# # Play with this

# Use the .to_html() to get your table in html
html_string =df.to_html()
Func = open ('list.html','w')
Func.write(html_string)
Func.close()