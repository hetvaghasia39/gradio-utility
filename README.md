# gradio-utility

# Converting Python Script to Executable (EXE)
A complete guide to create an executable from your Python script

## Method 1: Using PyInstaller (Recommended)

### Step 1: Set Up Your Environment
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# Mac/Linux:
source venv/bin/activate

# Install PyInstaller
pip install pyinstaller
```

### Step 2: Basic Conversion
```bash
# Simple conversion (creates a folder with dependencies)
pyinstaller run.py

# Create single file executable
pyinstaller --onefile run.py

# Create executable with custom name
pyinstaller --onefile --name MyApp run.py

# Create executable without console window (for GUI apps)
pyinstaller --onefile --windowed run.py
```

### Step 3: Handle Dependencies
Create a requirements.txt:
```bash
# Generate requirements file
pip freeze > requirements.txt

# Install all required packages
pip install -r requirements.txt
```

### Step 4: Create Spec File (for Complex Applications)
```bash
# Generate spec file
pyi-makespec run.py

# For GUI applications
pyi-makespec --windowed run.py
```

### Step 5: Build from Spec File
```bash
pyinstaller run.spec
```

## Method 2: Using Auto-py-to-exe (GUI Option)

### Step 1: Install auto-py-to-exe
```bash
pip install auto-py-to-exe
```

### Step 2: Launch GUI
```bash
auto-py-to-exe
```

### Step 3: In the GUI:
1. Select your Python script
2. Choose conversion mode (One Directory/One File)
3. Select Console/Window Based
4. Add additional files if needed
5. Click 'Convert'

## Project Structure Best Practices

```
your_project/
├── src/
│   ├── main.py          # Your main script
│   ├── modules/         # Your modules
│   └── assets/          # Resources
├── requirements.txt     # Dependencies
├── build/              # Build files
└── dist/               # Final executable
```

## Common Issues and Solutions

### 1. Missing Dependencies
```python
# Add hidden imports in spec file
hiddenimports=['numpy', 'pandas']
```

### 2. Missing Files/Assets
```python
# Add data files in spec file
datas=[
    ('path/to/file.yaml', '.'),
    ('path/to/assets', 'assets'),
]
```

### 3. Large File Size
```bash
# Use UPX for compression
pyinstaller --onefile --upx-dir=/path/to/upx run.py
```

### 4. DLL Missing Errors
```python
# Add in spec file
binaries=[('path/to/dll', '.')]
```

## Checklist Before Distribution

1. Test executable on a clean machine
2. Verify all required files are included
3. Check for antivirus false positives
4. Include any required configuration files
5. Create distribution package with:
   - Executable
   - Config files
   - README
   - License

## Command Line Options Reference

```bash
# Basic options
--onefile       # Create single executable
--windowed      # No console window
--name NAME     # Custom name
--icon=FILE     # Custom icon
--noconsole     # Hide console
--clean         # Clean cache
--debug         # Debug mode
--upx-dir=DIR   # UPX directory
```

## Testing Your Executable

1. Test on clean virtual machine
2. Test all functionality
3. Check startup time
4. Verify file paths
5. Test error handling

## Security Considerations

1. Avoid hardcoding sensitive data
2. Use environment variables
3. Implement proper error handling
4. Consider code obfuscation
5. Sign your executable (recommended)