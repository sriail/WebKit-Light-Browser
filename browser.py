#!/usr/bin/env python3
"""
WebKit Light Browser - A simple web browser using WebKit
"""

import sys
import gi

# Require specific versions
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')

from gi.repository import Gtk, WebKit2, GLib


class BrowserWindow(Gtk.Window):
    """Main browser window class"""
    
    def __init__(self):
        super().__init__(title="WebKit Light Browser")
        self.set_default_size(1024, 768)
        
        # Create main vertical box
        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=0)
        self.add(vbox)
        
        # Create toolbar
        toolbar = self.create_toolbar()
        vbox.pack_start(toolbar, False, False, 0)
        
        # Create WebKit WebView
        self.webview = WebKit2.WebView()
        
        # Create scrolled window for webview
        scrolled_window = Gtk.ScrolledWindow()
        scrolled_window.add(self.webview)
        vbox.pack_start(scrolled_window, True, True, 0)
        
        # Connect signals
        self.connect("destroy", Gtk.main_quit)
        self.webview.connect("load-changed", self.on_load_changed)
        
        # Load default page
        self.webview.load_uri("https://www.google.com")
    
    def create_toolbar(self):
        """Create browser toolbar with navigation controls"""
        toolbar = Gtk.Toolbar()
        
        # Back button
        back_button = Gtk.ToolButton(stock_id=Gtk.STOCK_GO_BACK)
        back_button.connect("clicked", self.on_back_clicked)
        toolbar.insert(back_button, -1)
        
        # Forward button
        forward_button = Gtk.ToolButton(stock_id=Gtk.STOCK_GO_FORWARD)
        forward_button.connect("clicked", self.on_forward_clicked)
        toolbar.insert(forward_button, -1)
        
        # Refresh button
        refresh_button = Gtk.ToolButton(stock_id=Gtk.STOCK_REFRESH)
        refresh_button.connect("clicked", self.on_refresh_clicked)
        toolbar.insert(refresh_button, -1)
        
        # Separator
        separator = Gtk.SeparatorToolItem()
        toolbar.insert(separator, -1)
        
        # URL entry
        self.url_entry = Gtk.Entry()
        self.url_entry.set_placeholder_text("Enter URL...")
        self.url_entry.connect("activate", self.on_url_activate)
        
        # Wrap URL entry in a tool item
        url_item = Gtk.ToolItem()
        url_item.set_expand(True)
        url_item.add(self.url_entry)
        toolbar.insert(url_item, -1)
        
        # Go button
        go_button = Gtk.ToolButton(stock_id=Gtk.STOCK_OK)
        go_button.connect("clicked", self.on_go_clicked)
        toolbar.insert(go_button, -1)
        
        return toolbar
    
    def on_back_clicked(self, widget):
        """Navigate back"""
        self.webview.go_back()
    
    def on_forward_clicked(self, widget):
        """Navigate forward"""
        self.webview.go_forward()
    
    def on_refresh_clicked(self, widget):
        """Reload current page"""
        self.webview.reload()
    
    def on_url_activate(self, widget):
        """Handle URL entry activation (Enter key)"""
        self.load_url()
    
    def on_go_clicked(self, widget):
        """Handle Go button click"""
        self.load_url()
    
    def load_url(self):
        """Load URL from entry field"""
        url = self.url_entry.get_text()
        if url:
            # Add protocol if missing
            if not url.startswith(('http://', 'https://', 'file://')):
                url = 'https://' + url
            self.webview.load_uri(url)
    
    def on_load_changed(self, webview, load_event):
        """Update URL entry when page loads"""
        if load_event == WebKit2.LoadEvent.COMMITTED:
            uri = webview.get_uri()
            if uri:
                self.url_entry.set_text(uri)


def main():
    """Main entry point"""
    # Create and show the browser window
    window = BrowserWindow()
    window.show_all()
    
    # Start GTK main loop
    Gtk.main()


if __name__ == "__main__":
    main()
