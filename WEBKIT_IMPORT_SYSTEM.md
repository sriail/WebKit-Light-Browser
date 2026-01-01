# WebKit Import System

## Overview

This browser uses modern **WebKitGTK 6.0** accessed through Python via **PyGObject**.

## Import Structure

### 1. Import PyGObject
```python
import gi
```

### 2. Set Version Requirements
```python
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit', '6.0')
```

### 3. Import Modules
```python
from gi.repository import Gtk, WebKit, GLib
```

## Key Components

### WebView Widget
```python
webview = WebKit.WebView()
```

The `WebKit.WebView` widget renders web content and can be embedded in any GTK application.

### Load Events
```python
webview.connect("load-changed", callback)
```

WebKit provides load progress tracking:
- `WebKit.LoadEvent.STARTED`
- `WebKit.LoadEvent.REDIRECTED`
- `WebKit.LoadEvent.COMMITTED`
- `WebKit.LoadEvent.FINISHED`

### Navigation Methods
- `load_uri(url)` - Load a URL
- `go_back()` - Navigate back
- `go_forward()` - Navigate forward
- `reload()` - Reload page
- `get_uri()` - Get current URL

## Installation

### Ubuntu/Debian
```bash
sudo apt-get install python3-gi gir1.2-gtk-3.0 gir1.2-webkit-6.0
```

### Fedora
```bash
sudo dnf install python3-gobject gtk3 webkit2gtk
```

### Arch Linux
```bash
sudo pacman -S python-gobject gtk3 webkit2gtk
```

## Testing

```bash
python3 test_imports.py
```

## References

- [WebKitGTK Documentation](https://webkitgtk.org/reference/webkit2gtk/stable/)
