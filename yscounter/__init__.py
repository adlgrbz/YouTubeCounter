#!/usr/bin/python3

import asyncio
from .gui import YSCounter


def run_tk(async_loop):
    root = YSCounter()
    root.mainloop()


async_loop = asyncio.get_event_loop()
run_tk(async_loop)
