#!/usr/bin/python3
#distribute archives to web servers

def deploy():
    """distribute archives"""
    pack = do_pack()
    if !pack:
        return False
    else:
        is_true = do_deploy(pack)
        return is_true
