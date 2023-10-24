#/usr/bin/env python3
#coding:utf-8
"""
Copyright (c) 2021 Baidu.com, Inc. All Rights Reserved

This module provide configure file management service in i18n environment.

Authors: yejunyi(yejunyi@baidu.com)
Date: 2021/12/10
desc: 此脚本用来比对metadata.yaml文件，前提是新旧yaml文件都放在同一台设备上，
      可以是自己本地，也可以是客户现场的同一台服务器。
"""

import yaml
#旧包的metadata.yaml文件完整路径
old_file = input("old metadata path:")
#新包的metadata.yaml文件完整路径
new_file = input("new metadata path:")


def get_config(filename):
    """
    解析metadata.yaml文件
    :param filename:
    :return:
    {
        "provides" : xxx,
        "requires": xxx,
        "others" : {"subsystem": xxx, ....}
    }
    """
    exclude_keys = ['maintainer', 'maintainers', 'description', 'tags', 'series', 'summary', 'name']
    necessary_keys = ['provides', 'requires']
    y, z = {}, {}
    with open(filename) as f:
        x = yaml.load(f,Loader=yaml.FullLoader)

    for k in x:
        if k in necessary_keys:
            z[k] = x[k]
            continue
        if k in exclude_keys:
            continue
        y[k] = x[k]
    z['others'] = y
    return z

def diff(old_config, new_config, otype='all'):
    """
    metadata.yaml k:v比对函数
    """
    tmp_list = []
    if otype == 'all':
        desc = u'配置'
    else:
        desc = otype
    ##打印新包比老包多的key
    diff_keys = set(new_config.keys()) - set(old_config.keys())
    if len(diff_keys) > 0:
        print(u'新包比老包多的%s(%s个):' % (desc, len(diff_keys)))
        for k in diff_keys:
            print('\t%s : %s' % (k, new_config[k]))
    ##打印新包比老包少的key
    diff_keys = set(old_config.keys()) - set(new_config.keys())
    if len(diff_keys) > 0:
        print(u'新包比老包少的%s(%s个):' % (desc, len(diff_keys)))
        for k in diff_keys:
            print('\t%s : %s' % (k, old_config[k]))

    ##打印新包比老包不一致的key
    same_keys = set(old_config.keys()) & set(new_config.keys())
    for k in same_keys:
        if new_config[k] != old_config[k]:
            tmp_list.append(k)
    if len(tmp_list) > 0:
        print(u'新包比老包不一致的%s(%s个):' % (desc, len(tmp_list)))
        for k in tmp_list:
            print('\t%s :\n\t\t新包: %s\n\t\t老包: %s' % (k, new_config[k], old_config[k]))
    return 0

def main(old_file, new_file):
    """
    主函数
    """
    old_dic = get_config(old_file)
    new_dic = get_config(new_file)

    old_config = old_dic.get('others')
    old_config_requires = old_dic.get('requires')
    old_config_provides = old_dic.get('provides')

    new_config = new_dic.get('others')
    new_config_requires = new_dic.get('requires')
    new_config_provides = new_dic.get('provides')

    ##打印除provides、requires外不同的配置
    diff(old_config, new_config)

    ##比对新、老包的provides
    diff(old_config_provides, new_config_provides, 'provides')

    ##比对新、老包的requires
    diff(old_config_requires, new_config_requires, 'requires')



if __name__ == '__main__':
    main(old_file, new_file)