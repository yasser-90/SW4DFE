import re


class Preprocess:
    def canceledWords(word):
        flag = 0
        canceledWord = ['Break', 'break', 'print', 'System', 'cout',
                        'Cout', 'Cin', 'Class', 'class', 'cin', 'main', 'namespace']
        for checkword in canceledWord:
            if word.find(checkword) != -1:
                flag = 1
                break
        return flag

    def pre_processing(path):
        file1 = open(path, 'r')
        comment = 0
        lines = file1.readlines()
        # lines content all line in file

        # start if file.py
        if (file1.name.endswith("py")):
            file2 = open('result.py', 'w')
            for line in lines:
                # remove start ad end space
                line = line.strip()
                # remove space between
                line = re.sub(r'\s+', '', line)
                # remove special in special between ''
                line = re.sub(r'\'.*\'', '\'\'', line)
                # remove special in special between ""
                line = re.sub(r'\".*\"', '\'\'', line)

                # start if not (line.strip() == "" or (line.startswith("import"))):
                if not (line.strip() == "" or (line.startswith("import"))):

                    # start if not (line.find("\'''") > -1 or line.find("\"""") > -1) and (comment == 0):
                    if not (line.find("\'") > -1 or line.find("\"") > -1) and (comment == 0):
                        if line.find("#") == 0:
                            continue
                        else:
                            if line.find("#") != -1:
                                line = line[0:line.find("#")]
                                if Preprocess.canceledWords(line) == 1:
                                    file2.write(line+"\n")
                                else:
                                    file2.write(line+"\n")
                            else:
                                if Preprocess.canceledWords(line) == 1:
                                    file2.write(line+"\n")
                                else:
                                    file2.write(line+"\n")
                    # ELSE if not (line.find("\'''") > -1 or line.find("\"""") > -1) and (comment == 0):
                    else:

                        if (line.find("\'") > -1 or line.find("\"") > -1) and (comment == 0):
                            comment = 1

                            if not (line.startswith("\'") or line.startswith("\"")):

                                line = line[0:line.find("\'")]
                                if Preprocess.canceledWorks(line) == 1:
                                    file2.write(line+"\n")
                                else:
                                    file2.write(line+"\n")
                        else:
                            if (line.find("\'") >= 0 or line.find("\"") >= 0) and (comment == 1):

                                line = line[line.find("\'")+3:]
                                comment = 0
                                if line.strip() != "":
                                    if Preprocess.canceledWords(line) == 1:
                                        file2.write(line+"\n")
                                    else:
                                        file2.write(line+"\n")
                            else:
                                file2.write(line+"\n")
                # ELSE if not (line.strip() == "" or (line.startswith("import"))):
                else:
                    if not line.strip() == "":
                        file2.write(line+"\n")
        # ELSE if file.py
        else:
            file2 = open('result.' +
                         file1.name[file1.name.find('.')+1:], 'w')

            for line in lines:
                line = line.strip()
                line = re.sub(r'\s+', '', line)
                line = re.sub(r'\'.*?\'', '\'\'', line)
                line = re.sub(r'\".*?\"', '\'\'', line)
                if (line.startswith('{') or line.startswith('}')):
                    file2.write(line+"\n")
                    continue
                if not (line.strip() == "" or (line.startswith("import")) or (line.startswith("#include")) or (line.find('main') != -1) or (line.startswith('using namespace'))):
                    if not (line.find("/*") > -1) and (comment == 0):

                        if line.find("//") == 0:
                            continue
                        else:
                            if line.find("//") != -1:
                                line = line[0:line.find("//")]
                                if Preprocess.canceledWords(line) == 1:
                                    file2.write(line+"\n")
                                else:
                                    file2.write(line+"\n")

                            else:
                                if Preprocess.canceledWords(line) == 1:
                                    file2.write(line+"\n")
                                else:
                                    file2.write(line+"\n")
                    else:

                        if (line.find("/*") > -1) and (comment == 0):
                            comment = 1

                            if not (line.startswit("/*")):

                                line = line[0:line.find("/*")]
                                if Preprocess.canceledWords(line) == 1:
                                    file2.write(line+"\n")
                                else:
                                    file2.write(line+"\n")

                        else:
                            if (line.find("*/") >= 0) and (comment == 1):

                                line = line[line.find("*/")+2:]
                                comment = 0
                                if line.strip() != "":
                                    if Preprocess.canceledWords(line) == 1:
                                        file2.write(line+"\n")
                                    else:
                                        file2.write(line+"\n")
                            else:
                                # ✅ if not(line.find("*/")>=0 ) and (comment==1):

                                file2.write(line+"\n")

                else:
                    if (line.strip() == "" or (line.startswith("import")) or (line.startswith("#include")) or (line.find('main') != -1) or (line.startswith('using namespace'))):
                        file2.write(line+"\n")

        file1.close()
        file2.close()


Preprocess.pre_processing('code.py')

# def gg(text):
#     canceledWord = ['Break', 'break', 'print', 'System', 'cout',
#                     'Cout', 'Cin', 'Class', 'class', 'cin', 'main', 'namespace']
#     fiag = 0
#     for checkword in canceledWord:
#         if text.find(checkword) != -1:
#             flag = 1
#             break
#     return flag


# print(gg(' ali cin'))


# def openFile(path):
#     file1 = open(path, 'r')
#     comment = 0
#     return file1.name.endswith("txt")


# print(openFile('Note.txt'))
# gg = '\"ali ali*?\"'
# gg = re.sub(r'\s+', 'o', gg)
# gg = re.sub(r'\'.*?\'', 'n', gg)
# gg = re.sub(r'\".*?\"', 'k', gg)
# print(gg)
# gg = 'ali ali\''''
# print(gg.startswith("g"))
