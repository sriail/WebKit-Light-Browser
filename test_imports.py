#!/usr/bin/env python3
"""
Test script to verify WebKit import system
This script tests that all necessary imports can be loaded
"""

import sys

def test_imports():
    """Test that all required imports work"""
    print("Testing WebKit import system...")
    print("-" * 50)
    
    # Test 1: Import gi module
    print("1. Testing gi (PyGObject) import...")
    try:
        import gi
        print("   ✓ gi module imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import gi: {e}")
        return False
    
    # Test 2: Require GTK version
    print("2. Testing GTK+ 3.0 requirement...")
    try:
        gi.require_version('Gtk', '3.0')
        print("   ✓ GTK+ 3.0 version requirement set")
    except (ValueError, AttributeError) as e:
        print(f"   ✗ Failed to set GTK version: {e}")
        print("   Note: This is expected if GTK is not installed")
        print("   Install with: sudo apt-get install gir1.2-gtk-3.0")
        return False
    
    # Test 3: Require WebKit2 version
    print("3. Testing WebKit2 4.0 requirement...")
    try:
        gi.require_version('WebKit2', '4.0')
        print("   ✓ WebKit2 4.0 version requirement set")
    except (ValueError, AttributeError) as e:
        print(f"   ✗ Failed to set WebKit2 version: {e}")
        print("   Note: This is expected if WebKit2GTK is not installed")
        print("   Install with: sudo apt-get install gir1.2-webkit2-4.0")
        return False
    
    # Test 4: Import from gi.repository
    print("4. Testing gi.repository imports...")
    try:
        from gi.repository import Gtk, WebKit2, GLib
        print("   ✓ Gtk imported successfully")
        print("   ✓ WebKit2 imported successfully")
        print("   ✓ GLib imported successfully")
    except ImportError as e:
        print(f"   ✗ Failed to import from gi.repository: {e}")
        return False
    
    # Test 5: Verify WebKit2.WebView class exists
    print("5. Testing WebKit2.WebView class...")
    try:
        webview_class = WebKit2.WebView
        print(f"   ✓ WebKit2.WebView class available: {webview_class}")
    except AttributeError as e:
        print(f"   ✗ WebKit2.WebView not found: {e}")
        return False
    
    print("-" * 50)
    print("✓ All WebKit import tests passed!")
    print("\nThe WebKit import system is correctly configured.")
    return True


if __name__ == "__main__":
    success = test_imports()
    sys.exit(0 if success else 1)
