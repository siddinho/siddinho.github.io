import pandas as pd
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import DataTable,TableColumn
import os
from bokeh.io import output_file, show

output_file("index.html")

#data = dict(
       # dates=[date(2014, 3, i+1) for i in range(10)],
       # downloads=[randint(0, 100) for i in range(10)],
   # )
#source = ColumnDataSource(data)
dba = pd.read_excel("DBA.xlsx") 
#dba = pd.DataFrame(dba1)  
#a= sorted(dba['CPU'] , reverse = 1)
#a = dba.sort_values('Cumulative CPU time in ms (S + R)',ascending=[False])   
#a=sorted(dba, key = 'Cumulative CPU time in ms (S + R)' )

so = ColumnDataSource(dba)
columns = [
        TableColumn(field="Session ID (S)", title="Session ID"),
        TableColumn(field="Application server host name", title="server"),
        TableColumn(field="CPU", title="CPU time in ms"),
        TableColumn(field="MS SQL Server object name", title="object name"),
        TableColumn(field="SQL Statement", title="SQL Statement")
    ]

data_table = DataTable(source=so, columns=columns, width=1100, height=700)


show((data_table))