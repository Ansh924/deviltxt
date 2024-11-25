#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7756796164:AAHqSqNGycDzOavKymRZ2dYEBQfwvHa3TCM")
    API_ID = int(os.environ.get("API_ID", "25552615"))
    API_HASH = os.environ.get("API_HASH", "b2ae2b696d592e1752304fe8521d0c7f")
