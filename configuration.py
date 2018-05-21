class ConfigAttribute():

    def __init__(self, name, attr_type, default=None):

        self._name = name

        self._type = attr_type

        self._default = default if default else attr_type()


    @property
    def attr_name(self):

        return '_' + self._name


    def __get__(self, instance, cls):

        return getattr(instance, self.attr_name, self._default)


    def __set__(self, instance, value):

        if not isinstance(value, self._type):

            raise TypeError('Wtong attribute type, it should be %s' % self._type) 

        setattr(instance, self.attr_name, value)


class ConfigMetaclass(type):

    def __new__(cls, clsname, bases, clsdict):

        cls.__instance = None

        return type.__new__(cls, clsname, bases, clsdict)


    def __call__(self, *args, **kwargs):

        if not self.__instance:

            self.__instance = super(ConfigMetaclass, self).__call__(*args, **kwargs)

        return self.__instance
        