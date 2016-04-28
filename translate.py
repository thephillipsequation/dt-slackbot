#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright 2014 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Simple command-line example for Translate.
Command-line application that translates some text.
"""
from __future__ import print_function
import json

__author__ = 'jcgregorio@google.com (Joe Gregorio)'

from googleapiclient.discovery import build




def main():

        def translate(inputString, inLang, outLang):


                # Build a service object for interacting with the API. Visit
                # the Google APIs Console <http://code.google.com/apis/console>
                # to get an API key for your own application.
                service = build('translate', 'v2',
                                                developerKey='AIzaSyCrPl1LCUbBtQjnnJ67UYKUaLp_k5eRqQ8')

                wordArray = inputString.split(' ')
                response = service.translations().list(
                                source=inLang,
                                target=outLang,
                                q=wordArray
                        ).execute()

                translations = response['translations']

                replyString = ''
                for wordDict in translations:
                        replyString = replyString + wordDict['translatedText'] + ' '

                return replyString


        inputString = ''
        outString1 = translate(inputString, 'en', 'fr')
        outString2 = translate(outString1, 'fr', 'de')
        outString3 = translate(outString2, 'de', 'it')
        outString4 = translate(outString3, 'it', 'es')
        outString5 = translate(outString4, 'es', 'en')
        print(outString5)


if __name__ == '__main__':
        main()