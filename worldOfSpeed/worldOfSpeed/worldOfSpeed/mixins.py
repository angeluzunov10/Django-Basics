class ReadOnlyFieldsMixin:
    readonly_fields = []
    disabled_fields = []

    def make_fields_readonly(self):
        for field_name in self.readonly_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['readonly'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_readonly()


class DisabledFieldsMixin:
    def make_fields_disabled(self):
        for field_name in self.disabled_fields:
            if field_name in self.fields:
                self.fields[field_name].widget.attrs['disabled'] = True

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.make_fields_disabled()
