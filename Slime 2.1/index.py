# author： Zichen
# date: 2021-02-27
# instruction： 随机数抽取
import fcRandom
import fcPreset
import OriginalConsole
from re import sub as reSub
import traceback
Vision = 'Slime2.0'
color = OriginalConsole.color()
while True:
    print(color.yellow + '\n\
——————————{Vision}——————————\n\
/p 使用预设置抽取\n\
/c 创建待设置文件\n\n\
'.format(Vision=Vision)
    )
    command = input(color.blue + '<<<')
    if command == '/p':
        filepath = input(color.blue + '预设置文件路径（可直接将文件拖入控制台）:\n<<<')
        while True:
            continueCommand = input(color.blue + '是否继续抽取?(Y/N)\n<<<')
            if continueCommand.upper() == 'Y':
                try:
                    setting = fcPreset.Read(filepath)
                    Range = setting[0].split('|')[1]
                    Num = int(setting[1].split('|')[1])
                    if setting[2].split('|')[0].split(';')[1] == 'T':  # 过滤
                        filterPath = setting[2].split('|')[1]
                        filterRule = 'T'
                        filterResult = fcRandom.RD(Range,
                                                   Num,
                                                   'Random',
                                                   filterRule,
                                                   filterPath)
                        if setting[3].split('|')[0].split(';')[1] == 'T':  # 表格
                            formPath = setting[3].split('|')[1]
                            print(color.bold + color.cyan + '抽取结果:%s' % reSub(r'[\[\]\']', '', str(fcRandom.FormProcessing(filterResult,
                                                                                                                           formPath,
                                                                                                                           'Random'))))
                        else:
                            print(color.bold + color.cyan + '抽取结果:%s' % reSub(
                                r'[\[\]\']', '', str(filterResult)))

                    else:
                        filterRule = 'F'
                        filterResult = fcRandom.RD(Range,
                                                   Num,
                                                   'Random',
                                                   filterRule,
                                                   None)
                        if setting[3].split('|')[0].split(';')[1] == 'T':
                            formPath = setting[3].split('|')[1]
                            print(color.bold + color.cyan + '抽取结果:%s' % reSub(r'[\[\]\']', '', str(fcRandom.FormProcessing(
                                filterResult,
                                formPath,
                                'Random'))))
                        else:
                            print(color.bold + color.cyan + '抽取结果:%s' % reSub(
                                r'[\[\]\']', '', str(filterResult)))

                except:
                    print(traceback.format_exc())
            else:
                break
    elif command == '/c':
        fcPreset.NewFile()
