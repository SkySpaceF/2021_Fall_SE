import os
import sys
import re

#all_data=open(r".\CSample.cpp",'r').read()
# print(all_data)

#将目标文件读入
def ReadFile(path):

    fp=open(path,'r',encoding='utf-8')
    punc = '~`!#$%^&*()_+-=|\';":/.,?><~·！@#￥%……&*（）——+-=“：’；、。，？》《'
    file_content=re.sub(r"[%s]+" %punc, " ",fp.read())
    c=file_content.split('\n')
    return c

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









#返回文本中题目要求的关键词组成的列表（该关键词并非标准C或CPP关键词）
def GetKey(file_content):
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
        elif 'break' in i:
            list_dest.append('break')
        elif 'default' in i:
            list_dest.append('default')
        elif 'return' in i:
            list_dest.append('return')
    return list_dest
def GetExtractKeyList(file_content):
    list_dest = []
    for i in file_content:
        if '{' in i:
            list_dest.append('{')
        elif '}' in i:
            list_dest.append('}')
        elif 'else if' in i:
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
#尝试在保留大括号的同时提取关键词
def NGetExtractKeyList(file_content):
    list_dest = []
    for i in file_content:
        if '{' in i:
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
            list_dest.append('{')
        elif '}' in i:
            elif 'else if' in i:
                list_dest.append('else if')
            elif 'if' in i:
                list_dest.append('if')
            elif 'else' in i:
                list_dest.append('else')
            elif 'switch' in i:
                list_dest.append('switch')
            elif 'case' in i:
                list_dest.append('case')
        elif '{'in i and '}' in i:
            elif 'else if' in i:
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
print(file_content)
Extracted_Key_list=GetExtractKeyList(file_content)
print(Extracted_Key_list)
# print(key_list)
# print(GetExtractKeyList(file_content))
# print('total num: ',CountStdCKey(key_list))
# key_list=GetKey(file_content)
# print('switch num: ',key_list.count('switch'))
#
# print('case num: ',end='')
# print(*CountCase(Extracted_Key_list),sep=' ')

