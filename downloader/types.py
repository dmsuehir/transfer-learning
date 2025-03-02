#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Intel Corporation
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
# SPDX-License-Identifier: Apache-2.0
#

from enum import Enum, auto


class DatasetType(Enum):
    TENSORFLOW_DATASETS = auto()
    TORCHVISION = auto()
    HUGGING_FACE = auto()
    GENERIC = auto()

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def from_str(dataset_str):
        if dataset_str is None:
            return DatasetType.GENERIC

        dataset_str = dataset_str.lower()

        if dataset_str in ["tfds", "tensorflow", "tensorflow_datasets", "tensorflow datasets", "tensorflow_dataset",
                           "tensorflow dataset"]:
            return DatasetType.TENSORFLOW_DATASETS
        elif dataset_str in ["torchvision"]:
            return DatasetType.TORCHVISION
        elif dataset_str in ["huggingface", "hugging_face", "hugging face"]:
            return DatasetType.HUGGING_FACE
        elif dataset_str in ["generic"]:
            return DatasetType.GENERIC
        else:
            options = [e.name for e in DatasetType]
            raise ValueError("Unsupported dataset type: {} (Select from: {})".format(
                dataset_str, options))


class ModelType(Enum):
    TF_HUB = auto()
    TORCHVISION = auto()
    PYTORCH_HUB = auto()
    HUGGING_FACE = auto()
    KERAS_APPLICATIONS = auto()
    GENERIC = auto()

    def __str__(self):
        return self.name.lower()

    @staticmethod
    def from_str(model_str):
        if model_str is None:
            return ModelType.GENERIC

            model_str = model_str.lower()

        if model_str in ["tfhub", "tf_hub", "tf hub", "tensorflow_hub", "tensorflow hub"]:
            return ModelType.TF_HUB
        elif model_str in ["torchvision"]:
            return ModelType.TORCHVISION
        elif model_str in ["pytorch_hub", "pyt_hub", "torch_hub", "torch hub", "pytorch hub"]:
            return ModelType.PYTORCH_HUB
        elif model_str in ["huggingface", "hugging_face", "hugging face"]:
            return ModelType.HUGGING_FACE
        elif model_str in ["keras", "keras_applications", "keras applications"]:
            return ModelType.KERAS_APPLICATIONS
        elif model_str in ["generic"]:
            return ModelType.GENERIC
        else:
            options = [e.name for e in ModelType]
            raise ValueError("Unsupported model type: {} (Select from: {})".format(model_str, options))
