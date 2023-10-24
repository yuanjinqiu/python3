#/usr/bin/env python
#coding:utf-8
#desc:
#auth:yejunyi
"""
Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved

This module provide configure file management service in i18n environment.

Authors: yejunyi(yejunyi@baidu.com)
Date: 2021/12/10
desc: 此脚本用来比对config.yaml文件，前提是yaml文件都放在同一台设备上，可以是自己本地，也可以是客户现场的同一台服务器。
"""

import yaml
import traceback


#旧包的config.yaml文件完整路径
old_file = input("old confing:")
#新包的config.yaml文件完整路径
new_file = input("new confing:")
#acpoc config.py ${APP} > /tmp/app.config.py 得到的当前客户现场的配置
current_config_file = '/tmp/app.config.py'


def get_config(filename, otype='config.py.yaml'):
    """
    config.py.yaml文件解析函数
    """
    with open(filename) as f:
        x = yaml.load(f,Loader=yaml.FullLoader)
    if otype == 'config.py.yaml':
        return x['options']
    else:
        return x['settings']


def diff(op, old_config, new_config, current_config_file):
    """
    k:v比对函数
    """
    tmp_list = []
    if op == 'more':
        diff_keys = set(new_config.keys()) - set(old_config.keys())
        for k in diff_keys:
            if new_config[k]['default'] != '':
                tmp_list.append(k)
        if len(tmp_list) > 0:
            print(u'新包比老包多的配置(%s个):' % len(tmp_list))
            for k in sorted(tmp_list):
                print('\t%s : %s' % (k, new_config[k]['default']))

    elif op == 'less':
        current_config = get_config(current_config_file, 'acpoc_config')
        diff_keys = set(old_config.keys()) - set(new_config.keys())
        if len(diff_keys) > 0:
            print(u'新包比老包少的配置(%s个):' % len(diff_keys))
            for k in diff_keys:
                print('\t%s :\n\t\t老包    : %s\n\t\t客户环境: %s' % (
                        k, old_config[k]['default'], current_config[k]['value']))

    elif op == 'same':
        current_config = get_config(current_config_file, 'acpoc_config')
        same_keys = set(old_config.keys()) & set(new_config.keys())

        for k in same_keys:
            if new_config[k]['default'] != old_config[k]['default'] and \
                    current_config[k]['source'] == 'default':
                tmp_list.append(k)

        if len(tmp_list) > 0:
            print(u"新包与老包key相同，value不同的配置(%s个):" % (len(tmp_list)))
            for k in tmp_list:
                print('\t%s :\n\t\t新包    : %s\n\t\t老包    : %s\n\t\t客户环境: %s' % (
                    k, new_config[k]['default'], old_config[k]['default'], current_config[k]['value']))
    else:
        print('Invalid params op')
        return 1
    return 0

def main(old_file, new_file, current_config_file):
    """
    主函数
    """
    old_config = get_config(old_file)
    new_config = get_config(new_file)

    ##比对新包比老包多的配置
    diff('more', old_config, new_config, current_config_file)

    ##比对新包比老包少的配置
    diff('less', old_config, new_config, current_config_file)

    ##比对新包、老包不一致的配置
    diff('same', old_config, new_config, current_config_file)

if __name__ == '__main__':
    main(old_file, new_file, current_config_file)