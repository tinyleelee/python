# coding:utf-8
import requests,json
import urllib.request
import re,os
def getHtml(i): #获取每个专辑地址
    headers ={
        "Host": "wx-1.dengtacourse.com",
        "Content-Type": "application/x-www-form-urlencoded",
        "anonymousId": "B08F4C2E-2FDB-4F2A-BF5D-9564149ECD07",
        "Authorization": "a465a295a95e983bc932e040f3862b8230ddfa61a3decfb77c23fb79218def0765eefba745b82fb52138935863d6400621170f65a60a03102b5686c762552ce6a34dd412772987277328bb6c90da91d4bb143004caa2a27ae1725124b04eca1595a1c725eb46ff37ccc39332d4c97e98",
        "Accept": "*/*",
        "osType": "IOS",
        "appVersionCode":"19300",
        "wxApptype":"35",
        "appVersion": "1.10.0",
        "Accept-Language": "zh-Hans-HK;q=1, zh-Hant-HK;q=0.9, yue-Hant-HK;q=0.8",
        "Accept-Encoding": "gzip, deflate, br",
        "deviceType": "iPhoneX",
        "deviceId": "23818371777938",
        "tourist": "0",
        "User-Agent": "Mozilla/5.0",
        "Content-Length": "33",
        "Connection": "keep-alive",
        "osVersion": "14.2",
    }
    url = "http://wx-1.dengtacourse.com/dengta/app/getSectionListNewV2.json"
    datas = "courseId=%s&imageVersion=_banner" % i

    html = requests.post(url,data=datas,headers = headers,verify = False).json()
    return  html


def getMp4(html): #获取专辑、视频地址和名称&下载
    if str(html) == None:
        pass
    else:
        global i
        ablum = re.findall(str(r"'courserName': '([\s\S]+?)'"), str(html))
        print(ablum[0])
        lessontitle = re.findall(str(r"'title': '([\s\S]+?)'"), str(html))
        mp4url = re.findall(str(r"'videoUrl': '([\s\S]+?)'"), str(html))
        print (mp4url)
        pictureurl = re.findall(str(r"'coverUrl': '([\s\S]+?)'"), str(html))

        folder_name = '%s'%ablum[0] #专辑文件名
        root_directory = 'D:\Download\\%s'%(str(i)+folder_name)
        try:                       #创建文件夹
            os.mkdir(root_directory)
        except OSError:
            pass

        for j in range(len(lessontitle)):
            print(lessontitle[j], mp4url[j])
            f = urllib.request.urlopen(mp4url[j])
            p = urllib.request.urlopen(pictureurl[j])
            data = f.read()
            data1 = p.read()
            lj = str(lessontitle[j]).replace(u"\\xa0", u"")
            file_path = r'D:\Download\%s\%s.mp4' % ((str(i) + folder_name), (lj))
            pic_path = r'D:\Download\%s\%s.png' % ((str(i) + folder_name), (lj))
            with open(file_path, "wb") as code:
                try:
                    code.write(data)
                except OSError:
                    pass
            with open(pic_path, "wb") as code:
                try:
                    code.write(data1)
                except OSError:
                    pass
i = 138
print('课程id:%s下载中...'% i)
html = getHtml(i)
getMp4(html)
