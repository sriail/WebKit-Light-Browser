# WebKit Light Browser

A lightweight web browser application built using WebKit2GTK and Python.

## Features

- Simple and clean user interface
- WebKit-based rendering engine
- Basic navigation controls (back, forward, refresh)
- URL bar for direct navigation
- Cross-platform support (Linux primarily)

## Requirements

- Python 3.6 or higher
- GTK+ 3
- WebKit2GTK 4.0
- PyGObject (Python GObject Introspection bindings)

## Installation

### System Dependencies

#### Ubuntu/Debian
```bash
sudo apt-get update
sudo apt-get install python3 python3-gi python3-gi-cairo gir1.2-gtk-3.0 gir1.2-webkit2-4.0
```

#### Fedora
```bash
sudo dnf install python3 python3-gobject gtk3 webkit2gtk3
```

#### Arch Linux
```bash
sudo pacman -S python python-gobject gtk3 webkit2gtk
```

### Python Dependencies

```bash
pip3 install -r requirements.txt
```

## Building and Running

### Make the browser executable
```bash
chmod +x browser.py
```

### Run the browser
```bash
./browser.py
```

Or:
```bash
python3 browser.py
```

### Using Make (optional)
```bash
make run
```

## Usage

1. Launch the browser using one of the methods above
2. Enter a URL in the address bar and press Enter or click the Go button
3. Use the navigation buttons to go back, forward, or refresh the page
4. The browser will automatically add `https://` to URLs without a protocol

## Architecture

The browser is built using:
- **WebKit2GTK**: The WebKit rendering engine with GTK+ 3 bindings
- **PyGObject**: Python bindings for GObject-based libraries
- **GTK+ 3**: The GUI toolkit

The main components:
- `browser.py`: Main application file containing the browser window and WebKit integration
- `requirements.txt`: Python package dependencies
- `Makefile`: Build and run automation

## License

This project is licensed under the GNU General Public License v3.0 - see the LICENSE file for details.

## Contributing

Contributions are welcome! Please feel free to submit pull requests or open issues.

## Future Enhancements

- Bookmark management
- Tab support
- Download manager
- Settings and preferences
- History tracking
- Search engine integration
- Developer tools
