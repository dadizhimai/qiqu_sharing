#!/usr/bin/env python
import os
import sys
# import django
#
# django.setup()
reload(sys)
sys.setdefaultencoding("utf-8")

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "qiqu_sharing.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)


"""
USER:admin
PASSWROD:admin@123
"""