# SPDX-Copyright: Copyright (c) FCON
# SPDX-License-Identifier: Apache-2.0
# Copyright 2018 FCON
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

import os
from setuptools import setup

CURR_DIR = os.path.abspath(os.path.dirname(__file__))

with open(os.path.join(CURR_DIR, "README.rst"), encoding="utf-8") as file_open:
    LONG_DESCRIPTION = file_open.read()

exec(open("vficredit/_version.py").read())

setup(
    name="vficredit",
    version=__version__,
    description="VFI solver for economies with credit defaults",
    long_description=LONG_DESCRIPTION,
    url="https://github.com/f-con/vfi-credit",
    author="FCON",
    author_email="s@fcon.xyz",
    license="Apache Software License",
    packages=["vficredit"],
    zip_safe=False,
)