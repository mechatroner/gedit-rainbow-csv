#==============================================================================
#  Description: rainbow csv
#               by Dmitry Ignatovich
#==============================================================================

from gi.repository import GObject, Gedit, GtkSource


def lines_are_delimited(lines, delim):
    if not len(lines):
        return False
    nf = len(lines[0].split(delim))
    if nf < 2:
        return False
    for l in lines:
        if len(l.split(delim)) != nf:
            return False
    return True

delim_types = {'\t' : 'tsv', ',' : 'csv'}

def get_delimiter(window):
    doc = window.get_active_document()
    if not doc:
        return None
    nlines = doc.get_line_count()
    if nlines < 5:
        return None
    start = doc.get_start_iter()
    end = doc.get_end_iter() if nlines < 10 else doc.get_iter_at_line(10)
    head_text = str(doc.get_text(start, end, True))
    lines = head_text.splitlines()
    for delim in delim_types.keys():
        if lines_are_delimited(lines, delim):
            return delim
    return None


class ExamplePyWindowActivatable(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "RainbowCsvLoader"
    name = __gtype_name__

    window = GObject.property(type=Gedit.Window)


    def do_activate(self):
        handler_id = self.window.connect("tab-added", self.on_tab_added)
        self.window.rbcsv_handler = handler_id
        for doc in self.window.get_documents():
            self.connect_document(doc)

    def do_deactivate(self):
        if hasattr(self.window, 'rbcsv_handler'):
            handler_id = self.window.rbcsv_handler
            self.window.disconnect(handler_id)

    def do_update_state(self):
        pass

    def on_tab_added(self, window, tab):
        doc = tab.get_document()
        self.connect_document(doc)

    def connect_document(self, doc):
        handler_id = doc.connect("loaded", self.on_document_load)
        doc.rbcsv_handler = handler_id

    def on_document_load(self, doc, *args):
        delim = get_delimiter(self.window)
        if delim is not None:
            lang_name = delim_types[delim]
            lang = GtkSource.LanguageManager.get_default().get_language(lang_name)
            doc.set_language(lang)

