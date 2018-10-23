import os
data_dir='audio/estudiantes'
######################
#

archivo=open('lista_estudiantes.txt','w')
label={'mesa':1,'pesa':2,'queso':3,'peso':4, 'si':5,'no':6}
for dirpath, dirnames, filenames in os.walk(data_dir):
   for name in filenames:
      if name.split('.')[1]=='wav':
         fullname = os.path.join(dirpath,name)
         for key in label.keys():
            if key in fullname.lower():
               linea = fullname +'\t' + str(label[key]) + '\n' 
               break
         archivo.write(linea)
        
        
archivo.close()
