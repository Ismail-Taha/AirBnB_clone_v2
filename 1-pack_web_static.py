#!/usr/bin/python3
"""
Fabric script to genereate tgz archive
execute: fab -f 1-pack_web_static.py do_pack
"""

from datetime import datetime
from fabric.api import *


def do_pack():
    """
    making an archive on web_static folder
    """

    curr_time = datetime.now()
    archive_fn = 'web_static_' + curr_time.strftime("%Y%m%d%H%M%S") + '.' + 'tgz'
    local('mkdir -p versions')
    tar_create = local('tar -cvzf versions/{} web_static'.format(archive_fn))
    if tar_create is not None:
        return archive_fn
    else:
        return None
