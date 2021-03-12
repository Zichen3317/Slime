# author： Zichen
# date: 2021-02-28
# instruction： 读取预设置，创建新预设文件

import OriginalConsole
import traceback
from datetime import datetime
from re import search as reSearch
color = OriginalConsole.color()


def Read(settingfile):
    '''
    用于读取预设置的函数
    参数：
    settingfile  预设置路径文件
    '''
    try:
        with open(settingfile, 'r', encoding='utf-8') as f:
            setting = f.read()

        setting_out = []  # 最后输出的数据列表，不包含带'//'的注释文件
        for i in setting.split('\n'):
            if bool(reSearch('//', i)) != True:
                setting_text = i.split('|')
                print(color.green+"\
{key}:{value} 可读状态:{bool}\
".format(key=setting_text[0].split(';')[0],
                    value=setting_text[1],
                    bool=setting_text[0].split(';')[1]))
                setting_out.append(i)
            else:
                pass
        return setting_out
    except:
        print(traceback.format_exc())


def NewFile():
    '''
    创建新预设文件
    '''
    with open('./预设置[%s].txt' % str(datetime.today()).split(' ')[0], 'w', encoding='utf-8') as f:
        f.write("\
//Tip: ';'后的 T/F 代表该项内容的读取状态，T：可读取，F：不可读取\n\
//请将填写的内容填写至'|'之后\n\
抽取范围;T|\n\
抽取个数;T|\n\
过滤规则路径;F|\n\
表格路径;F|")
    print(color.bold + color.green+'已创建新待设置文件，保存至./预设置[%s].txt' %
          str(datetime.today()).split(' ')[0])
