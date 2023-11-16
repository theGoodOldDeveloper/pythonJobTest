#!/usr/bin/env python
import wx
import wx.grid
import mysql.connector
import controldatabase
import connectdatabase
import csv
import writecsv
from pathlib import Path

# connect to database
mydb = connectdatabase.constr()
mycursor = mydb.cursor()

# input table(s) name(s) and longest name
mycursor.execute("SHOW TABLES")
myresult2 = mycursor.fetchall()
mycursor.execute("SELECT count(*) AS TOTALNUMBEROFTABLES FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_SCHEMA = 'test'")
myresult3 = mycursor.fetchall()
[tableNames, tableMaxLength] = controldatabase.checked(myresult2,myresult3)
tablePiece = len(tableNames)
pause = "        "
cbox = []
cboxvalue = []
for i in range(len(tableNames)):
    cbox.append('')
    cboxvalue.append(False)

# create frame Class
class DataBaseExport(wx.Frame):
    def __init__(self, *args, **kw):
        super(DataBaseExport, self).__init__(*args, **kw, size=((tableMaxLength*5 + 250), (tablePiece*50+100)))
        self.panel = wx.Panel(self)
        self.Centre()

        # create checkboxes
        vbox = wx.BoxSizer(wx.VERTICAL)
        self.SetSizer(vbox)
        self.SetBackgroundColour(wx.Colour(200, 0, 200))  # RGB values for a light gray color
        for i in range(len(tableNames)):
            cbox[i] = wx.CheckBox(self,id = i , label = pause + tableNames[i])
            font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
            # panel.SetBackgroundColour(wx.Colour(200, 200, 200))
            cbox[i].SetFont(font)
            vbox.Add(cbox[i], 0, wx.ALL, 10)
        self.Bind(wx.EVT_CHECKBOX, self.onChecked)
        hbox = wx.BoxSizer(wx.HORIZONTAL)
        hbox.Add((20, 20), 1)
        self.button = wx.Button(self, label="Mehet")
        # Set the font size for the checkbox label
        font = wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL)
        self.button.SetFont(font)
        hbox.Add((self.button))
        vbox.Add(hbox)
        self.button.Bind(wx.EVT_BUTTON, self.OnClickButton)

    def OnClickButton(self, event):
        # set root folder
        data_folder = Path("../../")

        # examination of choice
        for i in range(len(tableNames)):
            if cboxvalue[i]:
                mycursor.execute("SELECT * FROM " + tableNames[i])
                data = mycursor.fetchall()
                file_name = tableNames[i] + '.csv'
                file_path = data_folder / file_name
                writecsv.write_to_csv(file_path, data)
        print('Game over...')
        self.Close(True)
        ####### end write CVS method #######
        
    def onChecked(self, e):
        cb = e.GetEventObject()
        cboxvalue[cb.GetId()]=cb.Value

    def OnExit(self, event):
        """Close the frame, terminating the application."""
        self.Close(True)

if __name__ == '__main__':
    app = wx.App()
    frm = DataBaseExport(None, title='Export data to CVS file')
    frm.Show()
    app.MainLoop()