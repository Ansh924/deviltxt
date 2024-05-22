#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7121739297:AAG7ADpO1TJs1IGGVBA_zNrqmvMUpTf6JHI")
    API_ID = int(os.environ.get("API_ID", "26945844"))
    API_HASH = os.environ.get("API_HASH", "9f2f1d81fd2af2b21a700fa6681215b1")
