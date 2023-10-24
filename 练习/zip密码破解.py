from zipfile import ZipFile
import os

def passwd(path,pw):
    type_ = os.path.splitext(path)[-1][1:]
    if type_ == 'zip':
        with ZipFile(path,'r') as zip:
            try:
                zip.extractall('./tools/',pwd=pw.encode('utf-8'))
                print(pw)
                return True
            except Exception as e:
                pass

def creat_pwd():
    import itertools as its

    words = '0123456789zqawsxedcrfvtgbyhnujmiklopQAZWSXEDCRFVTGBYHNUJMIKLOP~!@#$%^&*()_+{}[]|'
    base = its.product(words,repeat=8)
    for i in base:
        yield ''.join(i)


if __name__ == '__main__':
    for i in creat_pwd():
        flag = passwd('./content.html.zip',i)
        if flag:
            print(i)
            break

