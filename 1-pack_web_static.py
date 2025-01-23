#!/usr/bin/python3
"""fabric script to generate .tgz archive"""

from fabric.api import *
if __name__ == "__main__":
    def do_pack():
        """function to pack contents"""
        result = local("tar -czf versions/webstatic_${date +%Y%m%d%H%M%S}.tgz /data/web_static")
        if result.succeeded:
            archive_path = "/data/web_static/versions/webstatic_" + result.stdout.strip() + ".tgz"
            return archive_path
        else:
            return None
