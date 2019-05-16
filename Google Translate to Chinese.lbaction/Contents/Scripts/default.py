#!/usr/local/anaconda3/bin/python
#
# LaunchBar Action Script
#
import sys
import json
import subprocess as sp
import os
from time import time
from plistlib import load 
from html import unescape

# Copyright 2016 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


def google_translate(text, target):
    # [START translate_quickstart]
    # Imports the Google Cloud client library
    from google.cloud import translate

    # Get API
    info_plist_path = os.path.abspath("../Info.plist")
    with open(info_plist_path, 'rb') as fp:
        LB_SUPPORT_PATH = os.path.expanduser("~/Library/Application Support/LaunchBar/Action Support/")\
                            + load(fp)["CFBundleIdentifier"]+"/"

    # Instantiates a client
    translate_client = translate.Client.from_service_account_json(\
                            LB_SUPPORT_PATH + 'Google_Translate_API.json')
    return translate_client.translate(
        text,
        target_language=target)


zeit = time()
my_env = os.environ.copy()
my_env["PATH"] = "/usr/local/bin:" + my_env["PATH"]

items = []
languages = ["zh"]
# Note: The first argument is the script's path
for arg in sys.argv[1:]:
    for language in languages:
        try:
            content = google_translate(arg, language)
            item = {}
            item["title"] = unescape(content['translatedText'])
            item["subtitle"] = content["detectedSourceLanguage"]\
                               + ": " + content["input"]
            item["icon"] = language+"_flag.png"
        except:
            item = {}
            item["title"] = "Error!"
            item["icon"] = "font-awesome:fa-exclamation-triangle"
        items.append(item)
zeit = time()-zeit
item1 = {}
item1["title"] = str(zeit) + "s"
item1["icon"] = "font-awesome:fa-hourglass-2"
items.append(item1)
print(json.dumps(items))