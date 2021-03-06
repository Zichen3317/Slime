# author： Zichen
# date: 2021-01-09
# vision: 1.0
# instruction：随机数模块

import random
import ConsoleLog
import xlrd
from rich.console import Console  # 控制台模块
orange = '#ffb74d'
cyan = '#63e6be'
grey = '#bdbdbd'
console = Console(color_system="auto")  # 创建控制台

logger = ConsoleLog.ConsoleLog()


def RD(Range, Num, algorithm, filterRule, filterPath):
    """
    随机抽取函数
    参数:
    Range 抽取范围
    Num 抽取个数 int
    algorithm 算法 str
    filiter 是否(True/False)使用过滤器过滤 str

    工作机理：
    读取抽取范围、抽取个数
    ->定义抽取最大最小值
    ->读取抽取个数
    ->按照选择的算法进行抽取
    ->输出结果
    ->写入日志
    """
    if filterRule == 'T':  # 过滤√
        numLst = []  # 装被抽取数字的列表
        resultLst_out = []  # 装抽取结果的列表
        try:
            for i in range(int(Range.split(',')[0]), int(Range.split(',')[1])):
                numLst.append(i)

            filter_numLst = Filter(filterPath, numLst)  # 过滤完毕的被抽取列表

            resultLst_out.extend(random.choices(filter_numLst, k=Num))

            logger.debug('[算法]%s-[过滤规则路径]%s-[结果]%s' %
                         (algorithm, filterPath, resultLst_out), 'fcRandom.py')
            return sorted(resultLst_out)
        except:
            console.print_exception()
    elif filterRule == 'F':  # 过滤×
        numLst = []  # 装被抽取数字的列表
        resultLst_out = []  # 装抽取结果的列表
        try:
            for i in range(int(Range.split(',')[0]), int(Range.split(',')[1])):
                numLst.append(i)

            resultLst_out.extend(random.choices(numLst, k=Num))
            logger.debug('[算法]%s-[结果]%s' %
                         (algorithm, resultLst_out), 'fcRandom.py')

            return sorted(resultLst_out)
        except:
            console.print_exception()


def FormProcessing(resultLst_in, formPath, algorithm):
    '''
    用于将抽取结果与表格内容匹配并输出匹配结果的函数
    参数：
    resultLst 类型：列表，用于与表格内容匹配
    formPath 类型:str,表格的路径
    algorithm 算法
    '''
    try:
        tempLst = []  # 存放未美化的数据的列表
        finalLst = {}  # 存放最终数据的字典
        workbook = xlrd.open_workbook(formPath)
        sheets = workbook.sheet_names()  # 获取工作簿中的所有表格
        worksheet = workbook.sheet_by_name(sheets[0])  # 获取工作簿中所有表格中的的第一个表格
        for i in range(0, worksheet.nrows):
            for j in range(0, worksheet.ncols):
                tempLst.append(
                    worksheet.cell_value(i, j))  # 逐行逐列读取数据后放入原始列表中

        for index, name in enumerate(tempLst):
            finalLst[index+1] = name  # 将数据以字典的形式储存
    except:
        console.print_exception()

    resultLst_out = []  # 储存抽取结果的列表
    try:
        for i in resultLst_in:
            resultLst_out.append("(%s)%s" % (int(i), finalLst.get(int(i))))

        logger.debug('[算法]%s-[导入表格路径]%s-[结果]%s'
                     % (algorithm, formPath, ','.join(str(x) for x in sorted(resultLst_out))), 'fcRandom.py')  # 输出结果
        return resultLst_out
    except:
        console.print_exception()


def Filter(filterPath, resultLst_in):
    '''
    过滤函数
    filterPath 过滤规则路径
    Be_Choice_Lst 需要过滤的列表
    '''
    with open(filterPath, 'r') as f:
        try:
            filelst = f.read().split(',')
            # console.log(filelst)
            # console.log(filelst.split(','))
        except:
            console.print_exception()
    resultLst_out = []  # 过滤完毕后的列表
    resultLst_out.extend(resultLst_in)
    for i in filelst:
        i = int(i)
        if i in resultLst_out:
            del resultLst_out[resultLst_out.index(i)]
        else:
            pass
    console.print('[bold red]\n过滤规则名:%s\n过滤规则:%s\n' %
                  (filterPath.split('\\')[-1], filelst))
    return resultLst_out
