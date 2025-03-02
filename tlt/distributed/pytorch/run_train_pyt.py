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

import argparse

from tlt.distributed.pytorch.utils.pyt_distributed_utils import (
    DistributedTorch,
    DistributedTrainingArguments
)


if __name__ == "__main__":

    # Program arguments
    print("******Distributed Training*****")

    description = 'Distributed training with PyTorch.'

    parser = argparse.ArgumentParser(description=description)

    parser.add_argument('--master_addr', type=str, required=True, help="Master node to run this script")
    parser.add_argument('--master_port', type=str, required=True, default='29500', help='Master port')
    parser.add_argument('--backend', type=str, required=False, default='ccl', help='Type of backend to use '
                        '(default: ccl)')
    parser.add_argument('--use_case', type=str, required=True,
                        help='Use case (image_classification|text_classification)')
    parser.add_argument('--epochs', type=int, required=False, default=1, help='Total epochs to train the model')
    parser.add_argument('--batch_size', type=int, required=False, default=128,
                        help='Global batch size to distribute data (default: 128)')
    parser.add_argument('--disable_ipex', action='store_true', required=False, help="Disables IPEX optimization to "
                        "the model")

    args = parser.parse_args()

    # Load the saved dataset and model objects
    loaded_objects = DistributedTorch.load_saved_objects(use_case=args.use_case)

    dataset = loaded_objects['dataset']
    train_subset = loaded_objects.get('train_subset', dataset)
    test_subset = loaded_objects.get('test_subset', dataset)
    validation_subset = loaded_objects.get('validation_subset', dataset)
    model = loaded_objects['model']
    loss = loaded_objects['loss']
    optimizer = loaded_objects['optimizer']

    # Launch distributed job
    training_args = DistributedTrainingArguments(
        dataset=train_subset,
        model=model,
        criterion=loss,
        optimizer=optimizer,
        epochs=args.epochs,
        batch_size=args.batch_size,
        disable_ipex=args.disable_ipex
    )

    dt = DistributedTorch(use_case=args.use_case)
    dt.launch_distributed_job(training_args, args.master_addr, args.master_port, args.backend)
