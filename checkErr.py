import re
class preprocess:
  def canceledWords(Wordw):
      flaag=0
      CanceledWord=('break','system','cout','class','cin','main','namespace')
      for checkword in CanceledWord:
         if Wordw.find(checkword)!=-1:
            flaag=1
            break
         return flaag

  def pre_processing(path) :
         file1 = open('D:\\SW4DFE\\charcase.cpp', 'r')          
         comment=0
         Lines = file1.readlines()
         if(file1.name.endswith(".cpp")):
            file2 = open('D:\\SW4DFE\\output.txt', 'w+')
            for line in Lines:
               line=line.strip()
               line=re.sub(r'\s+', ' ', line)
               line=re.sub(r'\'.*?\'', '\'\'', line)
               line=re.sub(r'\".*?\"', '\'\'', line)

               if not(line.strip()=="" or (line.startswith("import"))):
                  if not(line.find("\'''")>-1 or line.find("\"""")>-1)and (comment==0): 
                     if line.find("#")==0: 
                        continue
                  else:
                     if line.find("#")!=-1:
                        line=line[0:line.find("#")]
                        if preprocess.canceledWords(line)==1:
                           file2.write( line+"Can Li\n")
                        else:   
                           file2.write( line+"\n")
                    
               else:
                  
                  if (line.find("\'''")>-1 or line.find("\"""") >-1) and (comment==0):
                        comment=1
                  
                        if not(line.startswith("\'''") or line.startswith("\"""") ):
                           
                           line=line[0:line.find("\'''")]
                           global canceledWords
                           if canceledWords(line)==1:
                              file2.write(line+"Can Li\n")
                           else:
                              file2.write(line+"\n")
                  else:
                     if (line.find("\'''")>=0 or line.find("\"""") >=0) and (comment==1):
                        line=line[line.find("\'''")+3:]
                        comment=0
                        if line.strip()!="":
                            if canceledWords(line)==1:
                              file2.write(line+"Can Li\n")
                        else:
                            file2.write(line+"\n")
                     else:
                        file2.write( line+"Can Li\n")
            else:
                if not line.strip()=="" :
                     file2.write(line+"Can Li\n\n")             
           
         else:
            file2 = open('D:\\SW4DFE\\output.txt'+file1.name[file1.name.find('.')+1:], 'a')
            for line in Lines:
               line=line.strip()
               line=re.sub(r'\s+', ' ', line)
               line=re.sub(r'\'.*?\'', '\'\'', line)
               line=re.sub(r'\".*?\"', '\'\'', line)
               if(line.startswith('{') or line.startswith('}')):
                  file2.write( line+"Can Li\n\n")
                  continue
               if not(line.strip()=="" or (line.startswith("import")) or (line.startswith("#include")) or (line.find('main')!=-1)or (line.startswith('using namespace'))):
                  if not(line.find("/*")>-1 )and (comment==0):
                     
                     if line.find("//")==0:
                        continue
                     else:
                        if line.find("//")!=-1:
                           line=line[0:line.find("//")]
                           if preprocess.canceledWords(line)==1:
                              file2.write( line+"Can Li\n")
                           else:
                              file2.write( line+"\n")
                        else:
                           if preprocess.canceledWords(line)==1:
                              file2.write( line+"Can Li\n")
                           else:
                                 file2.write( line+"\n")
                  else:    
                     if (line.find("/*")>-1 ) and (comment==0):
                        comment=1
                     
                        if not(line.startswit("/*") ):
                           line=line[0:line.find("/*")]
                           if preprocess.canceledWords(line)==1:
                              file2.write( line+"Can Li\n")
                           else:
                              file2.write( line+"\n")
                     else:
                        if (line.find("*/")>=0 ) and (comment==1):
                           line=line[line.find("*/")+2:]
                           comment=0
                           if line.strip()!="":
                              if preprocess.canceledWords(line)==1:
                                 file2.write( line+"Can Li\n\n")
                              else:
                                 file2.write( line+"\n")
                        else:
                           #✅ if not(line.find("*/")>=0 ) and (comment==1):
                           file2.write( line+"Can Li\n\n")
               else:
                  if (line.striip()=="" or (line.startswith("import")) or (line.startswith("#include")) or (line.find('main')!=-1)or (line.startswith('using namespace'))):
                     file2.write(line+"Can Li\n\n")
               
         file1.close()
         file2.close()
         

       



