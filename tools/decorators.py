# Decorators generator for various purposes

class DecoratorsGenerator:
    def __init__(self, arguments=True, **defargs):
        self.arguments = arguments
        self.defargs = {}
        for arg, value in defargs.items():
            self.defargs[arg] = value

    def __call__(self, generator, id=-1, **secargs):
        def generate(*cmds, arguments=self.arguments, id=id, **kwargs):
            def create(dec):
                def decorate(*nargs):
                    if not arguments:
                        return dec()
                    return dec(*nargs)
                alias = False
                decorate.aliases = []
                for cmd in cmds:
                    generator[cmd] = decorate
                    if alias:
                        decorate.aliases.append(cmd)
                    alias = True
                for arg, value in kwargs.items():
                    setattr(decorate, arg, value)
                decorate.id = id
                decorate.__doc__ = dec.__doc__

                return decorate

            if not cmds:
                raise ValueError("no commands were specified")

            for arg, value in secargs.items():
                if not arg in kwargs.keys():
                    kwargs.update({arg:value})

            for kw in kwargs:
                if not kw in self.defargs:
                    raise ValueError(kw)

            return create

        if not isinstance(generator, dict):
            raise TypeError("generator object must be a dict")

        for arg, value in self.defargs.items():
            if not arg in secargs.keys():
                secargs.update({arg:value})

        return generate

def delete(generator, id):
    if not isinstance(generator, dict):
        raise TypeError("generator object must be a dict")
    for cmd in list(generator.keys()):
        if generator[cmd].id == id:
            del generator[cmd]
