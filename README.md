# WebKit Light Browser

A lightweight web browser built using modern WebKitGTK and Python.

## Features

- Simple and clean interface
- Modern WebKit rendering engine
- Basic navigation (back, forward, refresh)
- URL bar for direct navigation

## Requirements

- Python 3.6+
- GTK+ 3
- WebKitGTK 6.0
- PyGObject

## Installation

### Ubuntu/Debian
```bash
sudo apt-get install python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit-6.0
pip3 install -r requirements.txt
```

### Fedora
```bash
sudo dnf install python3-gobject gtk3 webkit2gtk
pip3 install -r requirements.txt
```

### Arch Linux
```bash
sudo pacman -S python-gobject gtk3 webkit2gtk
pip3 install -r requirements.txt
```

## Usage

```bash
./browser.py
# or
python3 browser.py
# or
make run
```

## License

GNU General Public License v3.0 - see LICENSE file for details.
