# Decorators generator for various purposes

def generate(generator, arguments=True, **defargs):
    def create(*cmds, id=-1, arguments=arguments, **kwargs):
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

            return fetch

        for arg, value in defargs.items():
            if not arg in kwargs.keys():
                kwargs.update({arg:value})

        return decorate

    return create

def delete(generator, id):
    for cmd in list(generator.keys()):
        for x in generator[cmd]:
            if x.id == id:
                generator[cmd].remove(x)
        if not generator[cmd]:
            del generator[cmd]