# Decorators generator for various purposes
# Code based on jcao219's decorator generator. Heavily modified

def generate(**defargs):
    def create(generator, **secargs):
        def decorate(*cmds, **kwargs):
            def parser(dec):
                def fetch(*nargs, **kwnargs):
                    if not kwargs["arguments"]:
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
                fetch.__doc__ = dec.__doc__

                return fetch

            if not cmds:
                raise ValueError("no commands were specified")

            secargs["id"] = secargs.get("id")

            for arg, value in secargs.items():
                kwargs[arg] = kwargs.get(arg, value)

            if not set(kwargs) ^ {"id"} <= set(defargs):
                raise ValueError("arguments must be defined in default")

            return parser

        defargs["arguments"] = defargs.get("arguments", True)

        for arg, value in defargs.items():
            secargs[arg] = secargs.get(arg, value)

        return decorate

    return create

def delete(generator, id):
    if id is None:
        raise ValueError("cannot unassign permanent values")
    for cmd in list(generator.keys()):
        for item in list(generator[cmd]):
            if item.id == id:
                generator[cmd].remove(item)
            if not generator[cmd]:
                del generator[cmd]
