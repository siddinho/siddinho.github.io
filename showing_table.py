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
        TableColumn(field="Work Process ID", title="wp"),
        TableColumn(field="Blocking Session ID", title="blocking id"),
        TableColumn(field="CPU", title="CPU time in ms"),
        TableColumn(field="Process ID (S)", title="Process ID (S)")
      
    ]

data_table = DataTable(source=so, columns=columns, width=1100, height=700)


show((data_table))