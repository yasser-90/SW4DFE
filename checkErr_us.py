import re


class Preprocess:
    def canceledWords(self, Wordw):
        flag = 0
        CanceledWord = ['Break', 'break', 'print', 'System', 'cout', 'Cout', 'Cin', 'Class', 'class', 'cin', 'main',
                        'namespace']
        for checkword in CanceledWord:
            if Wordw.find(checkword) != -1:
                flag = 1
                break
        return flag

    def pre_processing(self, path):
        file1 = open(path, 'r')
        comment = 0
        Lines = file1.readlines()
        if (file1.name.endswith("py")):
            file2 = open('D:\\resultpre.py', 'w')
            for line in Lines:
                line = line.strip()
                line = re.sub(r'\s+', ' ', line)
                line = re.sub(r'\'.*?', '\'', line)
                line = re.sub(r'\".*?', '\"', line)

                if not (line.strip() == "" or (line.startswith("import"))):
                    if not (line.find("\'''") > -1 or line.find("\"""") > -1) and (comment == 0):
                        if line.find("#") == 0:
                            continue
                        else:
                            if line.find("#") != -1:
                                line = line[0:line.find("#")]
                                if self.canceledWords(line) == 1:
                                    file2.write(line + "  ** Can Li\n")
                                else:
                                    file2.write(line + "\n")
                            else:
                                # if self.canceledWords(line) == 1:
                                #     file2.write(line + "  ** Can Li\n")
                                # else:
                                file2.write(line + "  ** Can Li\n")
                    else:

                        if (line.find("\'''") > -1 or line.find("\"""") > -1) and (comment == 0):
                            comment = 1

                            if not (line.startswith("\'''") or line.startswith("\"""")):

                                line = line[0:line.find("\'''")]
                                if self.canceledWords(line) == 1:
                                    file2.write(line + "  ** Can Li\n")
                                else:
                                    file2.write(line + "\n")
                        else:
                            if (line.find("\'''") >= 0 or line.find("\"""") >= 0) and (comment == 1):

                                line = line[line.find("\'''") + 3:]
                                comment = 0
                                if line.strip() != "":
                                    if self.canceledWords(line) == 1:
                                        file2.write(line + "  ** Can Li\n")
                                    else:
                                        file2.write(line + "\n")
                            else:
                                file2.write(line + "  ** Can Li\n")
                else:
                    if not line.strip() == "":
                        file2.write(line + "  ** Can Li\n\n")

        else:
            file2 = open('D:\\resultpre.' + file1.name[file1.name.find('.') + 1:], 'w')
            for line in Lines:
                line = line.strip()
                line = re.sub(r'\s+', ' ', line)
                line = re.sub(r'\'.*?\'', '\'\'', line)
                line = re.sub(r'\".*?\"', '\'\'', line)
                if (line.startswith('{') or line.startswith('}')):
                    file2.write(line + "  ** Can Li\n\n")
                    continue
                if not (line.strip() == "" or (line.startswith("import")) or (line.startswith("#include")) or (
                        line.find('main') != -1) or (line.startswith('using namespace'))):
                    if not (line.find("/*") > -1) and (comment == 0):

                        if line.find("//") == 0:
                            continue
                        else:
                            if line.find("//") != -1:
                                line = line[0:line.find("//")]
                                if self.canceledWords(line) == 1:
                                    file2.write(line + "  ** Can Li\n")
                                else:
                                    file2.write(line + "\n")

                            else:
                                if self.canceledWords(line) == 1:
                                    file2.write(line + "  ** Can Li\n")
                                else:
                                    file2.write(line + "\n")
                    else:

                        if (line.find("/*") > -1) and (comment == 0):
                            comment = 1

                            if not (line.startswith("/*")):

                                line = line[0:line.find("/*")]
                                if self.canceledWords(line) == 1:
                                    file2.write(line + "  ** Can Li\n")
                                else:
                                    file2.write(line + "\n")

                        else:
                            if (line.find("*/") >= 0) and (comment == 1):

                                line = line[line.find("*/") + 2:]
                                comment = 0
                                if line.strip() != "":
                                    if self.canceledWords(line) == 1:
                                        file2.write(line + "  ** Can Li\n\n")
                                    else:
                                        file2.write(line + "\n")
                            else:
                                # ✅ if not(line.find("*/")>=0 ) and (comment==1):
                                # continue
                                file2.write(line + "  ** Can Li\n\n")




                else:
                    if (line.strip() == "" or (line.startswith("import")) or (line.startswith("#include")) or (
                            line.find('main') != -1) or (line.startswith('using namespace'))):
                        file2.write(line + "  ** Can Li\n\n")

        file1.close()
        file2.close()

a = Preprocess()
a.pre_processing('test.py')
a.pre_processing('test2.cpp')



