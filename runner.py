#!/usr/bin/env python
# -*- coding: utf-8 -*-
import lib

class HaloServer_list():
    def __init__(self):
        self.output = [["Mots name", "Number of servers"]]
        config = lib.ConfigHelper()
        self.srv_list = lib.ServerController(config)
        self.file_read = lib.FileController()
        self.count = 0

    def build(self):
        self.read_mots = self.file_read.load_mots_file()
        for mot in self.read_mots:
            self.count = self.srv_list.get_servers(mot)
            self.output.append([mot,self.count])



    def run(self):
        self.build()
        #for server in self.list_server:
        #    self.output.append([server["id"], server["hostname"], server["server_label"], server["primary_ip_address"], server["group_name"], server["state"], server["last_state_change"]])
        lib.CsvWriter.write(self.output)

def main():
    halo_servers = HaloServer_list()
    halo_servers.run()

if __name__ == "__main__":
    main()
