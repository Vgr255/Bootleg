# Decorators generator for various purposes

def generate(arguments=True, **defargs):
    def create(generator, id=-1):
        def parse(*cmds, arguments=arguments, id=id, **kwargs):
            def decorate(dec):
                def fetch(*nargs):
                    if not arguments:
                        return dec()
                    return dec(*nargs)
                alias = False
                fetch.aliases = []
                for cmd in cmds:
                    generator[cmd] = fetch
                    if alias:
                        fetch.aliases.append(cmd)
                    alias = True
                for arg, value in kwargs.items():
                    setattr(fetch, arg, value)
                fetch.id = id
                fetch.__doc__ = dec.__doc__

                return fetch

            if not cmds:
                raise ValueError("no commands were specified")

            for arg, value in defargs.items():
                if not arg in kwargs.keys():
                    kwargs.update({arg:value})

            for kw in kwargs:
                if not kw in defargs:
                    raise ValueError(kw)

            return decorate

        if not isinstance(generator, dict):
            raise TypeError("generator object must be a dict")

        return parse

    return create

def delete(generator, id):
    if not isinstance(generator, dict):
        raise TypeError("generator object must be a dict")
    for cmd in list(generator.keys()):
        if generator[cmd].id == id:
            del generator[cmd]
