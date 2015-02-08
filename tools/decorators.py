# Decorators generator for various purposes
# Code based on jcao219's decorator generator. Heavily modified

def generate(arguments=True, **defargs):
    def create(generator, id=-1, **secargs):
        def decorate(*cmds, arguments=arguments, id=id, **kwargs):
            def parser(dec):
                def fetch(*nargs, **kwnargs):
                    if not arguments:
                        return dec()
                    return dec(*nargs, **kwnargs)
                alias = False
                fetch.aliases = []
                for cmd in cmds:
                    if cmd not in generator:
                        generator[cmd] = []
                    generator[cmd].append(fetch)
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

            for arg, value in secargs.items():
                if not arg in kwargs.keys():
                    kwargs[arg] = value

            for kw in kwargs:
                if not kw in defargs:
                    raise ValueError(kw)

            return parser

        if not isinstance(generator, dict):
            raise TypeError("generator object must be a dict")

        for arg, value in defargs.items():
            if not arg in secargs.keys():
                secargs[arg] = value

        return decorate

    return create

def delete(generator, id):
    if not isinstance(generator, dict):
        raise TypeError("generator object must be a dict")
    for cmd in list(generator.keys()):
        for item in list(generator[cmd]):
            if item.id == id:
                generator[cmd].remove(item)
            if not generator[cmd]:
                del generator[cmd]
