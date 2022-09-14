#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2022 Intel Corporation
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
# SPDX-License-Identifier: EPL-2.0
#

import os
import tensorflow as tf

from tlt.models.tf_model import TFModel
from tlt.utils.types import FrameworkType, UseCaseType


class TFHubModel(TFModel):
    """
    Base class used to represent a TF Hub pretrained model
    """

    def __init__(self, model_url: str,  model_name: str, framework: FrameworkType, use_case: UseCaseType):
        self._model = None
        self._model_url = model_url
        super().__init__(model_name, framework, use_case)

    @property
    def model_url(self):
        """
        The public URL used to download the TFHub model
        """
        return self._model_url

