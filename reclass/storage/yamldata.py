#
# -*- coding: utf-8 -*-
#
# This file is part of reclass (http://github.com/madduck/reclass)
#
# Copyright © 2007–14 martin f. krafft <madduck@madduck.net>
# Released under the terms of the Artistic Licence 2.0
#
from reclass import datatypes
import yaml
import os
from reclass.errors import NotFoundError

class YamlData(object):

    @classmethod
    def from_file(cls, path):
        ''' Initialise yaml data from a local file '''
        if not os.path.isfile(path):
            raise NotFoundError('No such file: %s' % path)
        if not os.access(path, os.R_OK):
            raise NotFoundError('Cannot open: %s' % path)
        y = cls('yaml_fs://{0}'.format(path))
        fp = file(path)
        data = yaml.safe_load(fp)
        if data is not None:
            y._data = data
        fp.close()
        return y

    @classmethod
    def from_string(cls, string, uri):
        ''' Initialise yaml data from a string '''
        y = cls(uri)
        data = yaml.safe_load(string)
        if data is not None:
            y._data = data
        return y

    def __init__(self, uri):
        self._uri = uri
        self._data = dict()

    uri = property(lambda self: self._uri)

    def get_data(self):
        return self._data

    def get_entity(self, name=None):
        classes = self._data.get('classes')
        if classes is None:
            classes = []
        classes = datatypes.Classes(classes)

        applications = self._data.get('applications')
        if applications is None:
            applications = []
        applications = datatypes.Applications(applications)

        parameters = self._data.get('parameters')
        if parameters is None:
            parameters = {}
        parameters = datatypes.Parameters(parameters)

        exports = self._data.get('exports')
        if exports is None:
            exports = {}
        exports = datatypes.Exports(exports)

        if name is None:
            name = self._uri

        env = self._data.get('environment', None)

        return datatypes.Entity(classes, applications, parameters, exports,
                                name=name, environment=env, uri=self.uri)

    def __str__(self):
        return '<{0} {1}, {2}>'.format(self.__class__.__name__, self._uri,
                                       self._data)

    def __repr__(self):
        return '<{0} {1}, {2}>'.format(self.__class__.__name__, self._uri,
                                       self._data.keys())
