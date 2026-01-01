.PHONY: help run clean install check-deps

help:
	@echo "WebKit Light Browser - Makefile"
	@echo ""
	@echo "Available targets:"
	@echo "  make run         - Run the browser application"
	@echo "  make check-deps  - Check if system dependencies are installed"
	@echo "  make install     - Install Python dependencies"
	@echo "  make clean       - Clean temporary files"
	@echo "  make help        - Show this help message"

run: browser.py
	@echo "Starting WebKit Light Browser..."
	python3 browser.py

check-deps:
	@echo "Checking system dependencies..."
	@which python3 > /dev/null || (echo "ERROR: python3 not found" && exit 1)
	@python3 -c "import gi" 2>/dev/null || (echo "ERROR: PyGObject not installed" && exit 1)
	@python3 -c "import gi; gi.require_version('Gtk', '3.0'); from gi.repository import Gtk" 2>/dev/null || (echo "ERROR: GTK+ 3 bindings not found" && exit 1)
	@python3 -c "import gi; gi.require_version('WebKit2', '4.0'); from gi.repository import WebKit2" 2>/dev/null || (echo "ERROR: WebKit2GTK bindings not found" && exit 1)
	@echo "All dependencies are installed!"

install:
	@echo "Installing Python dependencies..."
	pip3 install -r requirements.txt

clean:
	@echo "Cleaning temporary files..."
	find . -type f -name "*.pyc" -delete
	find . -type d -name "__pycache__" -delete
	@echo "Clean complete!"
