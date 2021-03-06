#
# -*- coding: utf-8 -*-
#
# This file is part of reclass (http://github.com/madduck/reclass)
#
# Copyright © 2007–14 martin f. krafft <madduck@madduck.net>
# Released under the terms of the Artistic Licence 2.0
#
import os, sys
from version import RECLASS_NAME

# defaults for the command-line options
OPT_STORAGE_TYPE = 'yaml_fs'
OPT_INVENTORY_BASE_URI = os.path.join('/etc', RECLASS_NAME)
OPT_NODES_URI = 'nodes'
OPT_CLASSES_URI = 'classes'
OPT_PRETTY_PRINT = True
OPT_NO_REFS = False
OPT_OUTPUT = 'yaml'

CONFIG_FILE_SEARCH_PATH = [os.getcwd(),
                           os.path.expanduser('~'),
                           OPT_INVENTORY_BASE_URI,
                           os.path.dirname(sys.argv[0])
                          ]
CONFIG_FILE_NAME = RECLASS_NAME + '-config.yml'

REFERENCE_SENTINELS = ('${', '}')
EXPORT_SENTINELS = ('$[', ']')
PARAMETER_INTERPOLATION_DELIMITER = ':'
PARAMETER_DICT_KEY_OVERRIDE_PREFIX = '~'
ESCAPE_CHARACTER = '\\'

MERGE_ALLOW_SCALAR_OVER_DICT = False
MERGE_ALLOW_SCALAR_OVER_LIST = False
MERGE_ALLOW_LIST_OVER_SCALAR = False
MERGE_ALLOW_DICT_OVER_SCALAR = False

AUTOMATIC_RECLASS_PARAMETERS = True
