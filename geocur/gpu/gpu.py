#! /usr/bin/python3
# -*- coding: utf-8 -*-
"""GeoCur Programmer's Utilities (GPU)"""
# Filename : gpu.py
# Version  : 0.0.0
# Release  : prototype
# Serial   : b2720d9e-db33-4dd0-8e8c-4aaf185ef7ad
# Created  : 2025.01.19 at 08:50:56
# Modified :
# Author   : G.R.Curtis
# Email    : grcurtis27__at__gmail.com
# ------------------------------ Module Import: ----------------------------- #
# Import Standard Python Libraries:

# Import 3rd-Party Libraries (I try not to use this section):

# Import Custom Libraries:
try:
    import inc.gpu_globals as glo
    if not glo.initdone:
        glo.init_globals(
            **{
                "application": __file__,
                "description": __doc__,
                "version"    : "0.0.0-prototype",
                "copyright"  : "Copyright© 2021-2025, G.R.Curtis",
                "license"    : "MIT",
                "author"     : ["G.R.Curtis",],
                "author_url" : ["",],
                "credits"    : ["G.R.Curtis",],
                "maintainer" : ["G.R.Curtis",],
                "email"      : ["grcurtis27__at__gmail.com",],
            }
        )
except ModuleNotFoundError as mnfe:
    print(f"Error: {mnfe} [gpu]")
    raise SystemExit

# --------------------- Variable & constant defintions: --------------------- #

# ----------------- Class, function & procedure definitions: ---------------- #


def main():
    pass
# End of main() definition.


# ------------------------------- EOF: gpu.py ------------------------------- #
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nprocess aborted by user. exiting...")
    except SystemExit:
        print("exiting...")
    except Exception as ex:
        print(f"Error: {ex}")
    finally:
        print("\nThanks for flying GeoCur!")
