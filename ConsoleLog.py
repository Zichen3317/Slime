# author： Zichen
# date: 2021-03-06
# instruction： ConsoleLog 配合Rich模块进行日志写入

from datetime import datetime
import os
# 获取日期，用于日志
Date = str(datetime.today()).split(' ')[0]


class ConsoleLog:
    # 初始化日志
    def __init__(self):
        self.logPath = './log/'
        self.logName = 'SlimeLog[%s].log' % Date
        self.logFile = self.logPath + self.logName

        # 检查日志目录是否存在，不存在则创建
        if os.path.isdir(self.logPath) != True:
            os.mkdir(self.logPath)

    def debug(self, message, funcName):
        # debug模式
        with open(self.logFile, 'a+', encoding='utf-8') as L:
            L.write(
                '[{asctime}][{levelname}]{funcName} - {message}\n'
                .format(asctime=str(datetime.today()).split(' ')[1].split('.')[0],
                        levelname='DEBUG',
                        funcName=funcName,
                        message=message))

    def error(self, message, funcName):
        with open(self.logFile, 'a+', encoding='utf-8') as L:
            L.write(
                '[{asctime}][{levelname}]{funcName} - {message}\n'
                .format(asctime=str(datetime.today()).split(' ')[1].split('.')[0],
                        levelname='ERROR',
                        funcName=funcName,
                        message=message))
