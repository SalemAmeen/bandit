# -*- coding:utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

import bandit
from bandit.core.test_properties import *


@takes_config
@checks('Str')
def hardcoded_tmp_directory(context, config):
    if (config is not None and 'tmp_dirs' in config):
        tmp_dirs = config['tmp_dirs']
    else:
        tmp_dirs = ['/tmp', '/var/tmp', '/dev/shm']

    if any(context.string_val.startswith(s) for s in tmp_dirs):
        return bandit.Issue(
            severity=bandit.MEDIUM,
            confidence=bandit.MEDIUM,
            text="Probable insecure usage of temp file/directory."
        )
