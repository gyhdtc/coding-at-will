import os
import os.path
import linecache
import openpyxl
needs = ["Four Character ID","Monument Description","Height of the Monument","Monument Foundation","Foundation Depth","Marker Description"]
for parent,dirname,filenames in os.walk("c:\\Users\\gyh\\Desktop\\log\\log"):
    print(len(filenames))
    wb = openpyxl.Workbook()
    sheet = wb.active
    hang = 1
    for filename in filenames:  #输出文件信息
        print("-----------------------",filename,"-----------------------")
        fopen = open(".\\log\\"+filename,'r',encoding='gbk',errors='ignore')
        lines = fopen.readlines()
        count = []
        for need in needs:
            for line in lines:
                if need in line:
                    count.append(line.split(':'))
                    break;
        lie = 1
        for i in count:
            print(i[1].strip())
            sheet.cell(hang,lie,value = str(i[1].strip()))
            lie += 1
        hang += 1
        wb.save(".\shit.xlsx")
        print("-----------------------",filename,"-----------------------")  