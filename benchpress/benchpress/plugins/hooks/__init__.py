#!/usr/bin/env python3
# Copyright (c) 2017-present, Facebook, Inc.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree. An additional grant
# of patent rights can be found in the PATENTS file in the same directory.

from .noop import NoopHook
from .file import FileHook
from .shell import ShellHook


def register_hooks(factory):
    factory.register('noop', NoopHook)
    factory.register('file', FileHook)
    factory.register('shell', ShellHook)
