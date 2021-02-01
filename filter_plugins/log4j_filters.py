# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type


def log4j_escape(str):
    """Escape string to avoid jinja2 special characters

    Args:
        str (string): string to espace

    Returns:
        string: string escaped
    """
    wrapped = "{% raw %}" + str + "{% endraw %}"
    return wrapped


class FilterModule(object):
    """Ansible docker_presets filters."""

    def filters(self):
        return {
            'log4j_escape': log4j_escape
        }
