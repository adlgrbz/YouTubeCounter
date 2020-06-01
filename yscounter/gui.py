import json
import serial
import asyncio
import aiohttp
from os import path
import tkinter as tk
from tkinter import ttk
import subprocess as sub
from bs4 import BeautifulSoup
from serial.tools import list_ports


__version__ = "2.0.0"
__author__ = "Adil Gürbüz"
__contact__ = "adlgrbz@tutamail.com"
__source__ = "https://github.com/adlgrbz/yscounter"

this_dir, this_filename = path.split(__file__)


class YSCounter(tk.Tk):
    def __init__(self):
        super().__init__()
        self._init_window()

        self.line = 0
        self.is_send = False

        self.url = "https://socialblade.com/youtube/channel/"
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0;) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4086.0 Safari/537.36"
        }

        self.port = serial.Serial()
        self.config = self.get_config()

        lf = tk.LabelFrame(padx=5, pady=5)
        lf.pack(pady=(0, 5), fill=tk.BOTH)

        _ = tk.PhotoImage(file=f"{this_dir}/data/icon.gif")
        self.icon = _

        self.tk.call("wm", "iconphoto", self._w, _)

        ttk.Button(lf, image=_, command=self.about).grid(
            row=0, rowspan=2, column=0, padx=(0, 15), sticky=tk.W,
        )

        ttk.Label(lf, text="YouTube Channel ID:").grid(
            row=0, column=1, sticky=tk.W
        )

        self.channel_id = ttk.Entry(lf)
        self.channel_id.grid(row=0, column=2, padx=5)

        self.channel_id.insert(0, self.config["channel_id"])

        ttk.Label(lf, text="Arduino Port Name:").grid(
            row=1, column=1, sticky=tk.W
        )

        self.port_name = ttk.Combobox(lf)
        self.port_name.config(
            values=[p.device for p in list(list_ports.comports())], width=10
        )

        try:
            self.port_name.set(self.port_name["values"][0])
        except IndexError:
            pass

        self.port_name.grid(row=1, column=2, padx=5, sticky=tk.W + tk.E)

        self.output_text = tk.Text()
        self.output_text.config(
            fg="#E34C00",
            bg="#000000",
            width=50,
            height=10,
            padx=5,
            pady=5,
            relief=tk.FLAT,
            state=tk.DISABLED,
        )
        self.output_text.pack(pady=(0, 5), fill=tk.BOTH, expand=1)

        ttk.Button(
            text="Build & Upload Code", command=self.build_and_upload_code
        ).pack(padx=(0, 5), side=tk.LEFT)

        ttk.Button(text="Tested", command=self.tested).pack(
            padx=(0, 5), side=tk.LEFT,
        )

        self.switch = ttk.Button(text="Send", command=self.switch)
        self.switch.pack(
            padx=(0, 5), side=tk.LEFT,
        )

        ttk.Button(text="Clear Log", command=self.clear_log).pack(side=tk.LEFT,)

    def _init_window(self) -> None:
        self.title("YSCounter")
        self.config(padx=5, pady=5)

        self.style = ttk.Style()
        self.style.theme_use("clam")

        self.minsize(
            self.winfo_screenmmwidth(), self.winfo_screenmmheight(),
        )

    def task(self):
        if len(self.channel_id.get()) <= 0:
            self._insert(f"[Warning] Missing entry...\n{51*'='}\n")
            return

        loop = asyncio.get_event_loop()
        loop.run_until_complete(self.get_subscribe_count())

    async def get_subscribe_count(self) -> None:
        async with aiohttp.ClientSession(headers=self.headers) as session:
            async with session.get(
                url=self.url + self.channel_id.get() + "/realtime", ssl=False
            ) as r:
                self.status = r.status
                text = await r.text()

        soup = BeautifulSoup(text, "html.parser")
        subs = soup.find_all("p", {"id": "rawCount"})

        self.data = subs[0].string

    def build_and_upload_code(self) -> None:
        self.output_text["state"] = tk.NORMAL
        command = f"ino build && ino upload -p /dev/{self.port_name.get()}"
        self._insert(f"[Run] {command}")

        p = sub.Popen(command, stdout=sub.PIPE, stderr=sub.PIPE, shell=True)
        output, errors = p.communicate()

        self._insert(
            (
                f"[Output] {output.decode('utf-8')}"
                f"\n[Errors] {errors.decode('utf-8')}\n"
            )
        )

        self.output_text["state"] = tk.DISABLED

        self.update_idletasks()

    def tested(self) -> None:
        self.task()

        self._insert(
            f"[Info][{self.status}] Number of subscribers: {self.data}\n"
        )

    def switch(self):
        self.is_send = not self.is_send

        self.save_config("channel_id", self.channel_id.get())

        if self.is_send:
            self.switch["text"] = "Stop"
        else:
            self.switch["text"] = "Send"
            self._insert(f"[Info] Stopped!\n")
            self.port.close()

        if self.is_send != True:
            return

        self.update()

    def clear_log(self) -> None:
        self.line = 0

        self.output_text["state"] = tk.NORMAL
        self.output_text.delete(1.0, tk.END)
        self.output_text["state"] = tk.DISABLED

    def update(self):
        if self.is_send != True:
            return

        if self.port.isOpen() != True:
            try:
                self.port = serial.Serial(self.port_name.get(), 9600)
                self._insert(f"[Info] Port is open: {self.port.isOpen()}\n")

            except (OSError, serial.SerialException):
                self._insert(f"[Warning] Port name not found!\n")
                return

        self.task()
        self._insert(f"[{self.line}] Sending {self.data} ...\n")
        self.port.write(str.encode(self.data))

        self.line += 1
        self.output_text.after(1000, self.update)

    def about(self):
        aw = tk.Toplevel()
        aw.title("About")
        aw.resizable(0, 0)
        aw.wm_iconphoto(aw._w, self.icon)

        tk.Label(
            aw,
            text=f"{self.wm_title()} {__version__}",
            compound=tk.LEFT,
            image=self.icon,
            padx=10,
        ).pack(padx=10, pady=5)
        info_text = (
            f"Author: {__author__}\n"
            f"Contact: {__contact__}\n\n"
            f"Source: {__source__}\n\n"
            "Contributors:\n"
            "GizliProfesor (https://github.com/GizliProfesor)"
        )
        tk.Label(aw, text=info_text, padx=5, pady=5, relief=tk.RIDGE).pack()

        ttk.Button(aw, text="Close", command=lambda: aw.destroy()).pack(
            padx=5, pady=5, side=tk.RIGHT
        )

    def get_config(self):
        with open(f"{this_dir}/data/config.json", "r") as file:
            config = json.load(file)

        return config

    def save_config(self, key, value) -> None:
        config = self.get_config()

        config[key] = value

        with open(f"{this_dir}/data/config.json", "w") as file:
            json.dump(config, file)

    def _insert(self, text) -> None:
        self.output_text["state"] = tk.NORMAL
        self.output_text.insert(1.0, text)
        self.output_text["state"] = tk.DISABLED
