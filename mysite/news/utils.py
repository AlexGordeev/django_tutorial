class MyMixin(object):
    mixin_prop = ''

    def get_prop(self) -> str:
        return self.mixin_prop.upper()

    def get_upper(self, string: str) -> str:
        return string.upper()
