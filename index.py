# author： Zichen
# date: 2021-02-27
# instruction： 随机数抽取
import fcRandom
import fcPreset
from rich.console import Console  # 控制台模块
from re import sub as reSub
orange = '#ffb74d'
cyan = '#63e6be'
grey = '#bdbdbd'
console = Console(color_system='auto')  # 创建控制台
# 程序文本规则：
# debug文本：绿色
# error文本：红色
# 提示文本：蓝色
# 目标信息反馈文本：橙色 #ffb74d
# 程序菜单标题及提示文本中需特殊强调部分： 青色 #63e6be
# 待定颜色：；灰色 #bdbdbd
Vision = 'Slime2.0'
while True:
    console.print('\n[bold {orange}]\
——————————{Vision}——————————\n\
/p 使用预设置抽取\n\
/c 创建待设置文件\n\n\
'.format(Vision=Vision, orange=orange)
    )
    command = console.input('[bold blue]<<<')
    if command == '/p':
        filepath = console.input('[bold blue]预设置文件路径（可直接将文件拖入控制台）:\n<<<')
        while True:
            continueCommand = console.input('[bold blue]是否继续抽取?(Y/N)\n<<<')
            if continueCommand.upper() == 'Y':
                try:
                    setting = fcPreset.Read(filepath)
                    Range = setting[0].split('|')[1]
                    Num = int(setting[1].split('|')[1])
                    if setting[2].split('|')[0].split(';')[1] == 'T':
                        filterPath = setting[2].split('|')[1]
                        filterRule = 'T'
                        if setting[3].split('|')[0].split(';')[1] == 'T':
                            formPath = setting[3].split('|')[1]
                            console.print('[bold #ffb74d]抽取结果:%s' % reSub(r'[\[\]\']', '', str(fcRandom.FormProcessing(
                                fcRandom.RD(Range,
                                            Num,
                                            'Random',
                                            filterRule,
                                            filterPath),
                                formPath,
                                'Random'))))
                        else:
                            console.print('[bold #ffb74d]抽取结果:%s' % reSub(r'[\[\]\']', '', str(fcRandom.RD(Range,
                                                                                                           Num,
                                                                                                           'Random',
                                                                                                           filterRule,
                                                                                                           filterPath))))

                    else:
                        filterRule = 'F'
                        if setting[3].split('|')[0].split(';')[1] == 'T':
                            formPath = setting[3].split('|')[1]
                            console.print('[bold #ffb74d]抽取结果:%s' % reSub(r'[\[\]\']', '', str(fcRandom.FormProcessing(
                                fcRandom.RD(Range,
                                            Num,
                                            'Random',
                                            filterRule,
                                            None),
                                formPath,
                                'Random'))))
                        else:
                            console.print('[bold #ffb74d]抽取结果:%s' % reSub(r'[\[\]\']', '', str(fcRandom.RD(Range,
                                                                                                           Num,
                                                                                                           'Random',
                                                                                                           filterRule,
                                                                                                           None))))

                except:
                    console.print_exception()
            else:
                break
    elif command == '/c':
        fcPreset.NewFile()
