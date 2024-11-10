class ReadonlyViewMixin:
    read_only_fields = []

    def make_fields_readonly(self):
        for field in self.read_only_fields:
            if field in self.fields:
                self.fields[field].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()

