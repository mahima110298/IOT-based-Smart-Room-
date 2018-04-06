import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['https://spreadsheets.google.com/feeds' , 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)
sheet = client.open('Mode.csv').sheet1


def printSheet() :
    row_count=len(sheet.get_all_records())+1
    for i in range(row_count) :
        RowInfo = sheet.row_values(i+1)
        print(RowInfo)

#to get column Info
#ColInfo = sheet.col_values(i)
#to get row Info
#ColInfo = sheet.row_values(i)
#to get cell value
#CellInfo = sheet.cell(x,y)
#to get all records
#ModeInfo = sheet.get_all_records()
#to update Cell
#sheet.update_cell(5,2,'changed')
#to insert a row
#row = ['new device' , 'new device ki state']
#index = 6
#sheet.insert_row(row,index)
#to delete row
#sheet.delete_row(5)
#to get row row_count
#sheet.row_count #giving wrong results
#print(row_count)
sheet.update_cell(5,2,'off')
printSheet()
