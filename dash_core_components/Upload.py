# AUTO GENERATED FILE - DO NOT EDIT

from dash.development.base_component import Component, _explicitize_args


class Upload(Component):
    """A Upload component.


Keyword arguments:
- children (a list of or a singular dash component, string or number | string; optional): Contents of the upload component
- disabled (boolean; optional): Enable/disable the upload component entirely
- style (dict; optional): CSS styles to apply
- multiple (boolean; optional): Allow dropping multiple files
- contents (string | list; optional): The contents of the uploaded file as a binary string
- disable_click (boolean; optional): Disallow clicking on the component to open the file dialog
- accept (string; optional): Allow specific types of files.
See https://github.com/okonet/attr-accept for more information.
Keep in mind that mime type determination is not reliable across
platforms. CSV files, for example, are reported as text/plain
under macOS but as application/vnd.ms-excel under Windows.
In some cases there might not be a mime type set at all.
See: https://github.com/react-dropzone/react-dropzone/issues/276
- id (string; optional): ID of the component. Used to identify component
in Dash callback functions.
- min_size (number; optional): Minimum file size
- className (string; optional): HTML class name of the component
- style_reject (dict; optional): CSS styles if rejected
- style_active (dict; optional): CSS styles to apply while active
- max_size (number; optional): Maximum file size. If `-1`, then infinite
- last_modified (number | list; optional): The last modified date of the file that was uploaded in unix time
(seconds since 1970).
- className_active (string; optional): HTML class name of the component while active
- filename (string | list; optional): The name of the file(s) that was(were) uploaded.
Note that this does not include the path of the file
(for security reasons).
- style_disabled (dict; optional): CSS styles if disabled
- className_reject (string; optional): HTML class name of the component if rejected
- className_disabled (string; optional): HTML class name of the component if disabled

Available events: """
    @_explicitize_args
    def __init__(self, children=None, style_reject=Component.UNDEFINED, min_size=Component.UNDEFINED, style=Component.UNDEFINED, multiple=Component.UNDEFINED, style_disabled=Component.UNDEFINED, className_reject=Component.UNDEFINED, className_disabled=Component.UNDEFINED, accept=Component.UNDEFINED, id=Component.UNDEFINED, disabled=Component.UNDEFINED, className=Component.UNDEFINED, last_modified=Component.UNDEFINED, style_active=Component.UNDEFINED, max_size=Component.UNDEFINED, className_active=Component.UNDEFINED, filename=Component.UNDEFINED, disable_click=Component.UNDEFINED, contents=Component.UNDEFINED, **kwargs):
        self._prop_names = ['children', 'disabled', 'style', 'multiple', 'contents', 'disable_click', 'accept', 'id', 'min_size', 'className', 'style_reject', 'style_active', 'max_size', 'last_modified', 'className_active', 'filename', 'style_disabled', 'className_reject', 'className_disabled']
        self._type = 'Upload'
        self._namespace = 'dash_core_components'
        self._valid_wildcard_attributes =            []
        self.available_events = []
        self.available_properties = ['children', 'disabled', 'style', 'multiple', 'contents', 'disable_click', 'accept', 'id', 'min_size', 'className', 'style_reject', 'style_active', 'max_size', 'last_modified', 'className_active', 'filename', 'style_disabled', 'className_reject', 'className_disabled']
        self.available_wildcard_properties =            []

        _explicit_args = kwargs.pop('_explicit_args')
        _locals = locals()
        _locals.update(kwargs)  # For wildcard attrs
        args = {k: _locals[k] for k in _explicit_args if k != 'children'}

        for k in []:
            if k not in args:
                raise TypeError(
                    'Required argument `' + k + '` was not specified.')
        super(Upload, self).__init__(children=children, **args)

    def __repr__(self):
        if(any(getattr(self, c, None) is not None
               for c in self._prop_names
               if c is not self._prop_names[0])
           or any(getattr(self, c, None) is not None
                  for c in self.__dict__.keys()
                  if any(c.startswith(wc_attr)
                  for wc_attr in self._valid_wildcard_attributes))):
            props_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self._prop_names
                                      if getattr(self, c, None) is not None])
            wilds_string = ', '.join([c+'='+repr(getattr(self, c, None))
                                      for c in self.__dict__.keys()
                                      if any([c.startswith(wc_attr)
                                      for wc_attr in
                                      self._valid_wildcard_attributes])])
            return ('Upload(' + props_string +
                   (', ' + wilds_string if wilds_string != '' else '') + ')')
        else:
            return (
                'Upload(' +
                repr(getattr(self, self._prop_names[0], None)) + ')')
