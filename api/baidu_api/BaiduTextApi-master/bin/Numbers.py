#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import base64
import requests
from .AccessToken import AccessToken
from .config import LOCALHOST_PATH, URL_LIST_URL

ACCESS_TOKEN = AccessToken().getToken()['access_token']

NUMBERS_URL = URL_LIST_URL['NUMBERS'] + '?access_token={}'.format(ACCESS_TOKEN)


class NumbersSuper(object):
    pass


class Numbers(NumbersSuper):

    def __init__(self, image=None, recognize_granularity='small', detect_direction=True):
        self.HEADER = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        self.IMAGE_CONFIG = {
            'recognize_granularity': recognize_granularity,
            'detect_direction': detect_direction
        }

        if image is not None:
            imagepath = os.path.exists(LOCALHOST_PATH['PATH'] + image)
            if imagepath == True:
                images = LOCALHOST_PATH['PATH'] + image
                with open(images, 'rb') as images:
                    self.IMAGE_CONFIG['image'] = base64.b64encode(images.read())

    def postNumbers(self):
        if self.IMAGE_CONFIG.get('image', None) == None:
            return 'image参数不能为空!'
        numbers = requests.post(url=NUMBERS_URL, headers=self.HEADER,
                                data=self.IMAGE_CONFIG)
        return numbers.text
