#!/usr/bin/env python
#
# Copyright (c) 2015 Intel Corporation.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
# * Redistributions of works must retain the original copyright notice, this
#   list of conditions and the following disclaimer.
# * Redistributions in binary form must reproduce the original copyright
#   notice, this list of conditions and the following disclaimer in the
#   documentation and/or other materials provided with the distribution.
# * Neither the name of Intel Corporation nor the names of its contributors
#   may be used to endorse or promote products derived from this work without
#   specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY INTEL CORPORATION "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL INTEL CORPORATION BE LIABLE FOR ANY DIRECT,
# INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING,
# BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE,
# DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING
# NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE,
# EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
#
# Authors:
#         Liu, Yun <yunx.liu@intel.com>

import unittest
import os
import comm
from xml.etree import ElementTree
import json


class TestCrosswalkApptoolsFunctions(unittest.TestCase):

    def test_start_url_https(self):
        comm.setUp()
        comm.create(self)
        os.chdir(comm.TEST_PROJECT_COMM)
        jsonfile = open(comm.TEMP_DATA_PATH + comm.TEST_PROJECT_COMM + "/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["start_url"] = "https://www.baidu.com"
        json.dump(jsonDict, open(comm.TEMP_DATA_PATH + comm.TEST_PROJECT_COMM + "/app/manifest.json", "w"))
        buildcmd = "crosswalk-app build"
        buildstatus = os.system(buildcmd)
        comm.run(self)
        comm.cleanTempData(comm.TEST_PROJECT_COMM)
        self.assertEquals(buildstatus, 0)

    def test_start_url_noexist(self):
        comm.setUp()
        comm.create(self)
        os.chdir(comm.TEST_PROJECT_COMM)
        jsonfile = open(comm.TEMP_DATA_PATH + comm.TEST_PROJECT_COMM + "/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["start_url"] = "http://www.noexist.com"
        json.dump(jsonDict, open(comm.TEMP_DATA_PATH + comm.TEST_PROJECT_COMM + "/app/manifest.json", "w"))
        buildcmd = "crosswalk-app build"
        buildstatus = os.system(buildcmd)
        comm.run(self)
        comm.cleanTempData(comm.TEST_PROJECT_COMM)
        self.assertEquals(buildstatus, 0)

    def test_start_url_blank(self):
        comm.setUp()
        comm.create(self)
        os.chdir(comm.TEST_PROJECT_COMM)
        jsonfile = open(comm.TEMP_DATA_PATH + comm.TEST_PROJECT_COMM + "/app/manifest.json", "r")
        jsons = jsonfile.read()
        jsonfile.close()
        jsonDict = json.loads(jsons)
        jsonDict["start_url"] = ""
        json.dump(jsonDict, open(comm.TEMP_DATA_PATH + comm.TEST_PROJECT_COMM + "/app/manifest.json", "w"))
        buildcmd = "crosswalk-app build"
        buildstatus = os.system(buildcmd)
        comm.run(self)
        comm.cleanTempData(comm.TEST_PROJECT_COMM)
        self.assertEquals(buildstatus, 0)

if __name__ == '__main__':
    unittest.main()
