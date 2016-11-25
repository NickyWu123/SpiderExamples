from proxy import PROXIES, FREE_PROXIES
from agents import AGENTS
import logging as log

import random


class CustomHttpProxyMiddleware(object):

    def process_request(self, request, spider):
        p = random.choice(PROXIES)
        request.meta['proxy'] = "http://%s" % p['ip_port']

class CustomUserAgentMiddleware(object):
    def process_request(self, request, spider):
        agent = random.choice(AGENTS)
        request.headers['User-Agent'] = agent
