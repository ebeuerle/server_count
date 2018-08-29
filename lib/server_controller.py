import math
import cloudpassage


class ServerController(object):
    def __init__(self, config):
        session = cloudpassage.HaloSession(config.halo_key,
                                           config.halo_secret,
                                           api_host=config.halo_url)
        self.request_obj = cloudpassage.HttpHelper(session)

    def get_servers(self,mots_name):
        endpoint = "/v1/servers?state=active&per_page=100&group_name=%s" % mots_name
        server_list = self.request_obj.get(endpoint)
        return server_list["count"]
