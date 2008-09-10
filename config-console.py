#!/usr/bin/python

import dialog


class Console:
    def __init__(self, title=None, width=60, height=18):
        self.width = width
        self.height = height

        self.console = dialog.Dialog(dialog="dialog")
        if title:
            self.console.add_persistent_args(["--backtitle", title])

    def msgbox(self, title, text, button_label="ok"):
        return self.console.msgbox(text, self.height, self.width,
                                   title=title, ok_label=button_label)

def _get_hostname():
    return "Drupal"

def _get_ipaddr():
    #return "192.168.0.1"
    return None

def _netstat():
    #todo: check listening ports
    ipaddr = _get_ipaddr()
    if ipaddr:
        info = "Web Browser:  http://%s\n" % ipaddr
        info += "Secure Shell: ssh root@%s\n" % ipaddr
    else:
        info = "Error: Network not configured\n"

    return info

def appname():
    return "Turnkey Linux %s" % _get_hostname()

def infotext(height):
    header = "\nYou may access this %s Appliance over\n" % appname()
    header += "the network using the following methods:\n\n"

    body = _netstat()

    footer = "For more information visit the Turnkey Linux Website\n"
    footer += "             http://www.turnkeylinux.org"

    curlines = header.count('\n') + body.count('\n') + footer.count('\n')
    bodypad = "\n"*(height - 5 - curlines)
    return header + body + bodypad + footer

def main():
    title = "Turnkey Linux Console Configuration"
    width = 60
    height = 18

    console = Console(title, width, height)
    console.msgbox(appname(), infotext(height), button_label="Advanced")

if __name__ == "__main__":
    main()
