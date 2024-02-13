import xml.etree.ElementTree as ET
import csv

tree=ET.parse("datafile.xml")
root=tree.getroot()

cpi_com = open('cpi_combined.csv', 'w')
cpi_rur = open('cpi_rural.csv', 'w')
cpi_urb = open('cpi_urban.csv', 'w')
cpi_og  = open('cpi_original.csv','w')
csvbth=csv.writer(cpi_com)
csvrur=csv.writer(cpi_rur)
csvurb=csv.writer(cpi_urb)
csog=csv.writer(cpi_og)

r_tot=len(root)

rnum=0
while rnum<=r_tot:
    rur_data=[]
    com_data=[]
    urb_data=[]
    og_data=[]
    for entry in root.findall('ROW'+str(rnum+1)):
        rsz=len(root[rnum])
        if rnum==0:
            i=0
            while i+1<=len(root[0]):
                a=root[rnum][i].tag
                urb_data.append(a)
                com_data.append(a)
                rur_data.append(a)
                og_data.append(a)
                i+=1
                            
            csvbth.writerow(com_data)
            csvurb.writerow(urb_data)
            csvrur.writerow(rur_data)
            csog.writerow(og_data)
                
        f=root[rnum][0].text
        
        rur_data=[]
        com_data=[]
        urb_data=[]
        og_data=[]
        
        if f=='Urban': 
            i=0
            while i+1<=len(root[rnum]):
                a=root[rnum][i].text
                urb_data.append(a)
                og_data.append(a)
                i+=1
            csvurb.writerow(urb_data)
        
        if f=='Rural':
            i=0
            while i+1<=len(root[rnum]):
                a=root[rnum][i].text
                rur_data.append(a)
                og_data.append(a)
                i+=1
            csvrur.writerow(rur_data)
        
        if f=='Rural+Urban':
            i=0
            while i+1<=len(root[rnum]):
                a=root[rnum][i].text
                com_data.append(a)
                og_data.append(a)
                i+=1
            csvbth.writerow(com_data)
        
        
        csog.writerow(og_data)                 

    rnum+=1 
cpi_com.close()
cpi_rur.close()
cpi_urb.close()
cpi_og.close()
