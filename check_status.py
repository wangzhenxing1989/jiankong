#!/usr/bin/env python

#import requests
import urllib

def url():
    with open('info_url') as f:
        with open('info_sta','w') as f1:
            st = ''
            for line in f:
                line = line.strip()
                #sta = str(requests.get(line).status_code)
		sta = str(urllib.urlopen(line).getcode())
                st = line+'|'+sta
                f1.write(st+'\n')

    with open('info_sta') as f:
        st = ''
        for line in f:
            url,status = line.strip().split('|')
            if status != '404':
                st = st + url + '\n'
    return st
