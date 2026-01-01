# WebKit Import System Documentation

## Overview

This document explains how the WebKit import system is implemented in the WebKit Light Browser application.

## Architecture

The browser uses **WebKit2GTK**, which is the GTK+ port of the WebKit rendering engine. This is accessed through Python using **PyGObject** (Python GObject Introspection bindings).

## Import Structure

### 1. PyGObject Foundation

```python
import gi
```

The `gi` module provides Python bindings for GObject-based libraries through GObject Introspection.

### 2. Version Requirements

```python
gi.require_version('Gtk', '3.0')
gi.require_version('WebKit2', '4.0')
```

These lines explicitly specify which versions of the libraries to use:
- **GTK+ 3.0**: The graphical toolkit for the user interface
- **WebKit2 4.0**: The WebKit2GTK rendering engine API

### 3. Import Modules

```python
from gi.repository import Gtk, WebKit2, GLib
```

This imports the actual modules:
- **Gtk**: GTK+ widgets and UI components
- **WebKit2**: WebKit rendering engine classes and methods
- **GLib**: Core application building blocks

## Key WebKit Components

### WebView Widget

```python
self.webview = WebKit2.WebView()
```

The `WebKit2.WebView` is the main widget that renders web content. It's a GTK widget that can be embedded in any GTK application.

### Load Events

```python
self.webview.connect("load-changed", self.on_load_changed)
```

WebKit2 provides signals for tracking page load progress:
- `WebKit2.LoadEvent.STARTED`: Page load started
- `WebKit2.LoadEvent.REDIRECTED`: Following a redirect
- `WebKit2.LoadEvent.COMMITTED`: Data starts arriving
- `WebKit2.LoadEvent.FINISHED`: Load complete

### Navigation Methods

The WebKit2.WebView provides standard browser navigation:
- `load_uri(url)`: Load a URL
- `go_back()`: Navigate back in history
- `go_forward()`: Navigate forward in history
- `reload()`: Reload current page
- `get_uri()`: Get current page URL

## System Dependencies

### Required Libraries

1. **Python 3**: The programming language
2. **PyGObject**: Python GObject Introspection bindings
3. **GTK+ 3**: The GUI toolkit
4. **WebKit2GTK 4.0**: The WebKit rendering engine

### Installation Commands

#### Ubuntu/Debian
```bash
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0
```

#### Fedora
```bash
sudo dnf install python3-gobject gtk3 webkit2gtk3
```

#### Arch Linux
```bash
sudo pacman -S python-gobject gtk3 webkit2gtk
```

## Build System Integration

The Makefile includes a dependency checker:

```bash
make check-deps
```

This verifies that all required components are installed before running the browser.

## Testing the Import System

Run the test script to verify imports:

```bash
python3 test_imports.py
```

This will test each import step and report any missing dependencies.

## How It Works

1. **PyGObject Introspection**: Uses GObject Introspection to automatically generate Python bindings from the C libraries
2. **Dynamic Loading**: Libraries are loaded at runtime based on the required versions
3. **Type Safety**: GObject Introspection provides type information for better Python integration
4. **Signal System**: GTK/GObject signal system allows event-driven programming

## Example Usage

```python
import gi
gi.require_version('WebKit2', '4.0')
from gi.repository import WebKit2

# Create a WebView
webview = WebKit2.WebView()

# Load a URL
webview.load_uri("https://www.example.com")

# Connect to load events
webview.connect("load-changed", callback_function)
```

## Advantages of This Approach

1. **Native Performance**: WebKit2GTK is a native library, providing full browser performance
2. **Standards Compliant**: Full WebKit rendering engine with modern web standards support
3. **Well Maintained**: WebKit2GTK is actively maintained as part of the WebKit project
4. **Cross-Platform**: Works on all major Linux distributions
5. **Python Integration**: Easy to use from Python while maintaining native performance

## References

- [WebKit2GTK API Documentation](https://webkitgtk.org/reference/webkit2gtk/stable/)
- [PyGObject Documentation](https://pygobject.readthedocs.io/)
- [GTK+ 3 Documentation](https://docs.gtk.org/gtk3/)
