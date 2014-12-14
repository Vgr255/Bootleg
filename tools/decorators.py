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
                    if not cmd in generator.keys():
                        generator[cmd] = []
                    generator[cmd].append(fetch)
                    if alias:
                        fetch.aliases.append(cmd)
                    alias = True
                for arg, value in kwargs.items():
                    setattr(fetch, arg, value)
                fetch.id = id

                return fetch

            for arg, value in defargs.items():
                if not arg in kwargs.keys():
                    kwargs.update({arg:value})

            for kw in kwargs:
                if not kw in defargs:
                    raise ValueError(kw)

            return decorate

        return parse

    return create

def delete(generator, id):
    for cmd in list(generator.keys()):
        for x in list(generator[cmd]):
            if x.id == id:
                generator[cmd].remove(x)
        if not generator[cmd]:
            del generator[cmd]
