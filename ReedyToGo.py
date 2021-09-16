import re


#读取目标文件，以列表形式返回，去除了符号
#输入文件的相对路径，输出去除所有符号并以换行符分割文件内容的列表
def ReadFile(path):
    #path为传入的c,cpp路径，这里取相对路径
    fp=open(path,'r',encoding='utf-8')
    #通过正则化原文本内容，去除所有符号
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
    file_content=re.sub(r"[%s]+" %punc, " ",fp.read())
    #文本通过换行符分割
    file_content=file_content.split('\n')
    return file_content

#将ReadFile处理的文件内容中空格删除，并进一步细化关键词
#输入ReadFile()处理后返回的列表，将其
def SplitTxtByBlank(file_content):
    key_list=[]
    for single_line in file_content:
        single_word=single_line.split(' ')
        single_word=list(filter(None,single_word))
        for element in single_word:
            if element!='':
                key_list.append(element)
    return key_list


#提取文件中重要关键词
#传入ReadFile()处理后返回的列表，返回以重要关键词组成的列表
def GetExtractKeyList(file_content):
    list_dest = []
    for i in file_content:
        if 'else if' in i:
            list_dest.append('else if')
        elif 'if' in i:
            list_dest.append('if')
        elif 'else' in i:
            list_dest.append('else')
        elif 'switch' in i:
            list_dest.append('switch')
        elif 'case' in i:
            list_dest.append('case')
    return list_dest


#返回文件中C、CPP关键词的总数
#传入ReadFile()处理文件后返回的列表，返回关键词的个数
def CountStdCKey(key_list):
    std_CKey=['else if','char','double','enum','float','int','long',
              'short','signed','struct','union','unsigned',
              'void','for','do','while','break','continue',
              'if','else','goto','switch','case','default',
              'return','auto','extern','register','static',
              'const','sizeof','typedef','volatile'
              ]
    num_key=0
    for element in key_list:
        if element in std_CKey:
            num_key+=1
    return num_key


#返回case数目为元素的列表
#传入重要关键词组成的列表列表，输出每组switch内的case数目
def CountCase(Extracted_Key_list):
    #文件中有switch才能统计case
    if(Extracted_Key_list.count('switch')):
        num_case=[]
        for i in range(len(Extracted_Key_list)):
            if Extracted_Key_list[i]== 'switch':
                offset=1
                cnt=0
                while(1):
                    if(Extracted_Key_list[i + offset]== 'case'):
                        cnt+=1
                        offset+=1
                    else:
                        break
                num_case.append(cnt)
        return num_case
    else:
        return [0]









if __name__ == '__main__':
    print("请将测试文件放在与本脚本文件同一目录下")
    path_level=input("请输入测试文件名称和等级,目前仅支持1、2级")
    path_level_list=path_level.split(' ')
    path=str(path_level_list[0])
    level=int(path_level_list[-1])
    if level>2 or level<0 :
        print('等级输入错误！')

    file_content = ReadFile(path)
    key_list = SplitTxtByBlank(file_content)

    if level==1:
        print('total num: ', CountStdCKey(key_list))
    else:
        print('total num: ', CountStdCKey(key_list))
        print('switch num: ',key_list.count('switch'))
        Extracted_Key_list = GetExtractKeyList(file_content)
        print('case num: ',end='')
        print(*CountCase(Extracted_Key_list),sep=' ')
    #
    # file_content=ReadFile('CSample.cpp')
    # print(file_content)
    # key_list=SplitTxtByBlank(file_content)
    # Extracted_Key_list=GetExtractKeyList(file_content)
    # print(key_list)
    # print(GetExtractKeyList(file_content))
    # print('total num: ',CountStdCKey(key_list))
    # key_list=GetExtractKeyList(file_content)
    # print('switch num: ',key_list.count('switch'))
    #
    # print('case num: ',end='')
    # print(*CountCase(Extracted_Key_list),sep=' ')
    #
