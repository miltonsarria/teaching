import os 
data_dir='/home/sarria/python/audio/audio'
######################
# frequency range to plot

archivo=open('lista.txt','w')
for dirpath, dirnames, filenames in os.walk(data_dir):
   for name in filenames:
      if name.split('.')[1]=='wav':
         fullname = os.path.join(dirpath,name)
         archivo.write(fullname+'\n')
         
         
archivo.close()
