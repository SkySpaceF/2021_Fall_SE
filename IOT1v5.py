
import sys
import re


#将目标文件读入，以列表形式返回，去除了符号
def ReadFile(path):
    fp=open(path,'r',encoding='utf-8')
    #通过正则化原文本内容，去除所有符号
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《{}'
    file_content=re.sub(r"[%s]+" %punc, " ",fp.read())
    #文本通过换行符分割
    c=file_content.split('\n')
    return c
#处理去除符号过文本以实现用空格分割
def SplitTxtByBlank(file_content):
    key_list=[]
    for single_line in file_content:
        single_word=single_line.split(' ')
        single_word=list(filter(None,single_word))
        for element in single_word:
            if element!='':
                key_list.append(element)
        #key_list.append(single_word)
    return key_list

#输入读入的文件，输出提取了swich,if，else,else if组成的列表
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


#将关键字列表中的C标准关键字统计出来
def CountStdCKey(key_list):
    std_CKey=['else if','char','double','enum','float','int','long',
              'short','signed','struct','union','unsigned',
              'void','for','do','while','break','continue',
              'if','else','goto','switch','case','default',
              'return','auto','extern','register','static',
              'const','sizeof','typedef','volatile'
              ]
    # std_Key=[
    #         'else if','if','else','switch','case','break','default'
    # ]
    num_key=0
    for element in key_list:
        if element in std_CKey:
            num_key+=1
    return num_key


#统计case有多少
def CountCase(Extracted_Key_list):
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



file_content=ReadFile('../MyCode/CSample.cpp')
key_list=SplitTxtByBlank(file_content)
Extracted_Key_list=GetExtractKeyList(file_content)
print(key_list)
print(GetExtractKeyList(file_content))
print('total num: ',CountStdCKey(key_list))
key_list=GetKey(file_content)
print('switch num: ',key_list.count('switch'))

print('case num: ',end='')
print(*CountCase(Extracted_Key_list),sep=' ')

