import sublime, sublime_plugin, os

class ExpandTabsOnSave(sublime_plugin.EventListener):
    """Run ST's 'expand_tabs' command when saving a file."""

    def on_pre_save(self, view):
        if view.settings().get('expand_tabs_on_save') == 1:
            view.window().run_command('expand_tabs')
