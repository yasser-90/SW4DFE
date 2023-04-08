from checkErr import preprocess as fun
file=open('D:\\SW4DFE\\charcase.cpp')
line=file.readlines()
vars=fun.canceledWords(line)
print(vars)
