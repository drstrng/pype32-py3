#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# Copyright (c) 2015, Sandor Nemes
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#     * Redistributions of source code must retain the above copyright notice,
#       this list of conditions and the following disclaimer.
#     * Redistributions in binary form must reproduce the above copyright
#       notice,this list of conditions and the following disclaimer in the
#       documentation and/or other materials provided with the distribution.
#     * Neither the name of the copyright holder nor the names of its
#       contributors may be used to endorse or promote products derived from
#       this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE
# LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE
# POSSIBILITY OF SUCH DAMAGE.
import bisect

caches = {}

class Cache(object):

    def __init__(self, name):
        self.name = name
        self.cache = {}
        self.sorted_keys = []

    def get(self, key):
        result = self.cache.get(key)
        if result is None and len(self.sorted_keys) > 1:
            # .net may point strings inside other strings, but
            # the cache only uses the start of strings so check
            # if this key can be part of another str/bytes value
            idx = bisect.bisect_left(self.sorted_keys, key)
            if idx > 0:
                cache_key = self.sorted_keys[idx - 1]
                offset = key - cache_key
                if offset > 0:
                    result = self.cache.get(cache_key)
                    if result is not None and len(result) > offset:
                        result = result[offset:]
                        self.put(key, result)
        return result

    def put(self, key, value):
        if key not in self.cache and (
            isinstance(value, str) or isinstance(value, bytes)
        ):
            # For strs/bytes keep a sorted list of keys (usually their offsets in .net heaps)
            bisect.insort(self.sorted_keys, key)
        self.cache.update({ key: value })

def getCache(name):
    cache = caches.get(name)
    if cache is None:
        cache = Cache(name)
        caches[name] = cache
    return cache

def cached(*ids):
    def decorator(func):
        def decorated(self, *args):
            funcname = "#".join([func.__name__] + [str(_) for _ in ids])
            cache = getCache(funcname)
            key = hash(args)
            result = cache.get(key)
            if result is None:
                result = func(self, *args)
                cache.put(key, result)
            return result
        return decorated
    return decorator
